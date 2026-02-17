from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend Running Successfully"}

@app.websocket("/ws/audio")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")

    try:
        while True:
            data = await websocket.receive_bytes()
            print(f"Received {len(data)} bytes")
            await websocket.send_bytes(data)  # Echo back
    except:
        print("Client disconnected")
