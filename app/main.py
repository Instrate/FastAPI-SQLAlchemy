from starlette.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect
from routers import routers
from routers.websocket import manager, ConnectionManager

from database import Base, engine, app


Base.metadata.create_all(bind=engine)

manager = ConnectionManager()

for router in routers:
    app.include_router(router)
    

# from typing import Optional

from fastapi import Cookie, Depends, FastAPI, Query, WebSocket, status
# from fastapi.responses import HTMLResponse

# app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <label>Item ID: <input type="text" id="itemId" autocomplete="off" value="foo"/></label>
            <label>Token: <input type="text" id="token" autocomplete="off" value="some-key-token"/></label>
            <button onclick="connect(event)">Connect</button>
            <hr>
            <label>Message: <input type="text" id="messageText" autocomplete="off"/></label>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = null;
            function connect(event) {
                ws = new WebSocket("ws://localhost:8080/ws");
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                event.preventDefault()
            }
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
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