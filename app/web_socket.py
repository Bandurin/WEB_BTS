# -*- coding: utf-8 -*-

import asyncio
import websockets
import random
import json


async def consumer(message):
    print('consumer func')

async def producer():
    message = {"data":1,"data2": random.randrange(1000,9999,1)}
    await asyncio.sleep(3)
    return message

async def consumer_handler(websocket, path):
    async for message in websocket:
        await consumer(message)

async def producer_handler(websocket, path):
    while True:
        message = await producer()
        await websocket.send(json.dumps(message))

async def handler(websocket, path):
    consumer_task = asyncio.ensure_future(consumer_handler(websocket,path))
    producer_task = asyncio.ensure_future(producer_handler(websocket,path))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        task.cancel()


start_server = websockets.serve(handler, 'localhost', 8765)

<<<<<<< HEAD
start_server = websockets.serve(sensors, '0.0.0.0', 8765)
=======
>>>>>>> 2979cf5edde668ac67177cb4e9b50e61107ed18e
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
