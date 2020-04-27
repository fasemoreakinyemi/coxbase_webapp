#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import or_
from sqlalchemy import and_
import json
from .. import process_request
from .. import newick_generator
import uuid

Base = automap_base()
settings = get_appsettings("/home/ubuntu/coxbase/coxbase/webapp/development.ini", name="main")
engine = engine_from_config(settings, 'db2.')
Base.prepare(engine, reflect=True)
RP = process_request.RequestProcessor()
NG = newick_generator.NewickProcessor()

@view_config(route_name='mlva_tree',renderer='json')
def mlva_tree_view(request):
    container = request.matchdict["ent"]
    query_container = json.loads(container)
    mlvaTable = Base.classes.mlva_normalized
    mlva_list = []
    index_list = []
    
    for items in query_container:
        entry_list = []
        query = request.db2_session.query(mlvaTable).filter(
            mlvaTable.ngt == items[0]).all()
        if query:
            mlva_values = RP._serialize_mlva_tolist(query)
            mlva_values = [float(x) for x in mlva_values]
            mlva_list.append(mlva_values)
            index_list.append(items[1])
        else:
            continue
    newick_string = NG.generate_newick(mlva_list, index_list)
    return  {'newick': newick_string }

@view_config(route_name='mlva_tree_2',renderer='json')
def mlva_tree_view_2(request):
    process_ID = uuid.uuid4().hex
    item_list = []
    for items in request.params:
        item_list.append(items)
    query_container = json.loads(item_list[0])
    mlvaTable = Base.classes.mlva_normalized
    mlva_list = []
    index_list = []
    metadata_list = [["ID","Host"]]
    
    for items in query_container:
        entry_list = []
        query = request.db2_session.query(mlvaTable).filter(
            mlvaTable.ngt == items[0]).all()
        if query:
            mlva_values = RP._serialize_mlva_tolist(query)
            mlva_values = [float(x) for x in mlva_values]
            mlva_list.append(mlva_values)
            index_list.append(items[1])
            metadata_list.append([items[1], items[2]])
        else:
            continue
    newick_string = NG.generate_newick(mlva_list, index_list)
    NG.write_newick(process_ID, newick_string)
    NG.write_metadata(process_ID, metadata_list)
    return  {'itms': "{}".format(process_ID) }
#   return {'itms': item_list}

