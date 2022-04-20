# Standard Library
import typing

# Third Party Libraries
import pytest

# App and Model Imports
from cypherize import utils


# arrange
@pytest.mark.parametrize(
    "t,res",
    [
        (typing.Optional[int], True),
        (typing.Union[typing.Optional[int], float], True),
        (int, False),
        (typing.Union[int, float], False),
    ],
)
def test_is_optional_type(t: type, res: bool):
    """Check optional types are correct."""
    # act and assert
    assert utils.is_optional_type(t) is res
