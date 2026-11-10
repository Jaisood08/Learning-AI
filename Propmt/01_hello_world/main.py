import sys
from pathlib import Path

# add the project root (the folder containing openai_adapter/) to the import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from openai_adapter.adapter import caller

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain to me how AI works"},
]

print(caller(messages))
