import logging
import os
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from agent_zeta.advisor import SYSTEM_PROMPT
from agent_zeta.providers.base import ChatMessage
from agent_zeta.providers.claude import ClaudeProvider

from .safety import validate_messages

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("agent-zeta-api")

limiter = Limiter(key_func=get_remote_address)
_provider: ClaudeProvider | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _provider
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        log.warning("ANTHROPIC_API_KEY not set — /v1/chat will fail")
    _provider = ClaudeProvider(
        model=os.environ.get("CLAUDE_MODEL", "claude-opus-4-7"),
        api_key=api_key,
    )
    log.info("Agent Zeta API ready (model: %s)", _provider.model_name)
    yield


ALLOWED_ORIGINS = [
    "https://oztp.org",
    "https://www.oztp.org",
    "https://oztp-org.github.io",
]
if os.environ.get("ENVIRONMENT") == "development":
    ALLOWED_ORIGINS += [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://127.0.0.1:5500",  # VS Code Live Server
    ]

app = FastAPI(
    title="Agent Zeta",
    description="AI Zero Trust Architecture Advisor — Open Zero Trust Project",
    version="0.1.0",
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["Content-Type"],
    max_age=600,
)


# ── Request / response models ─────────────────────────────────────────────────

class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]
    session_id: str | None = None


class ChatResponse(BaseModel):
    reply: str
    session_id: str


# ── Endpoints ─────────────────────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {"status": "ok", "service": "agent-zeta", "version": "0.1.0"}


@app.post("/v1/chat", response_model=ChatResponse)
@limiter.limit("15/minute")
async def chat(request: Request, body: ChatRequest):
    messages_raw = [{"role": m.role, "content": m.content} for m in body.messages]

    result = validate_messages(messages_raw)
    if not result.ok:
        raise HTTPException(status_code=422, detail=result.reason)

    chat_messages = [ChatMessage(role=m.role, content=m.content) for m in body.messages]

    try:
        reply = _provider.chat(chat_messages, system=SYSTEM_PROMPT)
    except Exception:
        log.exception("LLM call failed")
        raise HTTPException(status_code=502, detail="Advisor temporarily unavailable — please try again")

    session_id = body.session_id or str(uuid.uuid4())
    log.info("chat session=%s turns=%d", session_id[:8], len(body.messages))

    return ChatResponse(reply=reply, session_id=session_id)
