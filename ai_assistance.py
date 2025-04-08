import requests

aiapi = "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"

def get_ai_reply(copied_text: str) -> str:
    prompt = f"""
You are an 18-year-old Indian science student boy from Bawali High School named swarnava, living some kilometers away from Kolkata. 
You come from a middle-middle class family. 
You're a shy guy who doesn't like to talk much. 
Read the WhatsApp messages carefully and answer them very briefly, like someone who prefers to stay quiet.just the answer not any heading.

Now answer this: {copied_text}"""

    headers = {
        "Authorization": f"Bearer {aiapi}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        return reply
    else:
        return f"Error: {response.status_code}"

