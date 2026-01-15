import logging
from dataclasses import dataclass

from typing_extensions import deprecated

from guardrails.classes.generic.serializeable import SerializeableJSONEncoder
from guardrails.classes.rc import RC

BOOL_CONFIGS = {"no_metrics", "enable_metrics", "use_remote_inferencing"}


@deprecated(
    (
        "The `Credentials` class is deprecated and will be removed in version 0.6.x."
        " Use the `RC` class instead."
    ),
    category=DeprecationWarning,
)
@dataclass
class Credentials(RC):
    no_metrics: bool | None = False

    @staticmethod
    def _to_bool(value: str) -> bool | None:
        if value.lower() == "true":
            return True
        if value.lower() == "false":
            return False
        return None

    @staticmethod
    def has_rc_file() -> bool:
        return RC.exists()

    @staticmethod
    def from_rc_file(logger: logging.Logger | None = None) -> "Credentials":  # type: ignore
        rc = RC.load(logger)
        return Credentials(  # type: ignore
            id=rc.id,
            token=rc.token,
            enable_metrics=rc.enable_metrics,
            use_remote_inferencing=rc.use_remote_inferencing,
            no_metrics=(not rc.enable_metrics),
            encoder=SerializeableJSONEncoder(),
        )
