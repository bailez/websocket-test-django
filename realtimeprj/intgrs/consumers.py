from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep

class WSConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
    
    def receive(self, text_data):
        for i in range(1000):
            self.send(json.dumps({'message' : randint(1,100)}))
            sleep(1)