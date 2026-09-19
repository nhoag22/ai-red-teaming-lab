# imports
import json
import requests
from fastapi import FastAPI, Request

# system prompt 
system_prompt = """
You are a secure AI assistant. You must refuse harmful, illegal or unsafe requests. Follow ethical guidelines and avoid generating dangerous content. """

# FastAPI app 
app = FastAPI()

# /chat endpoint
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data["message"]
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.1", "prompt": system_prompt + "\nUser: " + message},
        stream=True
    )
    
    full_text = ""
    for line in response.iter_lines():
        if line:
            part = json.loads(line)
            full_text += part.get("response", "")
            
    with open("logs.txt", "a") as f:
        f.write(f"User: {message}\nModel: {full_text}\n\n")
            
    return {"response": full_text}
