.. Cypherize documentation master file, created by
   sphinx-quickstart on Fri Mar 11 18:10:01 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Cypherize's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   API/modules


Design Principles of Cypherize
------------------------------

Cypherze is not a replacement for writing Cypher, it just automates the boring and repetitive parts, where you're likely to make mistakes.

You can faithfully record and recreate your graph schema constraints inside of python models, but you should take responsibility for migrations, because this is a schemaless graph, not an RDBMS.

Cypherize will build queries and hydrate models for you, but these are totally separate from your schema.

You can query in a way that doesn't match your schema and Cypherize won't care, unless you want it to.

We stick to the community edition, unless I need to use enterprise and/or Neo4j fund this.

Ponderings
----------

The property graph model allows a single node to have multiple labels, but also to enforce constraints on a node with a given label. Since a node can have more than one label, this means that any attempt to organise objects by label becomes problematic since there is no guarantee that different objects are different nodes. If a model is based on the idea of a node label, then two different objects (which are based on class definitions relating to different node labels), could reference the same node.

As a python developer, I want to be able to query my graph for a basic graph pattern, using auto-generated CQL, by writing object oriented python code.

These should be easy to plug into other libraries like FastAPI, using pydantic if possible.

Most of the creation behaviour using identities derived from node labels is likely to require a merge.

How to map the property graph model to the python class hieracrchy?

Hierarchies are linear, the property graph model is not.

An attribute on a model that retrieves nodes through edges (or shows the presence or absence thereof) is inherently a query. As such, it is not appropriate to define this within a schema, this is a query.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
