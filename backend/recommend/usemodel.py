from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')

def testmodel(prompt):
    completion = client.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:hamza::AwwppreQ",
        messages=[
            {"role": "system", "content": "You are a specialized assistant trained only on COIS courses and that recommends other COIS courses. If the question is outside this domain, politely decline to answer and state that you can only respond to questions to recommend or provide information about COIS courses"},
            {"role": "user", "content": f"{prompt}? If you are unsure of the answer respond by saying that you are only allowed to answer on the topic of COIS courses"}
        ]
    )

    return completion.choices[0].message