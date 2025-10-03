import sys

if len(sys.argv) != 3:
    print("Usage: python clean_text.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as f:
    lines = f.readlines()

clean_lines = []
for line in lines:
    line = line.strip()
    # Remove non-ASCII characters
    line = ''.join(char for char in line if ord(char) < 128)
    if not line:  # blank line after stripping
        continue
    # Skip lines that are just names or titles (short lines without punctuation)
    if len(line) < 50 and not any(char in line for char in '.!?'):
        continue
    clean_lines.append(line)

with open(output_file, 'w') as f:
    f.write('\n'.join(clean_lines))