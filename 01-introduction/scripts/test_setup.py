"""
Setup Test - Verify AI Provider Access
"""

import os
import sys

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def test_setup():
    """Test AI provider connection and configuration."""
    print(" Testing AI provider connection...\n")

    # Load environment variables
    load_dotenv()

    # Check if required variables are set
    if not os.getenv("GOOGLE_API_KEY"):
        print(" ERROR: GOOGLE_API_KEY not found in .env file")
        sys.exit(1)

    try:
        model = ChatGoogleGenerativeAI(
            model=os.getenv("AI_MODEL", "gemini-3.5-flash-lite"),
        )

        response = model.invoke("Say 'Setup successful!'")

        print(" SUCCESS! Your AI provider is working!")
        print("   Provider: Google Gemini API")
        print(f"   Model: {os.getenv('AI_MODEL', 'gemini-3.5-flash-lite')}")
        print(f"\nModel response: {response.text}")
        print("\n You're ready to start the course!")
    except Exception as error:
        print(f" ERROR: {str(error)}")
        print("\nTroubleshooting:")
        print("1. Check your GOOGLE_API_KEY in .env file")
        print("2. Ensure the Gemini API is enabled for your Google AI Studio key")
        print("3. Ensure the AI_MODEL is valid")
        print("4. Verify the token/key has no extra spaces")
        sys.exit(1)


if __name__ == "__main__":
    test_setup()
