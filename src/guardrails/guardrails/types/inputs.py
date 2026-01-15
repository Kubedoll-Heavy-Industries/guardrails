from typing import Union

from guardrails.prompt.prompt import Prompt

"""List[Dict[str, Union[Prompt, str]]]"""
MessageHistory = list[dict[str, Union[Prompt, str]]]
