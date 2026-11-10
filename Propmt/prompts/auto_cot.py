import sys
from pathlib import Path
import json

# add the project root (the folder containing openai_adapter/) to the import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from openai_adapter.adapter import caller

SYSTEM_PROMPT = """
You are an expert AI assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given JSON output format.
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

Output JSON Format:
{ "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

Example:
START: Hey, can you solve 2 + 3 * 5 / 10 ?
PLAN: { "step": "PLAN", "content": "Seems like user is interested in a math problem" }
PLAN: { "step": "PLAN", "content": "Looking at the problem, we should solve this using the BODMAS method" }
PLAN: { "step": "PLAN", "content": "Yes, the BODMAS is the correct thing to be done here" }
PLAN: { "step": "PLAN", "content": "First, we must multiply 3 * 5 which is 15" }
PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
PLAN: { "step": "PLAN", "content": "We must perform the divide, that is 15 / 10 = 1.5" }
PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
PLAN: { "step": "PLAN", "content": "Finally, let's perform the add: 2 + 1.5 = 3.5" }
PLAN: { "step": "PLAN", "content": "Great, we have solved it and finally are left with 3.5 as the answer" }
OUTPUT: { "step": "OUTPUT", "content": "3.5" }
"""
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
]


def auto_cot():
    question = input("Ask anything: ")
    messages.append({"role": "user", "content": question})

    for _ in range(20):
        ans = caller(messages, isJson=True)
        messages.append({"role": "assistant", "content": ans})

        data = json.loads(ans)
        if data["step"] == "OUTPUT":
            print("## FINAL ##")
            print(data["content"])
            break

        print(f'[{data["step"]}] {data["content"]}')
        messages.append({"role": "user", "content": "Continue with the next step."})


auto_cot()
