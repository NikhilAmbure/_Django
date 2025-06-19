# Kafka - 1

from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaException, KafkaError
import json
import os
from home.models import LocationUpdate


class Command(BaseCommand):
    help = "Run kafka consumer to listen for location update"

    # Overriding handle
    def handle(self, *args, **options):

        conf = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'location_group', # group
            'auto.offset.reset': 'earliest' # A Unique no. in Partition
            }
        
        consumer = Consumer(conf)
        # Mention the topic-name from producer here
        consumer.subscribe(['location_updates'])

        # read the msg
        try:
            while True:
                msg = consumer.poll(timeout = 1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(msg.error())
                        break
                
                data = json.loads(msg.value().decode('utf-8'))

                LocationUpdate.objects.create(
                    latitude = data['latitude'],
                    longitude = data['longitude']
                )
                print(f"Received and saved {data}")

        except KeyboardInterrupt:
            pass
        finally: 
            consumer.close()

# python manage.py kafka_consumer -> starts the consumer...