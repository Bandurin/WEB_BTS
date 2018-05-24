# -*- coding: utf-8 -*-

import asyncio
import websockets
import random
import time

async def sensors(websocket, path):
    #name = await websocket.recv()
    #print("< {}".format(name))
    while 1:
        greeting = str({"Hello {}!" :random.randrange(1,10000,1)})
        await websocket.send(greeting)
        time.sleep(1)
        print("> {}".format(greeting))


start_server = websockets.serve(sensors, '0.0.0.0', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
