from typing import List, Optional

from fastapi.params import Query
from fastapi.param_functions import Depends
from fastapi import APIRouter
from fastapi.websockets import WebSocket
from starlette.websockets import WebSocketDisconnect
from database.session import SessionLocal, get_db

websocket_router = APIRouter(
    prefix='/ws',
    #dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_json(message)

manager:ConnectionManager = None

@websocket_router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket
):
    print('\nwe\'re in websocket mode\n')
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            print(data)
            await websocket.send_json({'response': f"Message text was: {data}"})
    except WebSocketDisconnect:
        websocket.close()
