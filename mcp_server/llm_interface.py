import anthropic 
import os

api_key = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

def ask_claude(prompt: str) -> dict:
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=300,
        messages=[{"role" : "user", "content" : prompt}]
    )
    return {"response" : response.content[0].text}
