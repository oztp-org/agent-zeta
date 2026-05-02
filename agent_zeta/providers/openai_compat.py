"""
OpenAI-compatible provider — works with OpenAI, Ollama, LM Studio, and any
server that implements the OpenAI Chat Completions API.

Ollama example config:
  base_url: "http://localhost:11434/v1"
  api_key: "ollama"
  model: "llama3.2:latest"

OpenAI example config:
  base_url: null  (uses the default OpenAI endpoint)
  api_key_env: "OPENAI_API_KEY"
  model: "gpt-4o"
"""
import os

from .base import ChatMessage, LLMProvider


class OpenAICompatProvider(LLMProvider):
    def __init__(
        self,
        model: str,
        base_url: str | None = None,
        api_key: str | None = None,
        api_key_env: str = "OPENAI_API_KEY",
    ):
        try:
            from openai import OpenAI
            self._openai_cls = OpenAI
        except ImportError:
            raise ImportError("Install the OpenAI SDK: pip install openai")

        self._model = model
        resolved_key = api_key or os.environ.get(api_key_env) or "no-key"
        self._client = self._openai_cls(api_key=resolved_key, base_url=base_url)
        self._base_url = base_url

    def chat(self, messages: list[ChatMessage], system: str = "") -> str:
        api_messages = []
        if system:
            api_messages.append({"role": "system", "content": system})
        api_messages += [{"role": m.role, "content": m.content} for m in messages]

        response = self._client.chat.completions.create(
            model=self._model,
            messages=api_messages,
            max_tokens=8192,
        )
        return response.choices[0].message.content or ""

    @property
    def model_name(self) -> str:
        return self._model

    @property
    def provider_label(self) -> str:
        location = self._base_url or "OpenAI"
        return f"OpenAI-compatible ({self._model} @ {location})"
