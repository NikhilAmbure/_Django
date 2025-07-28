# views == consumer

from channels.generic.websocket import WebsocketConsumer
import json
from .models import Pizza, Order
from asgiref.sync import async_to_sync, sync_to_async


class OrderProgress(WebsocketConsumer):

    def connect(self):
        # It's like passing the order_id to def index(req, order_id): (In consumer)
        # order_id variable
        self.room_name = self.scope['url_route']['kwargs']['order_id']
        self.room_group_name = f'order_{self.room_name}' #Order id generated
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # We send the data from here
        order = Order.give_order_details(self.room_name)

        self.accept()
        self.send(text_data=json.dumps({
            "payload": order
        }))
        

        def order_status(self, event):
            # print(event)
            data = json.loads(event['value'])
            # print(data)

            # Now sending data to frontend
            self.send(text_data=json.dumps({
                'payload': data
            }))


    def receive(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self, close_code):
        pass