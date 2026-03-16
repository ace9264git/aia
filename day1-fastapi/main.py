from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MessageRequest(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "Hello, all in ai"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/echo")
def echo_message(payload: MessageRequest):
    return {"received": payload.text}