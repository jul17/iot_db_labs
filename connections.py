import configparser
from azure.eventhub import EventHubProducerClient
import redis as redis_connection

config = configparser.ConfigParser()
config.read('app.config')

azure_redis = config['azure_redis']
redis_connection_str = redis_connection.StrictRedis(host=azure_redis['HOST'],
    port=int(azure_redis['PORT']), db=azure_redis['DB'], password=azure_redis['PASSWORD'], ssl=azure_redis.getboolean('SSL'))


event_hub = config['event-hub']
ev_h_connection_str = event_hub['CONNECTION_STR']
eventhub_name = event_hub['EVENT_HUB_NAME']
event_hub_client = EventHubProducerClient.from_connection_string(ev_h_connection_str, eventhub_name=eventhub_name)

mode = config['mode']
app_mode = mode['MODE']
    