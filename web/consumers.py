from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class DeviceConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'stream'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("stream", self.channel_name)

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        self.send(text_data=json.dumps({
            'message': message
        }))

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'stream_message',
                'message': message
            }
        )

    def stream_message(self, event):
        message = event['message']

        # Send message to websocket
        self.send(text_data=json.dumps({'message': message}))

