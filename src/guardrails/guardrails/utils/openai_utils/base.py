import os
from typing import Any

from guardrails.classes.llm.llm_response import LLMResponse


class BaseOpenAIClient:
    def __init__(
        self,
        api_key: str | None = None,
        api_base: str | None = None,
    ):
        if api_key is None:
            api_key = os.environ.get("OPENAI_API_KEY")
        self.api_key = api_key
        self.api_base = api_base


class BaseSyncOpenAIClient(BaseOpenAIClient):
    def create_embedding(
        self,
        model: str,
        input: list[str],
    ) -> list[list[float]]:
        raise NotImplementedError

    def create_completion(self, engine: str, prompt: str, *args, **kwargs) -> LLMResponse:
        raise NotImplementedError

    def create_chat_completion(
        self, model: str, messages: list[Any], *args, **kwargs
    ) -> LLMResponse:
        raise NotImplementedError


class BaseAsyncOpenAIClient(BaseOpenAIClient):
    async def create_embedding(
        self,
        model: str,
        input: list[str],
    ) -> list[list[float]]:
        raise NotImplementedError

    async def create_completion(self, engine: str, prompt: str, *args, **kwargs) -> LLMResponse:
        raise NotImplementedError

    async def create_chat_completion(
        self, model: str, messages: list[Any], *args, **kwargs
    ) -> LLMResponse:
        raise NotImplementedError
