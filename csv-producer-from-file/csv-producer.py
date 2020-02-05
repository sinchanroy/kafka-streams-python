#! /usr/bin/env python 

import re
import argparse
from collections import OrderedDict
import csv 
import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

def input():
    myparser = argparse.ArgumentParser("Taking Inputs")
    myparser.add_argument('--input', action='store', type=argparse.FileType('r'), required=True)
    args = myparser.parse_args()

    return args.input

def run():
    file = input()

    producer = KafkaProducer(bootstrap_servers=['127.0.0.1'])

    keys = ["id","name","branch","message"]
 
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count = line_count + 1
        dic = OrderedDict(zip(keys, row))
        json_data = json.dumps(dic).encode('ascii')
        producer.send('mytopic', {'key' : 'value'}) 
        
    
    def on_send_success(record_metadata):
     print(record_metadata.topic)
     print(record_metadata.partition)
     print(record_metadata.offset)

    producer.flush()

    producer = KafkaProducer(retries=5)


if __name__ == '__main__':
    run()

