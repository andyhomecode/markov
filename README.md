# Markov Chain Text Generator

This project implements a simple Markov chain text generator that can learn patterns from text and generate new text in a similar style.

## What is a Markov Chain?

A Markov chain is a mathematical model that predicts the next state based only on the current state, not on past states. In text generation, each "state" is a word, and the chain learns which words are likely to follow other words.

For example, if the training text contains "the cat in the hat", the model learns that "the" has 50/50 odds of being followed by either "cat" or "hat", "cat" is followed by "in", etc. When generating text, it starts with a word and randomly selects the next word based on what it learned from the training data.

## Instead of a Large Language Model, a Small Language Model
Similarities Between This Markov Chain and an LLM
- Text Generation: Both learn patterns from training data and generate new text by predicting the next word/token based on probabilities.
- Probabilistic Selection: They use statistical methods to choose subsequent words, creating coherent sequences to varying degrees.
- Training Basis: Both rely on large amounts of text data to build their models, capturing language patterns.

Differences Between This Markov Chain and an LLM
- Context Window:
    - Markov Chain: Uses only the immediate previous word (context window of 1), making it memoryless beyond that.
    - LLM: Considers a much larger context (e.g., thousands of previous tokens), allowing for long-range dependencies and better coherence.
- Model Complexity:
    - Markov Chain: Simple statistical model based on word transition counts; essentially a lookup table.
    - LLM: Complex neural network (transformer-based) that learns intricate patterns, semantics, and relationships.
- Parameters:
    - Markov Chain: Number of parameters equals the number of unique words in the training text(potentially thousands).
    - LLM: Billions of parameters, enabling richer representations and generalization.
- Training Method:
    - Markov Chain: Rule-based counting of word pairs from the training text.
    - LLM: Deep learning with backpropagation on massive datasets, requiring significant computational resources.

## Programs

### 1. clean_text.py
Cleans raw text by removing metadata, blank lines, and non-ASCII characters.

**Usage:**
```
python clean_text.py <input_file> <output_file>
```

**Example:**
```
python clean_text.py raw_text.txt cleaned_text.txt
```

### 2. train_model.py
Builds a Markov chain model from cleaned text and saves it as JSON.

**Usage:**
```
python train_model.py <text_file> <output_file>
```

**Example:**
```
python train_model.py cleaned_text.txt model.json
```

This will display model statistics including word counts, follower distributions, and top words.

### 3. generate_text.py
Generates new text using a trained Markov chain model.

**Usage:**
```
python generate_text.py <start_word> <num_words> <model_file>
```

**Example:**
```
python generate_text.py "Cat" 100 model.json
```

This generates 100 words of text starting with "The" using the model in model.json.

## Workflow

1. Clean your raw text: `python clean_text.py raw.txt clean.txt`
2. Train the model: `python train_model.py clean.txt model.json`
3. Generate text: `python generate_text.py "Cat" 50 model.json`

## Notes

- The model preserves capitalization and punctuation for more natural text generation.
- Larger training texts produce better results.
- The model is saved as JSON for easy inspection and reuse.