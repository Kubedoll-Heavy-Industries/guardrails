from contextlib import AbstractContextManager
from types import TracebackType
from unittest.mock import MagicMock


class MockSpan(AbstractContextManager):
    def __exit__(
        self,
        __exc_type: type[BaseException] | None,
        __exc_value: BaseException | None,
        __traceback: TracebackType | None,
    ) -> bool | None:
        return super().__exit__(__exc_type, __exc_value, __traceback)

    def __init__(self):
        super().__init__()
        self.set_attribute = MagicMock()
