from cypherize import schema

def test_schema_contains_models():
    """Do all models make it into the graph?"""
    # arrange
    Base = schema.declarative_base()
    test_schema = Base.__cypherize_schema__

    # act
    class A(Base):
        id: int

    class B(Base):
        ref: str

    # assert
    assert A in test_schema.G
    assert B in test_schema.G
    assert len(test_schema.G) == 2
