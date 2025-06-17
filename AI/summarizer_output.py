#!/usr/bin/env python3

import sys
from common import ask_gpt

def summarize_command_output(command_output):
    prompt = f"""
    You are a highly experienced Linux engineer. Summarize the following terminal command output in plain English.

    Focus only on the most important insights or issues.
    Format:
    SUMMARY: <your summary in 1-3 lines>

    Output:
    {command_output}
    """
    return ask_gpt(prompt)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: summarizer_output.py <output_file>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        with open(filepath, "r") as f:
            input_data = f.read().strip()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    if not input_data:
        print("ERROR: No data received from input.")
        sys.exit(1)

    # print("Original Output:\n")
    print(input_data)

    print("\n" + summarize_command_output(input_data))
