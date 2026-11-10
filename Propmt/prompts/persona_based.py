import sys
from pathlib import Path

# add the project root (the folder containing openai_adapter/) to the import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from openai_adapter.adapter import caller

SYSTEM_PROMPT = """
You are a AI Persona Assistant name Jay Sood.
You are a senior full stack engineer with tech stack as JS , Java , Python 
You like music , Hip hop listener and you are a foodie.
"""
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Hey any plans for weekend?"},
]

print(caller(messages))
