# AI/explain.py

import sys
from common import ask_gpt 

# Check if user passed a command to explain
if len(sys.argv) < 2:
    print("Usage: python3 explain.py <shell command>")
    sys.exit(1)

# Get the shell command from command-line arguments
command = ' '.join(sys.argv[1:])

# Build a natural language prompt for GPT
prompt = f"""
You're a helpful Linux shell tutor for beginners.  
Given the following command, explain it in very simple language.

- Break it into parts and explain each flag or component.
- Use bullet points (•) for each part.
- At the end, summarize what the command as a whole does in one sentence.

Command: {command}
"""

# Ask GPT for explanation
result = ask_gpt(prompt)

# Print the explanation (this will be read by the C++ shell)
print(result)
