import json
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

VALID_INTENTS = ["greeting", "pricing", "high_intent"]

import json
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

VALID_INTENTS = ["greeting", "pricing", "high_intent"]


def detect_intent(state):
    text = state["user_input"].lower().strip()

    # ✅ 1. HIGH INTENT (STRONG SIGNALS FIRST)
    if any(x in text for x in [
        "i want to try",
        "i want try",
        "i want to buy",
        "subscribe",
        "sign up",
        "get started",
        "start now",
        "take plan",
        "choose plan"
    ]):
        return {"intent": "high_intent"}

    # ✅ 2. PLAN-BASED HIGH INTENT
    if any(x in text for x in ["basic plan", "pro plan"]):
        if any(y in text for y in ["want", "take", "choose", "try"]):
            return {"intent": "high_intent"}

    # ✅ 3. GREETING
    if any(x in text for x in ["hi", "hello", "hey"]):
        return {"intent": "greeting"}

    # ✅ 4. LLM FALLBACK (NOW THIS WILL RUN)
    prompt = f"""
You are a strict intent classifier.

Classify the user message into EXACTLY one label:

greeting
pricing
high_intent

STRICT RULES:
- Return ONLY valid JSON
- No explanation

FORMAT:
{{"intent": "pricing"}}

User message: "{text}"
"""

    try:
        response = llm.invoke(prompt).content.strip()

        start = response.find("{")
        end = response.rfind("}") + 1

        if start == -1 or end == -1:
            raise ValueError("No JSON found")

        json_str = response[start:end]
        result = json.loads(json_str)

        intent = result.get("intent", "pricing")

        if intent not in VALID_INTENTS:
            intent = "pricing"

    except Exception:
        intent = "pricing"

    return {"intent": intent}