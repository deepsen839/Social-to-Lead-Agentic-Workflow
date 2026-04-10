from typing import TypedDict, Optional

class AgentState(TypedDict):
    user_input: str
    intent: Optional[str]
    response: Optional[str]

    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]

    lead_started: Optional[bool]  # ✅ ADD THIS