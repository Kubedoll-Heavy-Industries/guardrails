from contextlib import AbstractContextManager
from types import TracebackType


class MockFile(AbstractContextManager):
    def __exit__(
        self,
        __exc_type: type[BaseException] | None,
        __exc_value: BaseException | None,
        __traceback: TracebackType | None,
    ) -> bool | None:
        return super().__exit__(__exc_type, __exc_value, __traceback)

    def readlines(self):
        pass

    def writelines(self, *args):
        pass

    def close(self):
        pass

    def read(self, *args):
        pass

    def write(self, *args):
        pass

    def seek(self, *args):
        pass
