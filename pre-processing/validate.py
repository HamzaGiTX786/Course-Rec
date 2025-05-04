import json

# Load and validate the dataset
def validate_jsonl(file_path):
    with open(file_path, "r") as f:
        for line in f:
            entry = json.loads(line)
            assert "prompt" in entry and "completion" in entry, "Missing required fields."
            assert isinstance(entry["prompt"], str), "Prompt must be a string."
            assert isinstance(entry["completion"], str), "Completion must be a string."

    print("Dataset is valid!")

validate_jsonl("../data/course_data.jsonl")
