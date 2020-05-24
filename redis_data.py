import redis as redis_connection
import configparser
from connections import redis_connection_str as connection_str


class Redis:
    
    def get_data(self, r=connection_str):
        return r.get(self)
 
    def get_decode_data(self, r=connection_str):
        return r.get(self).decode("utf-8")  

    def set_data(self, value='test_value', r=connection_str):
        return r.set(self, value)

    def show_data(self, value='test_value', r=connection_str):
        return print(r.get(self).decode("utf-8"), flush=True)
