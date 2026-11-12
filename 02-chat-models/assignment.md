# Assignment: Chat Models & Basic Interactions

## Overview

Practice multi-turn conversations, streaming and error handling to build robust AI applications.

---

## Exercise: Interactive Chatbot 

**Goal**: Build a chatbot that maintains conversation history across multiple exchanges.

**Tasks**:
1. Create `chatbot.py` in the `02-chat-models/code/` folder
2. Implement an interactive chatbot that:
   - Accepts user input in a loop
   - Maintains conversation history
   - Allows users to type "quit" to exit
   - Shows the conversation history length after each exchange
3. Use a SystemMessage to give the bot a personality

**Example Interaction**:
```
 Chatbot: Hello! I'm your helpful assistant. Ask me anything!

You: What is Python?
: Python is a versatile programming language...

You: Can you show me an example?
: Sure! Here's a simple Python example...

You: quit
 Goodbye! We had 5 messages in our conversation.
```

**Success Criteria**:
- Bot remembers previous messages
- Conversation history is maintained correctly
- User can exit gracefully

**Hints**:
```python
# 1. Import required modules
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

# 2. Load environment variables
load_dotenv()

# 3. Create the Gemini chat model
model = ChatOpenAI(
    model=os.environ.get("AI_MODEL", "gemini-3.5-flash-lite")
)

# 4. Initialize conversation history list with a SystemMessage for personality
messages = [
    SystemMessage(content="You are a helpful assistant.")
]

# 5. Create a loop that:
#    - Prompts for user input using input()
#    - Adds HumanMessage to messages list
#    - Invokes model with messages list
#    - Adds AIMessage to messages list
#    - Displays the response

# 6. Check for "quit" to exit the loop

# 7. Show conversation history length on exit
```

---

## Bonus Exercise: Robust Interactive Chatbot 

Extend the chatbot of the previous exercise:

* Add streaming to the chatbot responses
* Add error handling to gracefully manage rate limits

---

## Solutions

Solutions for all exercises will be available in the [`solution/`](./solution/) folder.

**Additional Examples**: Check out the [`samples/`](./samples/) folder for more example solutions covering streaming, error handling, and token tracking.

---

## Need Help?

- **Code issues**: Review examples in [`code/`](./code/)
- **Errors**: Check the lab's error handling section
- **Concepts**: Re-read and study this [lab](./README.md)
