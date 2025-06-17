import sys
import os
import re
from common import ask_gpt

def generate_script(input_line):
    # Parse description and location
    parts = input_line.split("--location")
    if len(parts) != 2:
        print("ERROR: Usage: script: <desc> --location <file_path>")
        return 1

    description = parts[0].strip()
    output_path = parts[1].strip()

    prompt = f"""
You are a Linux shell scripting assistant.

The user has described a task for which you must generate a clean, safe, and functional Bash script.
Your job is to write production-quality Bash code based strictly on the following description:

"{description}"

Respond **only** using this exact format:

SCRIPT:
```bash
<correct and complete bash script goes here, no comments unless critical>
```
Guidelines:

- The script must be complete and syntactically valid.

- Avoid using placeholder phrases like "add your command here".

- Only include meaningful logic based on the task.

- Use best practices: input validation, proper variable naming, and safe execution.

- Never write malicious, dangerous, or unethical commands.

- If the request is suspicious or unsafe, reply with: ERROR: Unsafe or invalid task description.

"""

    result = ask_gpt(prompt)
    print(result)

    # Extract code from response
    match = re.search(r"SCRIPT:\s*```(?:bash)?\s*([\s\S]*?)```", result)
    if match:
        code = match.group(1).strip()

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w") as f:
            f.write(code + "\n")

        print(f"\n✅ Script saved to: {output_path}")
        # print(f"📥 Download: file://{os.path.abspath(output_path)}")
        print(f"▶️ Run with: bash {output_path}")
        return 1
    else:
        print("ERROR: Could not extract valid script from GPT response.")
        if "ERROR: Unsafe or invalid task description" in result:
            print("❌ Task was rejected: Unsafe or invalid description.")
        else:
            print("ERROR: Could not extract valid script from GPT response.")

        return 0

# CLI entry
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: scriptgen.py '<desc> --location <file.sh>'")
        sys.exit(1)
    generate_script(sys.argv[1])
