from dataclasses import dataclass


@dataclass
class GuardExecutionOptions:
    messages: list[dict] | None = None
    reask_messages: list[dict] | None = None
    num_reasks: int | None = None
