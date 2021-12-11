from typing import Callable, TypeVar

_T = TypeVar('_T')
_V = TypeVar('_V')


def wait_for_seconds(seconds: int, /):
    pass


def wait_until(get_value_function: Callable[[], _T], operator_function: Callable[[_T], _V], target_value: _V, /):
    pass


class Timer:

    def reset(self):
        pass

    def now(self) -> int:
        pass
