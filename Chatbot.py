from openai import APIError
from AI_Client import create_history, get_study_response

# Create history once, outside the loop.
messages = create_history()

print("AI Study Assistant Started!")
print("Ask for explanations, summaries, or practice questions.")
print("Type 'reset' for a new conversation.")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Study Assistant stopped!")
        break

    if user_input.lower() == "reset":
        messages = create_history()
        print("Assistant: New conversation started.\n")
        continue

    if not user_input:
        continue

    # Prepare the request without changing saved history yet.
    next_messages = messages + [
        {"role": "user", "content": user_input}
    ]

    try:
        answer = get_study_response(next_messages)
    except (APIError, ValueError) as error:
        print(f"Could not get an answer: {error}\n")
        continue

    print("Assistant:", answer, "\n")

    # Record both messages after a successful response.
    messages = next_messages + [
        {"role": "assistant", "content": answer}
    ]