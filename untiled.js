async def sedRequest(message):
    uri = "wss://ws.replika.ai/v17"

async with websockets.connect(uri) as websocket: #datos en formato json
data = env.generateData(message)
await websocket.send(json.dumps(data))