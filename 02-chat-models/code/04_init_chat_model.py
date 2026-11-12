"""
Provider-Agnostic Model Initialization
Run: python 02-chat-models/code/04_init_chat_model.py

This example demonstrates init_chat_model() with Google Gemini and shows how
to switch providers by changing the model identifier.
"""

import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

load_dotenv()


def google_gemini_example():
    """Demonstrate init_chat_model() with Google Gemini."""
    model_name = os.getenv("AI_MODEL", "gemini-3.5-flash-lite")
    model = init_chat_model(f"google_genai:{model_name}")

    response = model.invoke(
        [HumanMessage(content="What is LangChain in one sentence?")]
    )

    print(f"Using model: {model_name}")
    print("Response:", response.text)


def switching_providers_concept():
    """Show how init_chat_model() enables easy provider switching."""
    print("\nSwitch providers by changing the model identifier:\n")
    print('  # Google Gemini (course default)')
    print('  model = init_chat_model("google_genai:gemini-3.5-flash-lite")')
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
    google_gemini_example()
    switching_providers_concept()


if __name__ == "__main__":
    main()
