#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base
from .. import process_request
from sqlalchemy import or_
from .. import models
import logging
import traceback
import sys

Base = automap_base()
settings = get_appsettings(
        "/home/travis/build/foerstner-lab/CoxBase-Webapp/development.ini", name="main"
    )
engine = engine_from_config(settings, "db2.")
Base.prepare(engine, reflect=True)

@view_config(
    route_name="entry_view_mlva", renderer="../templates/mlva_query_view.jinja2"
)
def detailed_mlva_view(request):
    ID = request.matchdict["ID"]
    isolates = Base.classes.isolates
    isolatesRef = Base.classes.isolate_refs2
    try:
        query = request.db2_session.query(isolates).filter(isolates.mlvaGenotype == ID)
        # query = request.db2_session.query(isolates).join(isolatesRef, isolates.isolateid == isolatesRef.isolate_id).filter(isolatesRef.pmid  == 25037926).filter(
        #    isolates.mlvaGenotype == ID)
    except DBAPIError:
        return Response(db_err_msg, content_type="text/plain", status=500)
    return {"count": query.count(), "results": query.all()}


@view_config(
    route_name="entry_view_mlva_6", renderer="../templates/mlva_tilburg_query_view.jinja2"
)
def detailed_mlva_tilburg_view(request):
    ID = request.matchdict["ID"]
    isolates = Base.classes.isolates2022
    try:
        query = request.db2_session.query(isolates).filter(isolates.mlvaGenotype == ID)
    except DBAPIError:
        return Response(db_err_msg, content_type="text/plain", status=500)
    return {"count": query.count(), "results": query.all()}

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

