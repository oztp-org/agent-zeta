from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ChatMessage:
    role: str  # "user" or "assistant"
    content: str


class LLMProvider(ABC):
    @abstractmethod
    def chat(self, messages: list[ChatMessage], system: str = "") -> str:
        """Send messages and return complete response text."""
        ...

    @property
    @abstractmethod
    def model_name(self) -> str:
        ...

    @property
    @abstractmethod
    def provider_label(self) -> str:
        ...
