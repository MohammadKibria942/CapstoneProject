from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.orchestrator import handle_message
from utils.state import ConversationState

app = FastAPI()

# Allow browser to call our API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store each user's session state (simple in-memory storage)
SESSION_STATE = ConversationState()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    intent: str
    response: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    user_message = request.message
    intent, response = handle_message(user_message, SESSION_STATE)
    return ChatResponse(intent=intent, response=response)
