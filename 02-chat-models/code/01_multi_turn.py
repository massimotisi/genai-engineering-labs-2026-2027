"""
Multi-Turn Conversation
Run: python 02-chat-models/code/01_multi_turn.py
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()


def main():
    print(" Multi-Turn Conversation Example\n")

    # Create a chat model instance
    model = ChatGoogleGenerativeAI(
        model=os.getenv("AI_MODEL", "gemini-3.5-flash-lite"),
    )

    # Start with system message and first question
    messages = [
        SystemMessage(
            content="You are a helpful coding tutor who gives clear, concise explanations."
        ),
        HumanMessage(content="What is Python?"),
    ]

    print(" User: What is Python?")

    # First exchange
    response1 = model.invoke(messages)
    print(f"\n AI: {response1.text}")
    messages.append(AIMessage(content=response1.text))

    # Second exchange - AI remembers the context
    print("\n User: Can you show me a simple example?")
    messages.append(HumanMessage(content="Can you show me a simple example?"))

    response2 = model.invoke(messages)
    messages.append(AIMessage(content=response2.text))
    print(f"\n AI: {response2.text}")

    # Third exchange - AI still remembers everything
    print("\n User: What are the benefits compared to other languages?")
    messages.append(
        HumanMessage(content="What are the benefits compared to other languages?")
    )

    # the 3rd AI response is not added to conversation history since it is the last in the conversation
    response3 = model.invoke(messages)
    print(f"\n AI: {response3.text}")

    print("\n\n Notice how the AI maintains context throughout the conversation!")
    print(
        f" Total messages in history: {len(messages)} messages, that include 1 system message, 3 Human messages and 2 AI responses"
    )


if __name__ == "__main__":
    main()
