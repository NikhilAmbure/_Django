# Producer logic

from confluent_kafka import Producer
import json
import os


conf = {
    'bootstrap.servers': os.getenv('KAFKA_BROKER_URL', 'localhost:9092'),
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed : {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")



def SendLikeEvent(post_id):
    producer.produce('like_topic', key=str(post_id), value=json.dumps({
        "post_id": post_id
    }), callback=delivery_report)
    print("SENT TO KAFKA")
    producer.flush()