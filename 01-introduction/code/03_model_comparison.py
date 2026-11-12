"""
Lab 01 - Model Comparison in LangChain
This example shows how to compare different AI models.
"""

import time

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def compare_models():
    print(" Comparing AI Models\n")

    prompt = "Explain recursion in programming in one sentence."
    models = ["gemini-3.8-flash", "gemini-3.5-flash-lite"]

    for model_name in models:
        print(f"\n Testing: {model_name}")
        print("─" * 50)

        model = ChatGoogleGenerativeAI(
            model=model_name,
        )

        start_time = time.time()
        response = model.invoke(prompt)
        duration = (time.time() - start_time) * 1000

        print(f"Response: {response.text}")
        print(f"️  Time: {duration:.0f}ms")

    print("\n Comparison complete!")
    print("\n Key Observations:")
    print("   - gemini-3.8-flash is Google's higher-capability Flash model")
    print("   - gemini-3.5-flash-lite is optimized for speed and efficiency")
    print("   - Choose based on your needs: speed vs. capability")


if __name__ == "__main__":
    compare_models()
