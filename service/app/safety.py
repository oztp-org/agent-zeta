"""
Input validation and prompt injection defense for the Agent Zeta web API.

Defense layers:
1. Length and count limits — limits blast radius of any single request
2. Role validation — only "user"/"assistant" allowed; system role cannot be injected
3. Injection pattern detection — catches classic override attempts
4. Claude's own safety layer — the final line of defense, always present

The system prompt is never sent to or overridable by the client. It lives
server-side only, injected at call time.
"""
import re
from typing import NamedTuple

MAX_MESSAGE_LENGTH = 2000      # chars per individual message
MAX_HISTORY_MESSAGES = 12      # total messages in a conversation
MAX_TOTAL_CHARS = 8000         # total across all messages in a request

# Conservative set — only patterns that clearly signal injection intent,
# not anything that might appear in a legitimate Zero Trust question.
_INJECTION_PATTERNS = [
    r"ignore\s+(previous|all|above|prior|your)\s+(instructions?|prompts?|directives?|system)",
    r"disregard\s+(your|the|all|previous)\s+(instructions?|system|prompt|role)",
    r"forget\s+(your|all|previous|the)\s+(instructions?|training|role|purpose|constraints?)",
    r"new\s+system\s+(prompt|instructions?|directive)",
    r"override\s+(your|the)\s+(instructions?|system|prompt|constraints?)",
    r"you\s+are\s+no\s+longer",
    r"jailbreak",
    r"DAN\s+mode",
    r"developer\s+mode\s+enabled",
    r"<\|system\|>",
    r"\[SYSTEM\]",
    r"###\s*system\s*:",
    r"<<SYS>>",
    r"\[INST\]",
]

_compiled = [re.compile(p, re.IGNORECASE) for p in _INJECTION_PATTERNS]


class ValidationResult(NamedTuple):
    ok: bool
    reason: str = ""


def validate_messages(messages: list[dict]) -> ValidationResult:
    if not messages:
        return ValidationResult(False, "No messages provided")

    if len(messages) > MAX_HISTORY_MESSAGES:
        return ValidationResult(False, f"Too many messages in history (max {MAX_HISTORY_MESSAGES})")

    total_chars = 0
    for i, msg in enumerate(messages):
        role = msg.get("role", "")
        content = msg.get("content", "")

        if role not in ("user", "assistant"):
            return ValidationResult(False, f"Invalid role '{role}' at position {i}")

        if not isinstance(content, str):
            return ValidationResult(False, f"Message content must be a string at position {i}")

        # Strip null bytes and control characters before length check
        content = content.replace("\x00", "").strip()

        if len(content) > MAX_MESSAGE_LENGTH:
            return ValidationResult(
                False, f"Message at position {i} too long (max {MAX_MESSAGE_LENGTH} chars)"
            )

        total_chars += len(content)

        # Scan user messages for injection patterns
        if role == "user":
            for pattern in _compiled:
                if pattern.search(content):
                    return ValidationResult(False, "Message contains disallowed content")

    if total_chars > MAX_TOTAL_CHARS:
        return ValidationResult(False, "Conversation history too large")

    if messages[-1].get("role") != "user":
        return ValidationResult(False, "The last message must be from the user")

    return ValidationResult(True)
