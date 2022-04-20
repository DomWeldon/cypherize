"""Parse python schema objects"""
import typing

from .. import project_types as pt
from .. import utils


def parse_label_properties(
    annos: typing.Dict[str, type],
    unique: typing.Optional[typing.Set[str]] = None,
) -> pt.NodeLabelProperties:
    """Parse all label properties"""
    return pt.NodeLabelProperties(
        {
            "exist": {
                pt.Property(property_name): property_type
                for property_name, property_type in annos.items()
                if not utils.is_optional_type(property_type)
            },
            "unique": {u: annos[u] for u in (unique or {}) & annos.keys()},
            "all": {
                pt.Property(property_name): property_type
                for property_name, property_type in annos.items()
            },
        }
    )
