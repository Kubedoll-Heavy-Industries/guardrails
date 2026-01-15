import warnings
from typing import Any


def to_int(v: Any) -> int | None:
    try:
        int_value = int(v)
        return int_value
    except Exception:
        return None


def to_float(v: Any) -> float | None:
    try:
        float_value = float(v)
        return float_value
    except Exception:
        return None


def to_string(v: Any) -> str | None:
    try:
        str_value = str(v)
        return str_value
    except Exception:
        return None


def to_bool(value: str) -> bool | None:
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    warnings.warn(f"Could not cast {value} to bool. Returning None.")
    return None
