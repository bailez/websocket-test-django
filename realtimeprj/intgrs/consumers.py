from channels.generic.websocket import WebsocketConsumer, AsyncConsumer
import json
from random import randint
from time import sleep
import asyncio

class WSConsumer(AsyncConsumer):

    async def websocket_connect(self, _):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, text_data):
        for i in range(1000):
            await asyncio.sleep(1)
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({'message' : randint(1,100)})
            })