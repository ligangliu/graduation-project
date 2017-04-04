#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-03 17:20:55
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import base_conn
from flask import Flask,jsonify
#app = Flask(__name__)

#@app.route('/')
def get_list_by_cursor(cursor):
	list = []
	for x in cursor:
		list.append(x)
	return list
def get_all_stations():
	stations = base_conn.get_collection_names()
	count = len(stations)
	return {'stations':stations,'count':count}
	#return jsonify({'stations':stations})
	#return jsonify({'a':'dsaf'})
#print get_all_stations()

def get_stations_count():
	stations_count = len(base_conn.get_collection_names())
	return {'stations_count':stations_count}

def get_station_count(station_name):
	station_count = base_conn.get_conn(collection_name=station_name).find().count()
	return {'station_count':station_count}

def get_list_by_station_time(station_name,starttime,endtime):
	conn = base_conn.get_conn(station_name)
	cursor = conn.find({
		'$and':[
			{'STATION':station_name},
			{'DATE':{'$gte':starttime,'$lte':endtime}}
		]
	},{'_id':0,'TIME':1,'X':1,'Y':1,'Z':1})
	#cursor = conn.find({'STATION':station_name,'DATE':{'$gte':starttime,'$lte':endtime}},{'_id':0})
	list = get_list_by_cursor(cursor)
	count = len(list)
	return {'list':list,'count':count}

# print get_all_stations()
# print get_stations_count()
# print get_station_count('Kourou')
# @app.route('/')
# def index():
# 	return jsonify(get_list_by_station_time(station_name='person', starttime='2017-03-15', endtime='2017-03-16'))
print get_list_by_station_time(station_name='Kourou', starttime='2017-03-15', endtime='2017-03-16')

# if __name__ == '__main__':
#  	app.run(debug=True)