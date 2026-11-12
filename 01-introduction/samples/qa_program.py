"""
Lab 01 - Interactive Q&A Program
A simple interactive program that allows you to ask questions to an LLM.
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Create a Gemini chat model instance
model = ChatGoogleGenerativeAI(
    model=os.environ.get("AI_MODEL", "gemini-3.5-flash-lite")
)


def main():
    """Main function to run the interactive Q&A program."""
    print("Welcome to the Q&A Program!")
    print("Type 'quit' to exit.\n")

    while True:
        # Get user input
        question = input("You: ").strip()

        # Check for exit command
        if question.lower() == "quit":
            print("Goodbye!")
            break

        # Skip empty questions
        if not question:
            continue

        # Get response from the model
        response = model.invoke(question)
        print(f"AI: {response.text}\n")


if __name__ == "__main__":
    main()
