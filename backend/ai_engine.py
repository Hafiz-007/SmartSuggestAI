import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_reply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're an AI assistant that answers and suggests helpful products if needed."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']