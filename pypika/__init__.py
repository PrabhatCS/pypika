"""
PyPika is divided into a couple of modules, primarily the ``queries`` and ``terms`` modules.

pypika.queries
--------------

This is where the ``Query`` class can be found which is the core class in PyPika.  Also, other top level classes such
as ``Table`` can be found here.  ``Query`` is a container that holds all of the ``Term`` types together and also
serializes the builder to a string.

pypika.terms
------------

This module contains the classes which represent individual parts of queries that extend the ``Term`` base class.

pypika.functions
----------------

Wrappers for common SQL functions are stored in this package.

pypika.enums
------------

Enumerated values are kept in this package which are used as options for Queries and Terms.


pypika.utils
------------

This contains all of the utility classes such as exceptions and decorators.

"""
from .dialects import (
    Dialects,
    MSSQLQuery,
    MySQLQuery,
    OracleQuery,
    PostgreSQLQuery,
    RedshiftQuery,
    VerticaQuery,
)
from .enums import (
    DatePart,
    JoinType,
    Order,
)
from .queries import (
    Query,
    Table,
    Tuple,
    make_tables as Tables,
)
from .terms import (
    Case,
    Field,
    Interval,
    Not,
    Rollup,
)
from .utils import (
    CaseException,
    GroupingException,
    JoinException,
    RollupException,
    UnionException,
)

__author__ = "Timothy Heys"
__email__ = "theys@kayak.com"
__version__ = "0.10.4"
