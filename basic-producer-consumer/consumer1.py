#! /usr/bin/env python 

from kafka import KafkaConsumer
consumer = KafkaConsumer('mytopic', bootstrap_servers='35.239.34.125:9092')
for msg in consumer:
 print (msg)
