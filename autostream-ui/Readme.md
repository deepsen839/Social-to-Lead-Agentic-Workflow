# AutoStream AI – Social-to-Lead Agent

## Features
- Intent classification (greeting / pricing / high-intent)
- RAG-based knowledge retrieval
- Stateful conversation (LangGraph)
- Lead capture tool execution
- FastAPI backend + React frontend

## Run Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

## Run Frontend
cd frontend
npm install
npm run dev

## Flow
1. Greeting
2. RAG answer
3. Intent shift
4. Lead collection
5. Tool execution