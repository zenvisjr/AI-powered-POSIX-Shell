# AI/copilot.py

import sys
from common import ask_gpt

if len(sys.argv) < 2:
    print("Usage: python3 copilot.py <command>")
    sys.exit(1)

shell_command = ' '.join(sys.argv[1:])

# Prompt with safety-focused context
prompt = f"""
You're a cautious Linux shell assistant.

- If the command is valid, explain what it does briefly and start with: EXPLANATION:
- If it's unsafe or potentially dangerous, explain what it does and why it's dangerous. Start with: WARNING:
- If command is incorrect then suggest correct alrenative if possible and start with INCORRECT:
- If the command doesn't make sense or is incorrect, start with: ERROR:
- Important: Reply using **only one** of the above 4 formats, never mix them.

Command: {shell_command}
"""



result = ask_gpt(prompt)

# Return output to the shell
print(result)

# Exit with success
sys.exit(0)
