# Assignment: Introduction to LangChain

## Overview

Now that you've learned the basics of LangChain, it's time to practice! These exercises will help reinforce what you've learned about models, messages, and making your first LLM calls.

---

## Exercise: Experiment with System Prompts 

**Goal**: Learn how system messages affect AI behavior.

**Tasks**:
1. Create a file called `personality_test.py`
2. Test the same question with three different system prompts:
   - A pirate personality
   - A professional business analyst
   - A friendly teacher for kids
3. Display all three responses side-by-side

**Example System Prompts**:
- Pirate: `"You are a pirate. Answer all questions in pirate speak with 'Arrr!' and nautical terms."`
- Analyst: `"You are a professional business analyst. Give precise, data-driven answers."`
- Teacher: `"You are a friendly teacher explaining concepts to 8-year-old children."`

**Question to Test**: "What is artificial intelligence?"

**Success Criteria**:
- Same question gets three very different response styles
- You understand how SystemMessage shapes the AI's personality

**Hints**:
```python
# 1. Import required modules
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

# 2. Load environment variables
load_dotenv()

# 3. Create the ChatGoogleGenerativeAI model (reuse for all personalities)

# 4. Define a list of personalities with name and system prompt

# 5. Define the question to test

# 6. Loop through each personality:
#    - Create messages list with SystemMessage and HumanMessage
#    - Invoke the model with the messages
#    - Display the response with personality name
```

---

## Bonus Exercise: Model Performance Comparison 

**Goal**: Compare multiple models on the same task.

**Tasks**:
1. Create a file called `model_performance.py`
2. Test at least 2 Google models:
   - `gemma-4-26b-a4b-it`
   - `gemini-3.5-flash-lite`
3. For each model, measure:
   - Response time
   - Response length (character count)
   - Response quality (your subjective assessment)
4. Create a simple table showing the results

**Test Question**: "Explain the difference between machine learning and deep learning."

**Expected Output**:
```
 Model Performance Comparison
─────────────────────────────────────────────
Model          | Time    | Length | Quality
─────────────────────────────────────────────
gemini-3.5-flash-lite | 567ms   | 234ch  |
gemma-4-26b-a4b-it    | 1234ms  | 456ch  |
```

**Success Criteria**:
- Script compares at least 2 models
- Results are displayed in a clear format
- You can explain which model you'd choose for different use cases

**Hints**:
```python
# 1. Import required modules
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 2. Load environment variables
load_dotenv()

# 3. Define question and models list
question = "Explain the difference between machine learning and deep learning."

models = [
    {"name": "gemma-4-26b-a4b-it", "description": "Gemma 4 instruction-tuned"},
    {"name": "gemini-3.5-flash-lite", "description": "Fast and efficient"},
]

# 4. Create a function to test each model:
#    - Accept model_name as parameter
#    - Create ChatGoogleGenerativeAI instance with that model
#    - Measure start time with time.time()
#    - Invoke the model with the question
#    - Measure end time and calculate duration
#    - Return a dict with name, time, length, and response

# 5. Loop through models list:
#    - Call test_model() for each model
#    - Display results in a formatted table
#    - Use .ljust() for consistent column widths
```

---

## Solutions

Solutions for all challenges will be available in the [`solution/`](./solution/) folder. Try to complete the challenges on your own first before looking at the solutions!

**Additional Examples**: Check out the [`samples/`](./samples/) folder for more example solutions that demonstrate other useful concepts

---

## Need Help?

- **Stuck on code**: Review the examples in [`code/`](./code/)
- **Concepts unclear**: Re-read and study this [lab](./README.md)
