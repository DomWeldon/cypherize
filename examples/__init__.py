import typing

from cypherize.schema.models import declarative_base

Base = declarative_base()


class Book(Base):
    """A book written by >=0 authors"""
    __cypherize_args__ = {
        "unique": {"id"}
    }

    id: int
    title: str
    year: typing.Optional[int]

    class EdgesIn:
        AUTHOR_WROTE_BOOK = relationship()


class Person(Base):
    """A human being."""
    __cypherize_args__ = {
        "unique": {"id"}
    }

    id: int
    name: str

class Author(Person):
    """Person who has written a book."""
    pseudonym: str


Book(title="To Kill a Mocking Bird") \
    .EdgesOut.AUTHOR_WROTE_BOOK.where(primary=True)
