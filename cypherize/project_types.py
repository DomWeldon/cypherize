import typing

Property = typing.NewType("Property", str)
"""Fundamental to the PGM"""

NodeLabel = typing.NewType("NodeLabel", str)
"""Used to group nodes in the PGM."""


class NodeLabelProperties(typing.TypedDict):
    """Possible properties on a node."""

    exist: typing.Dict[Property, type]
    unique: typing.Dict[Property, type]
    all: typing.Dict[Property, type]
    # index: typing.list[Index]


class CypherizeModelProperties(typing.TypedDict):
    """Properties of a cypherise model"""

    labels: typing.Dict[NodeLabel, NodeLabelProperties]


class CypherizeArgs(typing.TypedDict):
    """Args passed to cypherize as a class attribute."""

    unique: typing.Optional[typing.Set[Property]]
