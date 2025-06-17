# AI/shellfix.py

import sys
from common import ask_gpt

def fix_error(command, error_msg):
    prompt = f"""
    You're a strict and intelligent Linux shell assistant. A user ran the following shell command and got an error.

    Command:
    {command}

    Error:
    {error_msg}

    Your task:
    1. If it's a known shell-related issue (e.g., permission denied, command not found, missing arguments, wrong syntax), suggest a safe and valid fix.
    2. If it's a possible spelling mistake (e.g., 'sl' instead of 'ls'), suggest the correct command.
    3. If the input is vague, gibberish, or not related to shell commands, respond with 'ERROR: Unrecognized or invalid shell command.'

    Output format:
    Start with **only one** of the following tags:
    - FIX: <your suggested fix>
    - ERROR: <explanation why it's invalid or can't be fixed>
    """


    result = ask_gpt(prompt)
    print(result)

# CLI Entry
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No input provided.")
        sys.exit(1)

    # print(f"DEBUG INPUT: {repr(sys.argv[1])}")  # Add this

    if "###" not in sys.argv[1]:
        print("ERROR: Invalid input format. Expected ### separator.")
        sys.exit(1)

    cmd, err = sys.argv[1].split("###", 1)
    fix_error(cmd.strip(), err.strip())