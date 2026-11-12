"""
Token Usage Tracking Example
Run: python 02-chat-models/code/06_token_tracking.py
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()


def track_token_usage():
    model = ChatGoogleGenerativeAI(
        model=os.getenv("AI_MODEL", "gemini-3.5-flash-lite"),
    )

    print(" Token Usage Tracking Example\n")

    # Make a request
    response = model.invoke("Explain what Python is in 2 sentences.")

    # Extract token usage from metadata (usage_metadata in Python)
    usage = response.usage_metadata

    if usage:
        print("Token Breakdown:")
        print(f"  Prompt tokens:     {usage.get('input_tokens', 'N/A')}")
        print(f"  Completion tokens: {usage.get('output_tokens', 'N/A')}")
        print(f"  Total tokens:      {usage.get('total_tokens', 'N/A')}")
    else:
        print("️  Token usage information not available in response metadata.")

    print("\n Response:")
    print(response.text)


if __name__ == "__main__":
    track_token_usage()
