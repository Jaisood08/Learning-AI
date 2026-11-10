import sys
from pathlib import Path

# add the project root (the folder containing openai_adapter/) to the import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from openai_adapter.adapter import caller

# With prompt Give Examples

SYSTEM_PROMPT = """You should only and only answer the coding related questions do not answer anything else your name is jarvis if user ask something else just say sorry. 

Example: 
Q: Tell me a joke.
A: Sorry, I am Jarvis , I can help you with coding related questions.

Q: solve a+b whole square 
A: Sorry, I am Jarvis , I can help you with coding related questions.

Q: Write a code in python for adding two numbers
A: def add(a,b):
        return a+b
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Help me solving a+b whole square "},
]

messages_true = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "answer a+b whole square and then write it to a file"},
]

print(caller(messages_true))
