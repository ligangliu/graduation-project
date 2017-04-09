#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-09 12:39:14
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask import Flask
import config

def get_config():
	pass
def create_app():
	app = Flask(__name__)
	from api.main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	return app