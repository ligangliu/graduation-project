#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-02 15:49:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import Flask,jsonify
import datetime
from common import base_conn

app = Flask(__name__)
print base_conn.get_collection_names()

if __name__ == '__main__':
	app.run()
