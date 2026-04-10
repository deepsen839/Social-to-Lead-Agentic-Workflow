from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.intent import detect_intent
from agent.rag import rag_node
from agent.lead import lead_node
from agent.greeting import greeting_node

def router(state):

    # ✅ HIGHEST PRIORITY → STAY IN LEAD FLOW
    if state.get("lead_started"):
        return "lead"

    intent = state["intent"]

    if intent == "greeting":
        return "greeting"

    if intent == "high_intent":
        return "lead"

    return "rag"

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("intent", detect_intent)
    graph.add_node("greeting", greeting_node)
    graph.add_node("rag", rag_node)
    graph.add_node("lead", lead_node)

    graph.set_entry_point("intent")

    graph.add_conditional_edges(
        "intent",
        router,
        {
            "greeting": "greeting",
            "rag": "rag",
            "lead": "lead"
        }
    )

    graph.set_finish_point("greeting")
    graph.set_finish_point("rag")
    graph.set_finish_point("lead")

    return graph.compile()