from typing import TypeVar

_T = TypeVar('_T')


def greater_than(a: _T, b: _T, /) -> bool:
    pass


def greater_than_or_equal_to(a: _T, b: _T, /) -> bool:
    pass


def less_than(a: _T, b: _T, /) -> bool:
    pass


def less_than_or_equal_to(a: _T, b: _T, /) -> bool:
    pass


def equal_to(a: _T, b: _T, /) -> bool:
    pass


def not_equal_to(a: _T, b: _T, /) -> bool:
    pass
