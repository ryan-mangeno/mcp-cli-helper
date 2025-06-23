from fastapi import FastAPI, Request
from mcp_server.handlers import handle_message

app = FastAPI()

@app.post("/message")
async def message_endpoint(req: Request):
    msg = await req.json()
    return handle_message(msg)
