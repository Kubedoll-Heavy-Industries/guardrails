import copy
from string import Template
from typing import cast

from guardrails.classes.output_type import OutputTypes
from guardrails.llm_providers import (
    AsyncLiteLLMCallable,
    LiteLLMCallable,
    PromptCallableBase,
)
from guardrails.prompt.instructions import Instructions
from guardrails.prompt.prompt import Prompt
from guardrails.types.inputs import MessageHistory


def messages_source(messages: MessageHistory) -> MessageHistory:
    messages_copy = []
    for msg in messages:
        msg_copy = copy.deepcopy(msg)
        content = (
            msg["content"].source
            if isinstance(msg["content"], Prompt) or isinstance(msg["content"], Instructions)
            else msg["content"]
        )
        msg_copy["content"] = content
        messages_copy.append(cast(dict[str, str], msg_copy))
    return messages_copy


def preprocess_prompt_for_string_output(
    prompt_callable: PromptCallableBase,
    instructions: Instructions | None,
    prompt: Prompt,
) -> tuple[Instructions | None, Prompt]:
    if isinstance(prompt_callable, LiteLLMCallable) or isinstance(
        prompt_callable, AsyncLiteLLMCallable
    ):
        prompt.source += "\n\nString Output:\n\n"
    if (
        isinstance(prompt_callable, LiteLLMCallable)
        or isinstance(prompt_callable, AsyncLiteLLMCallable)
    ) and not instructions:
        instructions = Instructions(
            "You are a helpful assistant, expressing yourself through a string."
        )

    return instructions, prompt


def preprocess_prompt_for_json_output(
    prompt_callable: PromptCallableBase,
    instructions: Instructions | None,
    prompt: Prompt,
    use_xml: bool,
) -> tuple[Instructions | None, Prompt]:
    if isinstance(prompt_callable, LiteLLMCallable) or isinstance(
        prompt_callable, AsyncLiteLLMCallable
    ):
        prompt.source += "\n\nJson Output:\n\n"
    if (
        isinstance(prompt_callable, LiteLLMCallable)
        or isinstance(prompt_callable, AsyncLiteLLMCallable)
    ) and not instructions:
        schema_type = "XML schemas" if use_xml else "JSON schema"
        instructions = Instructions(
            Template(
                "You are a helpful assistant, "
                "able to express yourself purely through JSON, "
                "strictly and precisely adhering to the provided ${schema_type}."
            ).safe_substitute(schema_type=schema_type)
        )

    return instructions, prompt


def preprocess_prompt(
    prompt_callable: PromptCallableBase,
    instructions: Instructions | None,
    prompt: Prompt,
    output_type: OutputTypes,
    use_xml: bool,
) -> tuple[Instructions | None, Prompt]:
    if output_type == OutputTypes.STRING:
        return preprocess_prompt_for_string_output(prompt_callable, instructions, prompt)
    return preprocess_prompt_for_json_output(prompt_callable, instructions, prompt, use_xml)
