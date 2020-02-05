#! /usr/bin/env python 

from kafka import KafkaProducer
producer = kafkaProducer(bootstrap_servers='localhost:2181')
for i in range (1,100):
	producer.send('mytopic','hello world')


 
