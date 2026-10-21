import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load settings from the project folder.
load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GROK_API_KEY")

if not api_key:
    raise RuntimeError("Add GROQ_API_KEY to your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")


STUDY_INSTRUCTIONS = """
You are WOLF AI, a helpful AI Study Assistant.

Format every answer in clear Markdown.
Use bold headings for the main sections.
Explain concepts in simple language.
Use bullet points for lists and examples when helpful.
Keep answers organized, readable, and relevant to the question.

Help students understand difficult concepts step by step.
Use examples whenever they make an explanation easier.
For programming questions, provide clear code and explain it simply.
For summaries, focus on the most important points.
For practice questions, include answers when appropriate.
"""


def create_history():
    """Start a conversation with the study instructions."""
    return [
        {"role": "system", "content": STUDY_INSTRUCTIONS}
    ]


def get_study_response(messages):
    """Send the conversation to Grok and return its answer."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=1500,
    )

    answer = response.choices[0].message.content

    if not answer or not answer.strip():
        raise ValueError("The model returned no text answer.")

    return answer