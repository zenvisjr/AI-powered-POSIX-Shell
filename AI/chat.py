# AI/chat.py

import sys
from common import ask_gpt

def chat_mode(user_input):
    prompt = f"""
    You're an intelligent Linux assistant inside a terminal. The user asked:

    {user_input}

    Provide a short and helpful response.
    """
    result = ask_gpt(prompt)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No input provided.")
        sys.exit(1)

    chat_mode(sys.argv[1])
