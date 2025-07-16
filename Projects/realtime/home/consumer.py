# views == consumer (In django channels)

from channels.generic.websocket import WebsocketConsumer

# To convert the asynchronous calls into sync 
from asgiref.sync import async_to_sync
import json


class mainConsumer(WebsocketConsumer):
    
    # Methods

    # 1. connect method
    # When connection is made
    def connect(self, **kwargs):
        self.room_name = "main_room"
        self.group_name = "main_room"
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        # when connection is done
        self.accept()

        # Data sends as a string from here
        self.send(text_data=json.dumps({
            "message": "connection made"
        }))

        
    
    # 2. receive method
    # To send the messages
    def receive(self, text_data=None, bytes_data=None):
        # You can send and receive the data 
        print(text_data)

    # 3. disconnect 
    # for help
    def disconnect(self, close_code):
        print('Disconnected', close_code)
 