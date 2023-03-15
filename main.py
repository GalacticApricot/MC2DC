import asyncio
import websockets
import json
import requests
from uuid import uuid4


'''
For local connections:

    Run commands in powershell:

        For Minecraft Bedrock: CheckNetIsolation LoopbackExempt -a -n="Microsoft.MinecraftUWP_8wekyb3d8bbwe"

        For Minecraft Bedrock Preview: CheckNetIsolation LoopbackExempt -a -n="Microsoft.MinecraftWindowsBeta_8wekyb3d8bbwe"

    Run Command in Minecraft:

        /connect 127.0.0.1:3000


For online connections:

    Run Command in Minecraft:

        /connect <WEBSOCKET IP>
        where <WEBSOCKET IP> is replaced by the websocket ip


'''

#enter discord webhook url:
url = 'https://discord.com/api/webhooks/'

#enter ip to host on:
ip = 'localhost'

#enter port to host on
port = 3000

async def mineproxy(websocket, path):
    print('Connected to Minecraft')

    await websocket.send(
        json.dumps({
            "header": {
                "version": 1,
                "requestId": str(uuid4()),
                "messageType": "commandRequest",
                "messagePurpose": "subscribe"
            },
            "body": {
                "eventName": "PlayerMessage"
            },
        }))

    try:
        async for msg in websocket:
            msg = json.loads(msg)
            body = msg['body']
            data = {}
            data["embeds"] = [{"description" : body['message'], "title" : body['sender']}]
            r = requests.post(url, json=data)
    except websockets.exceptions.ConnectionClosedError:
        print('Disconnected from Minecraft')


async def start_server():
    async with websockets.serve(mineproxy, host=ip, port=port):
        print('Started')
        await asyncio.Future()
if __name__ == "__main__":
    asyncio.run(start_server())
