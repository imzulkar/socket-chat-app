import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        return super().connect()

    # def close(self, code=None):
    #     return super().close(code)
    def disconnect(self, code=None):
        # return super().disconnect(code)
        pass
       
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.send(text_data=json.dumps({"message": message}))
        
    