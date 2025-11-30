from typing import List, Tuple

from agents.orchestrator import handle_message
from utils.state import ConversationState


# (message, expected_intent)
TEST_CASES: List[Tuple[str, str]] = [
    ("Where is my order 1001?", "ORDER"),
    ("Track order 1002", "ORDER"),
    ("Has my order been shipped?", "ORDER"),
    ("What is your return policy?", "FAQ"),
    ("How long does express shipping take?", "FAQ"),
    ("Do you ship internationally?", "FAQ"),
    ("Tell me a joke", "OTHER"),
    ("What is the weather today?", "OTHER"),
]


def main():
    total = len(TEST_CASES)
    correct = 0

    print("=== Intent Routing Evaluation ===\n")

    for message, expected in TEST_CASES:
        state = ConversationState()
        intent, response = handle_message(message, state)

        ok = intent == expected
        if ok:
            correct += 1

        print(f"User: {message}")
        print(f"Expected intent: {expected} | Predicted: {intent} | {'YES' if ok else 'NO'}")
        print("-" * 60)

    accuracy = correct / total * 100
    print(f"\nTotal: {total}, Correct: {correct}, Accuracy: {accuracy:.1f}%")

    print("\nNote: This tests routing only, not answer quality.")


if __name__ == "__main__":
    main()
