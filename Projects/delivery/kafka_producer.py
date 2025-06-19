
# Kafka - 1
# Real - time data of latitude and longitude

from confluent_kafka import Producer
import json
import os
import time


# Broker url of kafka
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(**conf)

# Some random latitude and longitude for project
# latitude and longitude of delivery boy
starting_latitude = 19.0760  
starting_longitude = 72.8777
end_latitude = 18.5204
end_longitude = 73.8567

# number of steps of delivery boy to walk / speed of delivery boy
# You can increase the num_steps... so it will increase the speed 
num_steps = 1000
step_size_lat = (end_latitude - starting_latitude) / num_steps
step_size_long = (end_longitude - starting_longitude) / num_steps
current_steps = 0


def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed : {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")



topic = "location_updates"
# To geneate lattitude and longitude
while True:
    latitude = starting_latitude + step_size_lat * current_steps
    longitude = starting_longitude + step_size_long * current_steps

    data = {
        "latitude": latitude, 
        "longitude": longitude
    }

    print(data)

    # It dumps the data into topic
    # callback function for checking data is pushed in
    producer.produce(topic, json.dumps(data).encode('utf-8'), callback = delivery_report)

    # flush / delete the data or u can save it also 
    # Only latest data will be shown
    producer.flush()

    current_steps += 1
    if current_steps > num_steps:
        current_steps = 0

    time.sleep(2)