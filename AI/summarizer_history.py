
import sys
import re
import argparse
from common import ask_gpt

def parse_arguments():
    parser = argparse.ArgumentParser(description="Summarize shell session")
    parser.add_argument("--mode", choices=["brief", "verbose"], default="verbose", help="Summary mode")
    parser.add_argument("--input", type=str, required=True, help="Shell command history")
    return parser.parse_args()

def build_prompt(mode, history):
    if mode == "brief":
        return f"""
        You're an assistant that summarizes Linux terminal usage.

        Task: Summarize this command history in one paragraph for a report or log.

        Commands:
        {history}

        Output should be short and clear. Start with: SUMMARY:
        """
    else:
        return f"""
        You're a Linux expert analyzing a shell session.

        Task: Break down the session into logical chunks or themes.
        Group commands where possible and provide context.
        Mention any interesting patterns or repeated behaviors.
        Add helpful remarks where relevant.

        Commands:
        {history}

        Output format:
        SUMMARY:
        - Group 1: ...
        - Group 2: ...
        """

def main():
    args = parse_arguments()
    prompt = build_prompt(args.mode, args.input)

    result = ask_gpt(prompt)
    if not result.startswith("SUMMARY:"):
        print("ERROR: GPT did not return a valid summary")
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()
