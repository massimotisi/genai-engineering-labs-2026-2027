"""
Lab 01 - Message Types in LangChain
This example demonstrates how to use different message types (SystemMessage, HumanMessage).
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def main():
    print(" Understanding Message Types\n")

    model = ChatGoogleGenerativeAI(
        model=os.getenv("AI_MODEL", "gemini-3.5-flash-lite"),
    )

    # Using structured messages for better control
    messages = [
        SystemMessage(
            content="You are a helpful AI assistant who explains things to a 10-year-old."
        ),
        HumanMessage(content="Explain quantum computing."),
    ]

    response = model.invoke(messages)

    print(" AI Response:\n")
    print(response.text)
    print("\n Notice how the SystemMessage influenced the response style!")


if __name__ == "__main__":
    main()
