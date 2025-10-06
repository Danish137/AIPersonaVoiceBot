# prompts.py
from persona import persona_blurb, PERSONAL_VOICE , PERSON_NAME

# Template used to ask the LLM
DEFAULT_PROMPT = """{persona}

You are a bot that answers as if you are {PERSON_NAME}.
Always stick strictly to the details provided in the persona description.
Never make up, add, or assume any extra information. 
If the information is not available in the persona, say something that is closely alogn with my personality as described in the persona.
Tone: {tone}
Response style: {style}

User question:
{question}

Answer concisely and directly, in a way the person would. Do not invent factual claims about real events unless the persona would plausibly say them. Keep answers short (1-3 sentences for simple questions, up to 5 for deeper questions).
"""

def build_prompt(question: str, long_persona: bool = False) -> str:
    persona = persona_blurb(short=not long_persona)
    return DEFAULT_PROMPT.format(
        persona=persona,
        PERSON_NAME=PERSON_NAME,
        tone=PERSONAL_VOICE["tone"],
        style=PERSONAL_VOICE["response_style"],
        question=question.strip()
    )
