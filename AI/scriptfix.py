import sys
import os
import re
from common import ask_gpt

def fix_shell_script(path):
    if not os.path.exists(path):
        print("❌ File does not exist.")
        sys.exit(1)

    with open(path, "r") as f:
        script = f.read()

    prompt = f"""
    You're a Linux shell script expert. A user has provided a shell script that may contain bugs or inefficiencies.

    Your task is to:
    1. Analyze it and explain all bugs or problems in clear, numbered bullet points.
    2. Rewrite the corrected version of the shell script with **no comments**, just the clean fixed code.
    3. Wrap the corrected script inside triple backticks with `bash` after FIXED: exactly as shown below.

    ❗ Very Important:
    - Do NOT add any explanation after the FIXED section.
    - The FIXED section must start with: FIXED:
    - Then directly open with: ```bash
    - Then the corrected script
    - Then close with: ```

    If the input is invalid or not a shell script, reply with:
    ERROR: Not a valid shell script.

    Respond in this exact format:

    BUGS:
    1. <bug 1>
    2. <bug 2>
    ...

    FIXED:
    ```bash
    <fixed script>

    Shell Script:
    {script}
    """


    result = ask_gpt(prompt)

    # Check for outright error
    if result.strip().startswith("ERROR"):
        print(result)
        sys.exit(1)

    print(result)  # Show full response in terminal

    # Extract the FIXED section inside triple backticks
    match = re.search(r"FIXED:\s*```(?:bash)?\s*([\s\S]*?)```", result, re.IGNORECASE)
    if match:
        # print(result)  # Show full response in terminal
        fixed_code = match.group(1).strip()

        # Save to new file in same directory
        dir_path = os.path.dirname(path)
        base_name = os.path.basename(path).rsplit(".", 1)[0]
        new_path = os.path.join(dir_path, f"{base_name}_fixed.sh")

        with open(new_path, "w") as f:
            f.write(fixed_code + "\n")

        print(f"\n✅ Fixed script saved to: {new_path}")
        # print(f"📥 Download: file://{os.path.abspath(new_path)}")
        print(f"▶️ Run with: bash {new_path}")
        sys.exit(0)
    else:
        print("\n⚠️ Could not extract the corrected script from the response.")
        sys.exit(1)

# CLI Entry
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fix.py <path>")
        sys.exit(1)

    fix_shell_script(sys.argv[1])
