from .base import ChatMessage, LLMProvider
from .claude import ClaudeProvider
from .openai_compat import OpenAICompatProvider


def build_provider(config: dict) -> LLMProvider:
    """Instantiate the correct LLM provider from a loaded config dict."""
    selected = config.get("provider", "claude")
    provider_configs = config.get("providers", {})
    cfg = provider_configs.get(selected, {})

    if selected == "claude":
        import os

        api_key = os.environ.get(cfg.get("api_key_env", "ANTHROPIC_API_KEY"))
        return ClaudeProvider(
            model=cfg.get("model", "claude-opus-4-7"),
            api_key=api_key,
        )
    elif selected == "openai_compat":
        return OpenAICompatProvider(
            model=cfg["model"],
            base_url=cfg.get("base_url"),
            api_key=cfg.get("api_key"),
            api_key_env=cfg.get("api_key_env", "OPENAI_API_KEY"),
        )
    else:
        raise ValueError(f"Unknown provider '{selected}'. Valid options: claude, openai_compat")


__all__ = ["ChatMessage", "LLMProvider", "ClaudeProvider", "OpenAICompatProvider", "build_provider"]
