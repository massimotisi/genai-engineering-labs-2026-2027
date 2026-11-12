"""
Provider-Agnostic Model Initialization
Run: python 02-chat-models/code/04_init_chat_model.py

This example demonstrates init_chat_model() with Gemini's OpenAI-compatible API.
"""

import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

load_dotenv()


def gemini_example():
    """Demonstrate init_chat_model() with Gemini's OpenAI-compatible API."""
    model_name = os.getenv("AI_MODEL", "gemini-3.5-flash-lite")
    model = init_chat_model(
        f"openai:{model_name}",
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    response = model.invoke(
        [HumanMessage(content="What is LangChain in one sentence?")]
    )

    print(f"Using model: {model_name}")
    print("Response:", response.text)


def switching_providers_concept():
    """Show how init_chat_model() enables provider switching."""
    print("\nSwitch providers by changing the model identifier and configuration:\n")
    print('  # Google Gemini via its OpenAI-compatible endpoint (course default)')
    print('  model = init_chat_model("openai:gemini-3.5-flash-lite", base_url=...)')
    print()
    print('  # OpenAI')
    print('  model = init_chat_model("openai:<model-name>")')
    print()
    print('  # Anthropic')
    print('  model = init_chat_model("anthropic:<model-name>")')
    print("\nThe invoke() interface stays the same across providers.")


def main():
    print("Provider-Agnostic Initialization with LangChain\n")
    print("=" * 60)
    gemini_example()
    switching_providers_concept()


if __name__ == "__main__":
    main()
