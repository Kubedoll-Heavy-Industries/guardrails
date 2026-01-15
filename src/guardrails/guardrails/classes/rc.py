import logging
import os
from dataclasses import dataclass
from os.path import expanduser

from guardrails.classes.generic.serializeable import Serializeable
from guardrails.utils.casting_utils import to_bool

BOOL_CONFIGS = {"no_metrics", "enable_metrics", "use_remote_inferencing"}


@dataclass
class RC(Serializeable):
    id: str | None = None
    token: str | None = None
    enable_metrics: bool | None = True
    use_remote_inferencing: bool | None = True

    @staticmethod
    def exists() -> bool:
        home = expanduser("~")
        guardrails_rc = os.path.join(home, ".guardrailsrc")
        return os.path.exists(guardrails_rc)

    @classmethod
    def load(cls, logger: logging.Logger | None = None) -> "RC":
        try:
            if not logger:
                logger = logging.getLogger()
            home = expanduser("~")
            guardrails_rc = os.path.join(home, ".guardrailsrc")
            with open(guardrails_rc, encoding="utf-8") as rc_file:
                lines = rc_file.readlines()
                filtered_lines = list(filter(lambda l: l.strip(), lines))
                config = {}
                for line in filtered_lines:
                    line_content = line.split("=", 1)
                    if len(line_content) != 2:
                        logger.warning(
                            """
                            Invalid line found in .guardrailsrc file!
                            All lines in this file should follow the format: key=value
                            Ignoring line contents...
                            """
                        )
                        logger.debug(f".guardrailsrc file location: {guardrails_rc}")
                    else:
                        key, value = line_content
                        key = key.strip()
                        value = value.strip()
                        if key in BOOL_CONFIGS:
                            value = to_bool(value)

                        config[key] = value

                rc_file.close()

                # backfill no_metrics, handle defaults
                # We missed this comment in the 0.5.0 release
                # Making it a TODO for 0.6.0
                # TODO: remove in 0.6.0
                no_metrics_val = config.pop("no_metrics", None)
                if no_metrics_val is not None and config.get("enable_metrics") is None:
                    config["enable_metrics"] = not no_metrics_val

                rc = cls.from_dict(config)
                return rc

        except FileNotFoundError:
            return cls.from_dict({})  # type: ignore
