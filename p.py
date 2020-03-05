import json
from confluent_kafka import Producer
from bson import json_util

conf = {'bootstrap.servers': 'localhost:9092', 'client.id': 'test', 'default.topic.config': {'acks': 'all'}}
producer = Producer(conf)

with open('dataset.json') as f:
  data = json.load(f)
  for x in data:
   producer.produce('sample', json.dumps(x, default=json_util.default).encode('utf-8'))
producer.flush()
