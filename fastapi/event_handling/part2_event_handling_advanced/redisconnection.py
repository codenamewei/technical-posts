import redis

class RedisConnection:

    redisconn = None

    def start_connection(self):

        self.redisconn = redis.Redis(host='localhost', port=6379, db=0)

    def close_connection(self):

        self.redisconn.close()

    def write(self, key : int, value : str):

        self.redisconn.set(key, value)

    def read(self, key : int):

        return self.redisconn.get(key)