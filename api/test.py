#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-09 12:54:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import json
from flask import jsonify
from api.main import main
from common.data_to_json import convert_to_builtin_type,dict_to_object
from common.base_conn import get_conn

class Person(object):
	"""docstring for Person"""
	def __init__(self, name,age,school):
		super(Person, self).__init__()
		self.name = name
		self.age = age
		self.school = school
	def __repr__(self):
		#return 'name: %s age: %s' %self.name %self.age
		return 'name :%s'%self.name

# person = Person('chenliqi', 20,'jiangxi')
# print json.dumps(person,default=convert_to_builtin_type)


#json_2 = {'user':User('orangle')}
#print json.dumps(json_2, cls=UserEncoder)
@main.route('/aa')
def index():
	d = Person('chenliqi', 20,'dsaf')
	print d
	a = {'a':1,'b':[1,2,3],
	'c':{'aa':1,'bb':'adsfda','cc':{'aaa':'ggggg'}},
	'd':Person('chenliqi', 20,'sdfa')}
	b = {'a':1,'b':[1,2,3],
	'c':{'aa':1,'bb':'adsfda','cc':{'aaa':'ggggg'}}}
	return json.dumps(a,default=convert_to_builtin_type)
	#return jsonify(b)
	#return {'a':1}
def get_list_by_cursor(cursor):
	list = []
	for x in cursor:
		list.append(x)
	return list
@main.route('/aaaa')
def index8():
    conn = get_conn()
    data = conn.find({},{'_id':0})
    datas = get_list_by_cursor(data)
    return jsonify({'a':datas})
    #return json.dumps(datas,default=convert_to_builtin_type)