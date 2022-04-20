"""Define node relationships with objects for query generation."""
# Standard Library
import dataclasses
import itertools
import typing

import networkx as nx
import pydantic

# Local Folder
from .. import project_types as pt
from .. import utils
from . import parser

class EdgeDeclaration:
    """An edge has been declared to, or from, the node label this targets."""
    target: typing.Union[str, type, typing.Set[typing.Union[type, str]]]




class CypherizeModel(pydantic.BaseModel):
    """A model representing an entity in the graph database."""

    __cypherize_model__: pt.CypherizeModelProperties
    __cypherize_args__: pt.CypherizeArgs
    __cypherize_node_label__: pt.NodeLabel
    __cypherize_edges_out__: str
    __cypherize_edges_in__: str
    __cypherize_defaults__ = {
        "__cypherize_args__": (),
        "__cypherize_edges_in__": "EdgesIn",
        "__cypherize_edges_out__": "EdgesOut",
    }

    def __init_subclass__(cls, *args, **kwargs):
        """Create new cypherize dictionary."""
        super().__init_subclass__()

        # simple defaults
        for attr, val in defaults.items():
            if not hasattr(cls, attr):
                setattr(cls, attr, val)

        # reference defaults
        cls.__cypherize_model__ = {"labels": {}}


class CypherizeSchema:
    """Collection object for a graph schema.

    Used in other parts of the library to reason about the graph structure."""

    G: nx.MultiDiGraph
    """A "meta" graph of how the graph can be traversed according to schema"""

    node_labels: typing.Set[pt.NodeLabel]

    def __init__(self):
        self.G = nx.MultiDiGraph()

    def add_model(self, model: CypherizeModel):
        # when models have not been declared yet but are used in type
        # annotations, they are
        if model not in self.G and model.__name__ in self.G:
            # replace the (temporary string) node with model
            self.G = nx.relabel_nodes(
                self.G, {
                    model.__name__: model
                }
            )
            pass

        self.G.add_node(model)

        # parse relationships
        edge_attrs = [
            (slice(0, 1, 1), "__cypherize_edges_out__"),
            (slice(0, 1, 1), "__cypherize_edges_out__"),
        ]
        for uv_slice, attr in edge_attrs:
            # check we have some edged defined on this model in our schema
            if getattr(model, attr, None) is None:
                continue

            # we do,




class CypherizeBaseTemplate(CypherizeModel):
    """Node must have a label"""

    __cypherize_schema__: CypherizeSchema

    def __init_subclass__(cls, *args, **kwargs):
        """Populate dictionary as required."""
        super().__init_subclass__(cls, *args, **kwargs)

        if getattr(cls, "__cypherize_schema__", None) is None:
            cls.__cypherize_schema__ = CypherizeSchema()

        if cls.__name__ != cls.__cypherize_base_name__:
            cls.__cypherize_schema__.add_model(cls)

        # add the label to the pattern
        for i, parent in enumerate(cls.__mro__):
            if parent.__name__ == cls.__cypherize_base_name__:
                break
            if issubclass(parent, CypherizeBaseTemplate):
                annos = parent.__annotations__.items()
                cls.__cypherize_model__["labels"][
                    parent.__name__
                ] = parser.parse_label_properties(
                    parent.__annotations__,
                    unique=cls.__cypherize_args__.get("unique", None),
                )


class CypherizeBaseMeta(pydantic.main.ModelMetaclass):
    """Metaclass to add properties to models automatically."""

    @property
    def __cypherize_node_label__(self) -> str:
        """Label name of node."""
        # remember, data descriptors take precedence over class dict
        # properties in class attribute lookup, check the user has not
        # overriden the node label first
        if "__cypherize_node_label__" in self.__dict__:
            return self.__dict__["__cypherize_node_label__"]

        return self.__name__



def declarative_base(
    base_name: str = "CypherizeBase", metaclass=CypherizeBaseMeta
) -> CypherizeBaseTemplate:
    """Generate a class for a single schema inheritance."""

    return metaclass(
        base_name, (CypherizeBaseTemplate,), {"__cypherize_base_name__": base_name}
    )
