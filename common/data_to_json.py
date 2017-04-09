#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-09 14:36:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

# class DataEncoder(json.JSONEncoder):
# 	def default(self, obj):
# 		if isinstance(obj, User):
# 			return obj.name
# 		return json.JSONEncoder.default(self, obj)
def convert_to_builtin_type(obj):
    #print 'default(', repr(obj), ')'
    # d = { '__class__':obj.__class__.__name__, 
    #       '__module__':obj.__module__,
    #     }
    d = {}
    d.update(obj.__dict__)
    return d
def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        print "MODULE:",module
        class_ = getattr(module,class_name)
        print "CLASS",class_
        args = dict((key.encode('ascii'),value) for key,value in d.items())
        print 'INSTANCE ARGS:',args
        inst = class_(**args)
    else:
        inst = d
    return inst
# print json.dumps(obj, default=convert_to_builtin_type)
# encoded_object = '[{"s":"helloworld","__module__":"jsontest","__class__":"MyObj"}]'
# myobj_instance = json.loads(encoded_object,object_hook=dict_to_object)
# print myobj_instance