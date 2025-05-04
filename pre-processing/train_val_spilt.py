import random

def split_jsonl_file(input_file, train_file, val_file, split_ratio=0.8):
    # Read the lines from the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Shuffle the lines
    random.shuffle(lines)
    
    # Calculate the split index
    split_index = int(len(lines) * split_ratio)
    
    # Split the lines into training and validation sets
    train_lines = lines[:split_index]
    val_lines = lines[split_index:]
    
    # Write the training lines to the training file
    with open(train_file, 'w') as f:
        f.writelines(train_lines)
    
    # Write the validation lines to the validation file
    with open(val_file, 'w') as f:
        f.writelines(val_lines)

# Example usage
input_file = '../data/course_data_new_chattype.jsonl'
train_file = '../data/train.jsonl'
val_file = '../data/val.jsonl'
split_jsonl_file(input_file, train_file, val_file)

print(f"The file {input_file} has been split into {train_file} and {val_file} with an 80%-20% split.")