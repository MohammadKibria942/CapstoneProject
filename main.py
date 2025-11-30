from agents.orchestrator import handle_message
from utils.state import ConversationState
from utils.logger import log_interaction

def main():
    print("=== E-commerce Customer Service Agent ===")
    print("Type 'exit' to quit.\n")

    state = ConversationState()  # <-- NEW

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Agent: Goodbye! 👋")
            break

        if not user_input:
            continue

        intent, response = handle_message(user_input, state)
        print(f"[Intent detected: {intent}]")
        print(f"Agent: {response}\n")

        # --- logging for LLMOps ---
        meta = {
            "pending_intent": state.pending_intent,
            "last_intent": state.last_intent,
        }
        log_interaction(user_input, intent, response, meta)


if __name__ == "__main__":
    main()
