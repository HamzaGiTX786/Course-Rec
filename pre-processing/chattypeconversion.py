import json
import random

# Load your existing JSONL file
input_file = "../data/course_data_new_chattype.jsonl"
output_file = "../data/course_data_new_chattype.jsonl"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        data = json.loads(line)
        new_format = {
            "messages": [
                {"role": "system", "content": "You are a specialized assistant trained only on COIS courses and that recommends other COIS courses. If the question is outside this domain, politely decline to answer and state that you can only respond to questions to recommend or provide information about COIS courses"},
                {"role": "user", "content": data["prompt"]},
                {"role": "assistant", "content": data["completion"]}
            ]
        }
        outfile.write(json.dumps(new_format) + "\n")

print(f"File converted and saved as {output_file}")
