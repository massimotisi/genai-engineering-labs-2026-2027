"""
Setup Test - Verify AI Provider Access
"""

import os
import sys

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def test_setup():
    """Test AI provider connection and configuration."""
    print(" Testing AI provider connection...\n")

    # Load environment variables
    load_dotenv()

    # Check if required variables are set
    if not os.getenv("OPENAI_API_KEY"):
        print(" ERROR: OPENAI_API_KEY not found in .env file")
        sys.exit(1)

    if not os.getenv("OPENAI_BASE_URL"):
        print(" ERROR: OPENAI_BASE_URL not found in .env file")
        sys.exit(1)

    try:
        model = ChatOpenAI(
            model=os.getenv("AI_MODEL", "gemini-3.5-flash-lite"),
            base_url=os.getenv("OPENAI_BASE_URL"),
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        response = model.invoke("Say 'Setup successful!'")

        print(" SUCCESS! Your AI provider is working!")
        print("   Provider: Google Gemini API (OpenAI-compatible endpoint)")
        print(f"   Model: {os.getenv('AI_MODEL', 'gemini-3.5-flash-lite')}")
        print(f"\nModel response: {response.text}")
        print("\n You're ready to start the course!")
    except Exception as error:
        print(f" ERROR: {str(error)}")
        print("\nTroubleshooting:")
        print("1. Check your Gemini API key in OPENAI_API_KEY in .env file")
        print("2. Check OPENAI_BASE_URL in .env file")
        print("3. Ensure the Gemini API is enabled for your Google AI Studio key")
        print("4. Ensure the AI_MODEL is valid")
        print("5. Verify the token/key has no extra spaces")
        sys.exit(1)


if __name__ == "__main__":
    test_setup()
