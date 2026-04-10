from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import build_graph
from fastapi.middleware.cors import CORSMiddleware    
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
graph = build_graph()

# Session memory (retains 5–6 turns)
sessions = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
def chat(req: ChatRequest):

    # ✅ FIXED STATE (ADD lead_started)
    state = sessions.get(req.session_id, {
        "name": None,
        "email": None,
        "platform": None,
        "lead_started": False   # ✅ THIS WAS MISSING
    })

    state["user_input"] = req.message

    result = graph.invoke(state)

    state.update(result)
    sessions[req.session_id] = state

    return {"response": result["response"]}