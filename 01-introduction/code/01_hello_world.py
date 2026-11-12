"""
Lab 01 - Hello World with LangChain
This example demonstrates a basic LLM call using Google Gemini.
"""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print(" Hello LangChain!\n")

    # Create a chat model instance
    model = ChatOpenAI(
        model=os.getenv("AI_MODEL", "gemini-3.5-flash-lite"),
    )

    # Make your first AI call!
    response = model.invoke("What is LangChain in one sentence?")

    print(" AI Response:", response.text)
    print("\n Success! You just made your first LangChain call!")


if __name__ == "__main__":
    main()
