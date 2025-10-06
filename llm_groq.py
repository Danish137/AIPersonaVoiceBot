
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("Missing GROQ_API_KEY. Please set it in your .env file.")


client = Groq(api_key=GROQ_API_KEY)

def groq_generate(prompt: str, model: str = "openai/gpt-oss-120b") -> str:
    """
    Generate text using Groq's API.
    Default model: LLaMA 3 8B.
    """
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are Danish Akhtar, AI/ML engineer and creative storyteller. Respond in first person, humble, clear, reflective."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=300,
    )
    return completion.choices[0].message.content.strip()


if __name__ == "__main__":
    from prompts import build_prompt
    question = "where can i find your projects"
    prompt = build_prompt(question)
    response = groq_generate(prompt) 
    print("LLM Response:", response)
