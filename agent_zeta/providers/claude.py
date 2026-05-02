import os

from .base import ChatMessage, LLMProvider

DEFAULT_MODEL = "claude-opus-4-7"


class ClaudeProvider(LLMProvider):
    def __init__(self, model: str = DEFAULT_MODEL, api_key: str | None = None):
        try:
            import anthropic
            self._anthropic = anthropic
        except ImportError:
            raise ImportError("Install the Anthropic SDK: pip install anthropic")

        self._model = model
        self._client = self._anthropic.Anthropic(
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY")
        )

    def chat(self, messages: list[ChatMessage], system: str = "") -> str:
        api_messages = [{"role": m.role, "content": m.content} for m in messages]

        kwargs: dict = {
            "model": self._model,
            "max_tokens": 8192,
            "messages": api_messages,
            "thinking": {"type": "adaptive"},
        }

        if system:
            # Stable system prompt — mark for prompt caching
            kwargs["system"] = [
                {"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}
            ]

        with self._client.messages.stream(**kwargs) as stream:
            message = stream.get_final_message()

        # Filter out thinking blocks; return the first text block
        text_blocks = [b for b in message.content if b.type == "text"]
        return text_blocks[0].text if text_blocks else ""

    @property
    def model_name(self) -> str:
        return self._model

    @property
    def provider_label(self) -> str:
        return f"Anthropic Claude ({self._model})"
