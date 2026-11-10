import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()

key = os.getenv("API_KEY")
if not key:
    raise ValueError("API_KEY not found. Check your .env file.")

client = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def caller(messages, isJson=False):
    try:
        response = client.chat.completions.create(
            model="gemini-3.6-flash",
            reasoning_effort="low",
            response_format={"type": "json_object"} if isJson else None,
            messages=messages,
        )
        return response.choices[0].message.content

    except openai.BadRequestError as e:
        print("400 body:", e.response.text)
    except openai.RateLimitError as e:
        print("429 body:", e.response.text)
