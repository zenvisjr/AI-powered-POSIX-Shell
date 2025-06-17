# AI/generate.py

import sys
from common import ask_gpt  # Reuse the same helper

# Check if user passed a natural language description
if len(sys.argv) < 2:
    print("Usage: python3 generate.py <task description>")
    sys.exit(1)

# Join all command-line arguments to form one full task
task = ' '.join(sys.argv[1:])

# Prompt GPT to convert it into a valid bash command
prompt = f"""You are a helpful Linux assistant. Convert the following instruction into a safe single-line bash command only.
Instruction: {task}
Return only the command, nothing else
If its not a valid instruction or not a safe command, start prompt with ERROR:  """

# Ask GPT for shell command
result = ask_gpt(prompt)

# Print result back to C++ shell
print(result)
