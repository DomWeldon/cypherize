# Standard Library
import typing

# Third Party Libraries
import pytest

# App and Model Imports
from cypherize import schema


def test_expected_labels():
    """Check for expected labels"""
    # arrange and act
    Base = schema.declarative_base()

    class A(Base):
        __cypherize_args__ = {"unique": {"id"}}
        id: int
        name: str
        description: typing.Optional[str] = None

    # assert
    assert A.__cypherize_model__["labels"]["A"]["exist"] == {
        "id": int,
        "name": str,
    }
    assert A.__cypherize_model__["labels"]["A"]["all"] == {
        "id": int,
        "name": str,
        "description": typing.Optional[str],
    }
    assert A.__cypherize_model__["labels"]["A"]["unique"] == {"id": int}


def test_expected_labels_inheritance():
    """Check for expected labels"""
    # arrange
    Base = schema.declarative_base()

    class A(Base):
        id: int
        name: str
        description: typing.Optional[str] = None

    class AA(Base):
        id: int
        name: str
        description: typing.Optional[str] = None

    class B(A):
        id: int
        uuid: str

    class C(B):
        ref: float

    class D(AA, B):
        identifier: int

    # assert
    print(A.__cypherize_model__["labels"])
    assert A.__cypherize_model__["labels"].keys() == {"A"}
    assert B.__cypherize_model__["labels"].keys() == set("BA")
    assert C.__cypherize_model__["labels"].keys() == set("CBA")
    assert D.__cypherize_model__["labels"].keys() == set("DBA") | {"AA"}

# @pytest.mark.skip()
def test_expected_dataclass():
    """Does it also behave as a dataclass?"""
    # arrange
    Base = schema.declarative_base()

    class A(Base):
        id: int
        name: str
        description: typing.Optional[str]

    # act
    model = A(id=1, name="test", description="description")

    # assert
    assert model.id == 1
    assert model.name == "test"
    assert model.description == "description"


def test_base_separation():
    """Do different bases contain separate schemas correctly?"""
    # arrange
    BaseA = schema.declarative_base()
    BaseB = schema.declarative_base()

    # act
    class A(BaseA):
        id: int

    class B(BaseB):
        id: int

    # assert
    assert len(BaseA.__cypherize_schema__.G) == 1
    assert len(BaseB.__cypherize_schema__.G) == 1
    assert A in BaseA.__cypherize_schema__.G
    assert B in BaseB.__cypherize_schema__.G


def test_expected_auto_node_labels():
    """Check for expected labels"""
    # arrange
    Base = schema.declarative_base()

    # act
    class A(Base):
        id: int
        name: str
        description: typing.Optional[str] = None

    class AB(Base):
        __cypherize_node_label__ = "Woof"

        id: int
        name: str
        description: typing.Optional[str] = None


    # assert
    assert A.__cypherize_node_label__ == "A"
    assert AB.__cypherize_node_label__ == "Woof"
