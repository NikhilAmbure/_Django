# Using kafka

from django.core.management.base import BaseCommand
from confluent_kafka import Consumer
import os
import json
from collections import defaultdict
from django.db import transaction
from likes.models import Posts

class Command(BaseCommand):
    help = 'Run Kafka Consumer'

    # Main Logic
    # updating in database
    def processBatch(self, like_batch):
        with transaction.atomic():
            for post_id, like_count in like_batch.items():
                post = Posts.objects.get(id=post_id) 
                post.like += like_count
                post.save()
        # print(like_batch)
    
    def handle(self, *args, **options):
        print("** KAFKA CONSUMER STARTED **")
        like_batch = defaultdict(int)
        conf = {
            'bootstrap.servers': os.getenv('KAFKA_BROKER_URL', 'localhost:9092'),
            'group.id': 'location_group',
            'auto.offset.reset': 'earliest'
        }

        consumer = Consumer(conf)
        # Topic
        consumer.subscribe(['like_topic'])
        total_messages = 0

        try: 
            while True:
                print("** listening for msgs **")
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(msg.error())
                    continue

                # Logic
                data = json.loads(msg.value().decode('utf-8'))
                post_id = data['post_id']
                like_batch[post_id] += 1
                total_messages += 1
                print(f"like_batch = {like_batch}, total_messages =  {total_messages}")


                if total_messages >= 10:
                    self.processBatch(like_batch)
                    like_batch.clear()
                    total_messages = 0

        except KeyboardInterrupt:
            pass
        finally: 
            consumer.close()
