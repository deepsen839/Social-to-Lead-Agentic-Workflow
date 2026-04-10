import re
from agent.tool import mock_lead_capture


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def lead_node(state):
    user_input = state["user_input"]

    # Step 0: Start lead flow
    if not state.get("lead_started"):
        return {
            "lead_started": True,   # ✅ RETURN IT
            "response": "Great! Let's get you started 😊\n\nWhat's your name?"
        }

    # Step 1: Name
    if not state.get("name"):
        return {
            "lead_started": True,
            "name": user_input,
            "response": "Nice to meet you 😊\n\nWhat's your email?"
        }

    # Step 2: Email
    if not state.get("email"):
        if not is_valid_email(user_input):
            return {
                "lead_started": True,
                "response": "Please enter a valid email address."
            }

        return {
            "lead_started": True,
            "name": state["name"],
            "email": user_input,
            "response": "Which platform do you create content on? (YouTube, Instagram, etc.)"
        }

    # Step 3: Platform
    if not state.get("platform"):
        mock_lead_capture(
            state["name"],
            state["email"],
            user_input
        )

        return {
            "lead_started": True,
            "name": state["name"],
            "email": state["email"],
            "platform": user_input,
            "response": "🎉 Lead captured successfully! We'll reach out soon."
        }