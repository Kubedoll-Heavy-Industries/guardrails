from typing import Any

from guardrails.validator_base import (
    PassResult,
    ValidationResult,
    Validator,
    register_validator,
)


@register_validator(name="mock-validator", data_type="string")
class MockValidator(Validator):
    def validate(self, value: Any, metadata: dict) -> ValidationResult:
        return PassResult()
