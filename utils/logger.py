import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

# logs directory is at project_root/logs
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
LOG_FILE = os.path.join(LOG_DIR, "agent_logs.jsonl")

# Make sure the directory exists
os.makedirs(LOG_DIR, exist_ok=True)


def log_interaction(
    user_message: str,
    intent: str,
    response: str,
    meta: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Append a single interaction to logs/agent_logs.jsonl as one JSON line.

    Fields:
    - timestamp: ISO UTC time
    - user_message
    - intent
    - response
    - meta: extra info (tools used, state, etc.)
    """
    if meta is None:
        meta = {}

    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_message": user_message,
        "intent": intent,
        "response": response,
        "meta": meta,
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
