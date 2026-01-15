from collections.abc import Callable
from typing import Any, Union

from guardrails.validator_base import Validator

PydanticValidatorTuple = tuple[Union[Validator, str, Callable], str]
PydanticValidatorSpec = Union[Validator, PydanticValidatorTuple]

UseValidatorSpec = Union[Validator, type[Validator]]

UseManyValidatorTuple = tuple[
    type[Validator],
    Union[list[Any], dict[str, Any]] | None,
    dict[str, Any] | None,
]
UseManyValidatorSpec = Union[Validator, UseManyValidatorTuple]

ValidatorMap = dict[str, list[Validator]]
