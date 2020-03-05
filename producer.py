import json
from bson import json_util
import yaml

from kafka import KafkaProducer

p = KafkaProducer(bootstrap_servers='localhost:9092')

with open('dataset.json') as f:
  data = json.load(f)
  for x in data:
   p.send('sample', json.dumps(x, default=json_util.default).encode('utf-8'))
p.flush()
