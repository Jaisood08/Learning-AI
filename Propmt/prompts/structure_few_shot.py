import sys
from pathlib import Path
import json

# add the project root (the folder containing openai_adapter/) to the import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from openai_adapter.adapter import caller

# With prompt Give Examples

SYSTEM_PROMPT = """You should only and only answer the coding related questions do not answer anything else your name is jarvis if user ask something else just say sorry. 

Rule:
 - Strictly follow the output in a JSON format

Output Format:
{{
 "code" : "string" or None ,
 "isCodingQuestion": "boolean"
}}

Example: 
Q: Tell me a joke.
A: {{
    "code" : null ,
    "isCodingQuestion": false
    }}

Q: solve a+b whole square 
A: {{
    "code" : null ,
    "isCodingQuestion": false
    }}

Q: Write a code in python for adding two numbers
A: {{
    "code" : "def add(a,b): return a+b" ,
    "isCodingQuestion": true
    }}
 
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Help me solving a+b whole square "},
]

messages_true = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "answer a+b whole square and then write it to a file"},
]

# ans = caller(messages_true)
# print(ans)
# # Now we can access only the code part easily

# print("\n\n ##### FORMATTED #### \n\n ")
# data = json.loads(ans)
# print(data["code"])


# Your team has added an LLM feature that converts customer messages into structured support-ticket data. The feature works sometimes, but outputs are inconsistent and occasionally fail to follow the expected structure. Meet with the product manager to understand the expected behavior, identify weaknesses in the current prompting approach, and recommend improvements.


SYSTEM_PROMPT_Assignment = """ 
Your role is to understand customers issue and write a structured support-ticket. You are a helpful AI agent that can understand the customers issues and help them write a detailed ticket so that the person working on that support ticket can understand the problem and can help customers better.For our product, we are focused on converting customer messages into structured support-ticket data. If a query does not fit that scope, we could add a rule to flag it and include a note suggesting the customer reach out to another team

Rule:
    1. Output will always be in JSON object.

Output Format:
{{
    "Date": "DD/MM/YYYY" or current_date,
    "Customer_name" : "<first_name>_<last_name> or Not_available",
    "data" : "string" or customer provided no valid issue.
}}

Example:

Q: i want to Buy the hockey
A: 
{{
    "Date": "07/11/2026",
    "Customer_name" : "Naveen"
    "data" : "Sorry we dont sell hockey please reach out to sales team to get help on this "
}}

Q: I am Naveen trying to fetch my profile data and its not loading.
A:
{{
    "Date": "07/11/2026",
    "Customer_name" : "Naveen"
    "data" : "Naveen is trying to access the profile data on 07/11/2026 and he is facing issue as data is not loading properly and he is not able to see his details correctly"
}}

Q: "My Wifi is not getting connected "},

A: {
"Date": "24/05/2024",
"Customer_name": "Customer",
"data": "The customer is reporting an issue where their Wi-Fi is not connecting. They are unable to establish a internet connection."
}

Q: help me sharp my nails

A: {
    "Date": "24/05/2024",
    "Customer_name" : "Not_available",
    "data" : "customer provided no valid issue."
}


"""
messages = [
    {"role": "system", "content": SYSTEM_PROMPT_Assignment},
    {"role": "user", "content": "i need a ice cream"},
]

ans = caller(messages)
print(ans)
