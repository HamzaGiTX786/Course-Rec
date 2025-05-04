from openai import OpenAI
import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')

fine_tune_resposne = client.fine_tuning.jobs.create(
    training_file="file-WG2Vzf7syNgS5ZjKAEDSS1",
    validation_file="file-MtGpc6NcXMYiTnD698BUtJ",
    model="gpt-4o-mini-2024-07-18"
)

print(fine_tune_resposne)
