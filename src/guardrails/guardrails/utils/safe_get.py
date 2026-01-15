from typing import Any, Union

from guardrails.logger import logger


def safe_get_with_brackets(
    container: Union[str, list[Any], Any], key: Any, default: Any | None = None
) -> Any:
    try:
        value = container[key]
        if not value:
            return default
        return value
    except Exception as e:
        logger.debug(
            f"""
            Failed to get value for key: {key} out of container: {container}.
            Reason: {e}
            Fallbacking to default value...
            """
        )
        return default


def safe_get(
    container: Union[str, list[Any], dict[Any, Any], tuple],
    key: Any,
    default: Any | None = None,
) -> Any:
    if isinstance(container, dict):
        return container.get(key, default)
    else:
        return safe_get_with_brackets(container, key, default)
