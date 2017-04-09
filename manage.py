#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-09 12:57:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from flask_script import Manager
from appliction import create_app

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
	manager.run()
