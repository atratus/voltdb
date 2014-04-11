#!/usr/bin/env python

# This file is part of VoltDB.
# Copyright (C) 2008-2014 VoltDB Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

{
    "basic-compoundex": {"schema": "schema.py",
                         "ddl": "compoundex-DDL.sql",
                         "template": "compound.sql",
                         "normalizer": "normalizer.py"},
# BIGINT OVERFLOW CAUSES FAILURES IN THIS SUITE, DISABLING
# also, the generator fails to generates statements for:
# Template "SELECT * FROM _table WHERE (_variable _cmp _value[int64]) _logic (_variable _cmp _variable)" failed to yield SQL statements
# Template "UPDATE _table SET BIG = _value[int64] WHERE (_variable _cmp _variable) _logic (_variable _cmp _value[int64])" failed to yield SQL statements
# Template "DELETE FROM _table WHERE (_variable _cmp _variable) _logic (_variable _cmp _value[int64])" failed to yield SQL statements
# because there are insufficient columns of the same type to satisfy all the _variables
# given how the generator works.
    "basic-ints": {"schema": "int-schema.py",
                   "ddl": "int-DDL.sql",
                   "template": "basic-ints.sql",
                   "normalizer": "normalizer.py"},
# HSQL SEEMS TO HAVE A BAD DEFAULT PRECISION, DISABLING
#    "basic-decimal": {"schema": "decimal-schema.py",
#                      "ddl": "DDL.sql",
#                      "template": "basic-decimal.sql",
#                      "normalizer": "normalizer.py"},
# Floating point rounding differences lead to deltas
#    "basic-timestamp": {"schema": "timestamp-schema.py",
#                        "ddl": "timestamp-DDL.sql",
#                        "template": "basic-timestamp.sql",
#                        "normalizer": "normalizer.py"},
# BIGINT OVERFLOW CAUSES FAILURES IN THIS SUITE
# also, the generator fails to generate statements for:
# Template "UPDATE _table SET BIG = _value[int64] WHERE (_variable _cmp _variable) _logic (_variable _cmp _value[int64])" failed to yield SQL statements
# Template "DELETE FROM _table WHERE (_variable _cmp _variable) _logic (_variable _cmp _value[int64])" failed to yield SQL statements
#    "basic-matview": {"schema": "matview-schema.py",
#                      "ddl": "int-DDL.sql",
#                      "template": "basic-matview.sql",
#                      "normalizer": "normalizer.py"},
     "basic-joins": {"schema": "schema.py",
                     "ddl": "DDL.sql",
                      "template": "basic-joins.sql",
                      "normalizer": "normalizer.py"},
     "basic-index-joins": {"schema": "schema.py",
                           "ddl": "index-DDL.sql",
                           "template": "basic-joins.sql",
                           "normalizer": "normalizer.py"},
     "basic-compoundex-joins": {"schema": "schema.py",
                                "ddl": "compoundex-DDL.sql",
                                "template": "basic-joins.sql",
                                "normalizer": "normalizer.py"},
# TODO: Need to scale down precision of values to keep HSQL happy even after math
    "numeric-decimals": {"schema": "decimal-schema.py",
                         "ddl": "DDL.sql",
                         "template": "numeric-decimals.sql",
                        "normalizer": "normalizer.py"},
    "numeric-ints": {"schema": "int-schema.py",
                     "ddl": "int-DDL.sql",
                     "template": "numeric-ints.sql",
                     "normalizer": "normalizer.py"},
# HSQL SEEMS TO HAVE A BAD DEFAULT PRECISION, DISABLING
#    "advanced-decimal": {"schema": "decimal-schema.py",
#                         "ddl": "DDL.sql",
#                         "template": "advanced-decimal.sql",
#                         "normalizer": "normalizer.py"},
    "advanced-joins": {"schema": "schema.py",
                       "ddl": "DDL.sql",
                       "template": "advanced-joins.sql",
                       "normalizer": "normalizer.py"},
    "advanced-index-joins": {"schema": "schema.py",
                             "ddl": "index-DDL.sql",
                             "template": "advanced-joins.sql",
                             "normalizer": "normalizer.py"},
    "advanced-subq-joins": {"schema": "schema.py",
                            "ddl": "DDL.sql",
                            "template": "advanced-subq-joins.sql",
                            "normalizer": "normalizer.py"},
    "advanced-repl-subq-joins": {"schema": "repl-schema.py",
                                 "ddl": "repl-DDL.sql",
                                 "template": "advanced-subq-joins.sql",
                                 "normalizer": "normalizer.py"},
    "advanced-compoundex-joins": {"schema": "schema.py",
                                  "ddl": "compoundex-DDL.sql",
                                  "template": "advanced-joins.sql",
                                  "normalizer": "normalizer.py"},
    "advanced-matview-repl-subq-nonjoin": {"schema": "matview-repl-schema.py",
                                 "ddl": "matview-repl-DDL.sql",
                                 "template": "advanced-matview-repl-subq-nonjoin.sql",
                                 "normalizer": "normalizer.py"},
}
