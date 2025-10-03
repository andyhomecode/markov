import random
import json
import sys
import statistics

def build_markov_chain(text_file_path):
    """
    Builds a Markov chain model from a text file.
    The model is a dictionary where keys are words and values are lists of words that follow them.
    """
    markov_chain = {}
    with open(text_file_path, 'r', encoding='utf-8') as f:
        text = f.read()  # Read the text (keeping original capitalization)
    
    # Simple tokenization: split by spaces (keeping punctuation attached to words)
    words = text.split()
    
    for i in range(len(words) - 1):
        # step through the text one word at a time, 
        # looking at each word and the one that follows

        current_word = words[i]
        next_word = words[i+1]
        
        if current_word not in markov_chain:
            markov_chain[current_word] = [] # if it's a new word, add it
        markov_chain[current_word].append(next_word) # and add whatever word followed it.
    
        # so "the cat in the hat" would produce:
        #
        # {"the": ["cat", "hat"], 
        # "cat": ["in"], 
        # "in": ["the"], 
        # "hat": []}
        # 


    return markov_chain, len(words)

def print_model_stats(chain, total_words):
    """Print statistics about the Markov chain model."""
    print("\n### Model Statistics ###")
    num_words = len(chain)
    followers = [len(chain[word]) for word in chain]
    max_followers = max(followers) if followers else 0
    median_followers = statistics.median(followers) if followers else 0
    avg_followers = sum(followers) / len(followers) if followers else 0
    
    # Percentiles
    sorted_followers = sorted(followers)
    p90 = sorted_followers[int(0.9 * len(sorted_followers))] if sorted_followers else 0
    p95 = sorted_followers[int(0.95 * len(sorted_followers))] if sorted_followers else 0
    p99 = sorted_followers[int(0.99 * len(sorted_followers))] if sorted_followers else 0
    
    # Counts
    num_single = sum(1 for f in followers if f == 1)
    num_many = sum(1 for f in followers if f > 10)
    
    print(f"Total words in training text: {total_words}")
    print(f"Number of unique words: {num_words}")
    print(f"Max followers per word: {max_followers}")
    print(f"Median followers per word: {median_followers:.2f}")
    print(f"Average followers per word: {avg_followers:.2f}")

    
    # ASCII bar chart for percentiles
    percentiles = [('90th', p90), ('95th', p95), ('99th', p99)]
    max_p = max(p for _, p in percentiles) if percentiles else 1
    print("\nPercentile Bar Chart:")
    for name, value in percentiles:
        bar_length = int(value * 50 / max_p) if max_p > 0 else 0
        bar = '|' * bar_length
        print(f"{name}: {value:3d} {bar}")
    
    # Top 50 words by followers in 3 columns
    top_words = sorted(chain.items(), key=lambda x: len(x[1]), reverse=True)[:50]
    print("\nTop 50 words by number of followers:")
    for i in range(0, len(top_words), 3):
        row = top_words[i:i+3]
        col1 = f"{row[0][0]}: {len(row[0][1])}" if len(row) > 0 else ""
        col2 = f"{row[1][0]}: {len(row[1][1])}" if len(row) > 1 else ""
        col3 = f"{row[2][0]}: {len(row[2][1])}" if len(row) > 2 else ""
        print(f"{col1:<25} {col2:<25} {col3}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python train_model.py <text_file> <output_file>")
        sys.exit(1)
    
    text_file = sys.argv[1]
    output_file = sys.argv[2]

    chain, total_words = build_markov_chain(text_file)
    print("### Built Markov Chain Model ###")

    print_model_stats(chain, total_words)

    with open(output_file, "w") as f:
        json.dump(chain, f, indent=4)
    print(f"### Model saved to {output_file} ###")