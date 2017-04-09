#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-09 14:29:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import Flask,jsonify,request
import datetime
from common.station import get_all_stations,get_list_by_station_time,get_stations_by_location
from api.main import main


@main.route('/station',methods=['GET'])
def get_stations():
	query = get_all_stations()
	if not query or query is None:
		print 'stations is empty'
		return jsonify({'error','stations is empty'}),404
	stations = query
	print stations
	return jsonify({'error':None,'station':stations})

@main.route('/station/<stationname>',methods=['GET'])
def get_station_list():
	if stationname is None:
		return jsonify({'error':'stattionname is not valid'}),404
	if request.json:
		info = request.json
		starttime = info[starttime]
		endtime = info[endtime]
		station_list = get_list_by_station_time(stationname,starttime,endtime)
		if not station_list or station_list is None:
			return jsonify({'error':None,'station_list':station_list})
		else:
			return jsonify({'error':'station_list is empty'})

@main.route('/station_location',methods=['GET'])
def get_location_stations():
	if request.json:
		info = request.json
		x_latitude = info[x_latitude]
		y_latitude = info[y_latitude]
		x_longitude = info[x_longitude]
		y_longitude = info[y_longitude]
		station_list = get_stations_by_location(x_latitude, y_latitude, x_longitude, y_longitude)
		if not station_list or station_list is None:
			return jsonify({'error':None,'station_list':station_list})
		else:
			return jsonify({'error':'station_list is empty'})	
