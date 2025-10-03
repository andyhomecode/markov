import random
import json
import sys

def generate_text(markov_chain, start_word, num_words=50):
    """
    Generates text using the Markov chain model.
    """
    if start_word not in markov_chain:
        print(f"Start word '{start_word}' not found in the model. Please choose a word from the training text.")
        return ""

    generated_words = [start_word]
    current_word = start_word

    for _ in range(num_words - 1):
        if current_word in markov_chain and markov_chain[current_word]:
            next_word = random.choice(markov_chain[current_word])
            generated_words.append(next_word)
            current_word = next_word
        else:
            # If a word has no followers, stop or try a new random start
            break 
            
    return ' '.join(generated_words)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_text.py <start_word> <num_words> <model_file>")
        sys.exit(1)
    
    start_word = sys.argv[1]
    num_words = int(sys.argv[2])
    model_file = sys.argv[3]
    
    try:
        with open(model_file, "r") as f:
            chain = json.load(f)
    except FileNotFoundError:
        print(f"{model_file} not found. Please run train_model.py first.")
        sys.exit(1)
    
    generated_text = generate_text(chain, start_word, num_words)
    print(generated_text)