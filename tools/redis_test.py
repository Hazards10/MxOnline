# -*- coding: utf-8 -*-
__author__ = '隋宇飞'
__date__ = '2019/8/10  17:27'
import redis

r = redis.Redis(host='localhost', port=6379, db=0, charset="utf8", decode_responses=True )

r.set("mobile", "123")
r.expire("mobile", 1)
import time
time.sleep(1)
print(r.get("mobile"))