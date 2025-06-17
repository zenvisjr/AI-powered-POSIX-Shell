import sys
from common import ask_gpt

def run_interactive_tutorial(topic):
    prompt = f"""
You are a friendly and expert Linux tutor.

The user wants to learn: {topic}

Break it into clear, beginner-friendly **step-by-step instructions**, suitable for the terminal.

Respond using this format ONLY:
Step 1: <instruction>
Step 2: <instruction>
Step 3: <instruction>
...
Do NOT add explanations or summaries. Each step should be concise and command-line actionable.
"""

    result = ask_gpt(prompt).strip()

    if not result:
        print("ERROR: Empty response from GPT.")
        return

    steps = [line.strip() for line in result.split('\n') if line.strip().lower().startswith("step")]
    if not steps:
        print("ERROR: No valid steps found in GPT response.")
        return

    print(f"\n📚 Tutorial: {topic.strip()}\n")

    for step in steps:
        print(step)
        while True:
            print("✅ Ready to continue? (Y/n):")
            cont = input().strip().lower()
            if cont in ("y", "yes", ""):
                print()  # Add spacing before next step
                break
            elif cont in ("n", "no"):
                print("❌ Tutorial stopped.")
                return
            else:
                print("Please type Y or n.")

    print("\n🎉 Tutorial completed!\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: learn.py '<topic>'")
        sys.exit(1)

    topic = sys.argv[1].strip()
    if not topic:
        print("ERROR: Topic cannot be empty.")
        sys.exit(1)

    run_interactive_tutorial(topic)
