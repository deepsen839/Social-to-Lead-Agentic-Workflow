# 🚀 AutoStream – Social-to-Lead Agentic Workflow

> An AI-powered conversational agent that converts user interactions into qualified business leads using a structured agentic workflow.

---

# 🌟 Demo Overview

AutoStream simulates a SaaS assistant that:
- Understands user intent
- Answers product queries using RAG
- Detects high-intent users
- Captures leads (Name → Email → Platform)
- Executes backend actions

---

# 🧠 Architecture Diagram

```
User Input
    ↓
Intent Detection
    ↓
   Router
 ┌────┼───────────┐
 ↓    ↓           ↓
Greeting  RAG   Lead Capture
                  ↓
          mock_lead_capture()
```

---

# 🏗️ Architecture Explanation

This project uses **LangGraph** to implement a stateful, multi-step conversational agent.

LangGraph was chosen over traditional LangChain chains or AutoGen because it provides **explicit control over node transitions and branching logic**, which is critical for workflows like lead capture.

The system is composed of four key nodes:
- **Intent Node** → Classifies user input
- **RAG Node** → Retrieves pricing/features from knowledge base
- **Greeting Node** → Handles casual interactions
- **Lead Node** → Collects user details step-by-step

A **router function** dynamically directs execution based on intent and state.

## 🧩 State Management

State is maintained using a shared `AgentState` object stored in session memory.

### Key fields:
- `name`
- `email`
- `platform`
- `lead_started`

The `lead_started` flag ensures that once a user enters the lead flow, the agent remains in that flow and does not revert to other nodes.

This guarantees:
- Controlled execution
- No premature tool calls
- Consistent multi-turn interaction

---

# 📱 WhatsApp Integration (Webhooks)

This agent can be deployed on WhatsApp using the **WhatsApp Business API** via providers like **Meta or Twilio**.

### Flow:
1. User sends message on WhatsApp
2. WhatsApp forwards it to a backend webhook (`/webhook`)
3. Backend processes it using LangGraph (`graph.invoke(state)`)
4. Response is sent back via WhatsApp API

### Session Handling:
- Use **phone number as session_id**
- Maintains conversation continuity

---

# 🛠️ How to Run Locally

## 🔹 Backend

```bash
cd backend
python -m venv myenv
source myenv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

👉 Runs at: http://127.0.0.1:8000

---

## 🔹 Frontend

```bash
cd autostream-ui
npm install
npm run dev
```

👉 Runs at: http://localhost:5173

---

## 🔹 Docker (Recommended)

```bash
docker-compose up --build
```

👉 Frontend: http://localhost:5173  
👉 Backend: http://localhost:8000  

---

# 🧪 Example Conversation

```
User: Hi
→ Greeting

User: Tell me about pricing
→ RAG response

User: I want to try Pro plan
→ Ask name

User: Deep Sen
→ Ask email

User: deep@gmail.com
→ Ask platform

User: YouTube
→ Lead captured 🎉
```

---

# ✅ Features

- ✅ Intent classification (greeting / pricing / high-intent)
- ✅ RAG-based knowledge retrieval
- ✅ Stateful multi-turn conversation
- ✅ Lead capture workflow
- ✅ Tool execution control
- ✅ React frontend UI
- ✅ Dockerized deployment

---

# 🧠 Tech Stack

| Layer | Tech |
|------|-----|
| Backend | FastAPI, LangGraph |
| LLM | Groq (LLaMA 3) |
| Frontend | React (Vite) |
| Deployment | Docker |

---

# 🔐 Environment Variables

Create `.env` in backend:

```
GROQ_API_KEY=your_api_key
```

---

# 🎯 Design Decisions

- Used **hybrid intent detection (rules + LLM)** for reliability
- Used **state lock (`lead_started`)** to prevent flow break
- Used **RAG instead of hardcoding** for scalability
- Ensured **tool executes only after full data collection**

---

# 🏁 Conclusion

This project demonstrates how **agentic AI systems** can go beyond chatbots to drive **real business outcomes (lead generation)** using structured workflows and state management.

---

# 💡 Interview Pitch

> “I built a stateful AI agent using LangGraph that combines intent classification, retrieval, and controlled execution to convert conversations into leads.”
