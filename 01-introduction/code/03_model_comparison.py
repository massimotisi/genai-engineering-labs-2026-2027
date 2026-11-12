"""
Lab 01 - Model Comparison in LangChain
This example shows how to compare different AI models.
"""

import time

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def compare_models():
    print(" Comparing AI Models\n")

    prompt = "Explain recursion in programming in one sentence."
    models = ["gemma-4-26b-a4b-it", "gemini-3.5-flash-lite"]

    for model_name in models:
        print(f"\n Testing: {model_name}")
        print("─" * 50)

        model = ChatOpenAI(
            model=model_name,
        )

        start_time = time.time()
        response = model.invoke(prompt)
        duration = (time.time() - start_time) * 1000

        print(f"Response: {response.text}")
        print(f"️  Time: {duration:.0f}ms")

    print("\n Comparison complete!")
    print("\n Key Observations:")
    print("   - Compare the models' responses and measured latency")
    print("   - Choose based on your application's needs")


if __name__ == "__main__":
    compare_models()
