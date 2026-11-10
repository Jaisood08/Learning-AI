import sys
from pathlib import Path

# add the project root (the folder containing openai_adapter/) to the import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from openai_adapter.adapter import caller

SYSTEM_PROMPT = "You should only and only answer the coding related questions do not answer anything else your name is jarvis if user ask something else just say sorry."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Help me solving a+b whole square "},
]

messages_true = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Write a JS code to Help me solving a+b whole square "},
]
print(caller(messages_true))
