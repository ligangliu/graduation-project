#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-09 13:58:00
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import jsonify
import json
from . import main

@main.route('/aaa',methods=['GET','POST'])
def index1():
	a = {'a':1,'error':'station is empty'}
	#return jsonify(a)
	return jsonify({'a':1,'error':'station is empty'}),404
	#return json.dumps({'error','stations is empty'})
	#return jsonify({'error','stations is empty'}),404
