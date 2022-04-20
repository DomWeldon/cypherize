from . import models

CypherizeModel = models.CypherizeModel
declarative_base = models.declarative_base

__all__ = ["declarative_base", "CypherizeModel"]
