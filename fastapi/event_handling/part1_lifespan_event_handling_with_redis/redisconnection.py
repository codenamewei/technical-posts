#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-11-05
# Updated Date: 2023-11-05
# version ='1.0'
# ---------------------------------------------------------------------------

import redis
import logging

class RedisConnection:

    redisconn = None

    def start_connection(self):
        
        try:

            self.redisconn = redis.Redis(host='localhost', port=6379, db=0)

            self.redisconn.ping()

        except ConnectionError as e:

            raise ConnectionError("Connection to Redis. Check is Redis is up")
        
        else:

            logging.info("Connection to Redis is up.")

    def close_connection(self):

        self.redisconn.close()

        logging.info("Connection to Redis is down.")

    def write(self, key : str, value : int):

        self.redisconn.set(key, value)

    def read(self, key : str):

        return self.redisconn.get(key)