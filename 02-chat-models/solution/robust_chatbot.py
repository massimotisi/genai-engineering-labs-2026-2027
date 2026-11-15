"""
Bonus Solution: Robust Interactive Chatbot
Run: python 02-chat-models/solution/robust_chatbot.py
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from openai import RateLimitError

load_dotenv()

model = ChatOpenAI(
    model=os.environ.get("AI_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

messages = [
    SystemMessage(
        content="You are a friendly and helpful AI assistant. Be conversational and warm in your responses."
    ),
]


def chat():
    """Stream chatbot replies and handle rate limits without losing chat history."""
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n\n Goodbye! We had {len(messages)} messages in our conversation.")
            break

        if user_input.lower() in ("quit", "exit"):
            print(f"\n Goodbye! We had {len(messages)} messages in our conversation.")
            break

        if not user_input:
            continue

        user_message = HumanMessage(content=user_input)
        response_parts = []

        print("\n Chatbot: ", end="", flush=True)
        try:
            for chunk in model.stream([*messages, user_message]):
                response_parts.append(chunk.text)
                print(chunk.text, end="", flush=True)
        except RateLimitError:
            print("\n Rate limit reached. Please wait a moment, then try again.")
            continue
        except Exception as error:
            print(f"\n Error: {error}")
            continue

        if not response_parts:
            print("\n No response received. Please try again.")
            continue

        messages.extend([user_message, AIMessage(content="".join(response_parts))])
        print(f"\n Conversation length: {len(messages)} messages")

        if os.environ.get("CI") == "true":
            break


def main():
    print(" Chatbot: Hello! I'm your helpful assistant. Ask me anything!")
    print('(Type "quit" to exit)\n')
    chat()


if __name__ == "__main__":
    main()
