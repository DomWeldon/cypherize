"""Utility functions"""
# Standard Library
import typing


def is_optional_type(t: typing.Type):
    """Is this type optional?"""
    # is it None?
    if t is None or t is type(None):
        return True

    # is it a plain type?
    origin = typing.get_origin(t)
    if origin is None:
        # yes, so it's not optional
        return False

    args = typing.get_args(t)
    # can it be None?
    if origin is typing.Union:
        # are any of these types potentially None?
        return any(is_optional_type(t) for t in args)

    return False
