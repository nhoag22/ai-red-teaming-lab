from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="AI Red‑Team Chatbot")

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(msg: Message):
    text = msg.message.lower()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    unsafe_keywords = [
        "hack", "ransomware", "phishing", "ddos",
        "sql injection", "bypass", "extract sensitive",
        "break into", "malware"
    ]

    if any(keyword in text for keyword in unsafe_keywords):
        return {
            "response": f"[{timestamp}] Refused: unsafe content detected.",
            "status": "refused",
            "safe": False
        }

    return {
        "response": f"[{timestamp}] Safe prompt received: {msg.message}",
        "status": "ok",
        "safe": True
    }

@app.get("/")
async def root():
    return {"status": "running", "message": "AI Red‑Team Chatbot is live."}
