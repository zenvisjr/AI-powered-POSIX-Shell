
# AI-Powered Custom POSIX Shell

## Table of Contents

#### [Overview](#overview)
#### [Features Implemented](#features-implemented)
   - [Shell Prompt](#shell-prompt)
   - [cd command](#cd-command)
   - [echo command](#echo-command)
   - [pwd command](#pwd-command)
   - [ls command](#ls-command)
   - [Process Management](#process-management)
   - [pinfo Command](#pinfo-command)
   - [Signals Handling](#signals-handling)
   - [I/O Redirection](#io-redirection)
   - [Piping](#piping)
   - [History](#history)
   - [Auto-Completion](#auto-completion)
   - [Search](#search)

   - [AI-Powered Features](#ai-powered-features)
     - [explain](#explain)
     - [generate](#generate)
     - [copilot](#copilot)
     - [scriptgen](#scriptgen)
     - [scriptfix](#scriptfix)
     - [summarize](#summarize)
     - [summarizer_history](#summarizer_history)
     - [learn](#learn)
     - [chat](#chat)
     - [fixing error made easy](#fixing-error-made-easy)
   - [Theme Changer](#theme-changer)

#### [Implementation Details](#implementation-details)
#### [Requirements](#requirements)
#### [Project Structure](#project-structure)
#### [Installation and Setup](#installation-and-setup)
#### [Usage](#usage)
#### [OpenAI API Key Setup](#openai-api-key-setup)
#### [Contributing](#contributing)
#### [Learning Outcomes](#learning-outcomes)
#### [Author](#author)
#### [Points to Notice](#points-to-notice)



---

## Overview

This is a AI powered custom shell implementation in C++ that mimics the original Linux terminal, demonstrating a deep understanding of process management, system calls, and core shell functionality, enhanced with AI-powered features using OpenAI’s GPT models for intelligent command explanation, generation, debugging, and interactive assistance.


## Features Implemented

### Shell Prompt
- Dynamically displays `username@system_name:current_directory>`.
- Supports random spaces and tabs in command input.
- Home directory represented by `~`.

### `cd` Command
- Supports flags: `.`, `..`, `-`, `~`.
- Handles directory navigation with error checking.
- Changes current working directory and reflects absolute path.

### `echo` Command
- Prints input strings.
- Handles tabs and spaces.

### `pwd` Command
- Displays current working directory.

### `ls` Command
- Implements detailed file/directory listing.
- Supports flags:
  - `-a`: Show all files (including hidden).
  - `-l`: Detailed listing with file permissions, size, etc.
- Handles multiple flags and directory arguments.
- Supports various input combinations like `ls`, `ls -a`, `ls -l`, etc.

### Process Management

#### Foreground Processes
- Shell waits for process completion.
- Blocks the shell until process exits.

#### Background Processes
- Use `&` to run processes in the background.
- Prints Process ID (PID) of background processes.
- Supports multiple simultaneous background processes.

### `pinfo` Command
- Displays process information.
- Shows PID, process status, memory usage, executable path.
- Supports querying specific process or current shell process.

### Signals Handling
- `CTRL-Z`: Push foreground job to background.
- `CTRL-C`: Interrupt running foreground process.
- `CTRL-D`: Logout from shell.

### I/O Redirection
- Supports `<`, `>`, `>>` operators.
- Redirects input/output for commands.
- Creates/overwrites/appends output files.
- Handles input file non-existence.

### Piping
- Implements `|` for command chaining.
- Supports multiple pipe combinations.
- Works with redirection.

### History
- Stores the last 20 commands.
- `history` command displays recent commands.
- Up arrow key navigation through command history.

### Auto-completion
- Implements auto completion using the Readline library.
- Suggests commands, file names, and directory names dynamically using tab key.

### Search 
- Provides `search` command to find files or text within files.
- Supports recursive directory search.

### AI-Powered Features

AI features are integrated into the shell using a Python backend (`common.py`) that communicates with OpenAI's GPT models via API. These enhance the shell with intelligent suggestions, explanations, script generation, debugging, and summarization.




| Command Name          | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `explain:`             | Explains a shell command in simple language.                 |
| `generate:`            | Generates a shell command from a natural language prompt.    |
| `copilot:`             | Provides smart, context-aware command-line suggestions.      |
| `scriptgen:`           | Creates full shell scripts from plain English descriptions.  |
| `scriptfix:`           | Analyzes and fixes bugs in shell script files.               |    |
| `summarize:`           | Summarizes the output of shell command pipelines.            |
| `summarizer_history:`  | Summarizes the last N commands from shell history.           |
| `learn::`              | Interactive tutorials on shell topics step-by-step.          |
| `chat:`                | Opens a live AI chat session directly in the shell.          |

### `explain`

The `explain` command lets you get a simple, human-friendly explanation of any shell command or pipeline. It helps understand complex or unfamiliar commands without leaving the terminal.

**Syntax:**
```bash
explain: <shell_command>
```
**Example**
```bash
explain: rsync -av --progress source/ dest/
```

### `generate`

The `generate` command creates a shell command from a natural language description you provide. It helps translate plain English tasks into actual shell commands.

**Syntax:**
```bash
generate: <natural_language_description>
```
**Example**
```bash
generate: copy all .cpp files from src to build
```

### `copilot` 

The `copilot` command provides smart, context-aware command-line suggestions and completions for a given input. It helps by recommending commands, flags, or options based on your current input.

**Syntax:**
```bash
copilot: <command>
```
**Example**
```bash
copilot: git chec (may suggest git checkout)
```

### `scriptgen`

The `scriptgen` command generates a complete shell script based on a natural language description. You need to specify the output file location using the `--location` flag (mandatory).

**Syntax:**
```bash
scriptgen: <description> --location <filepath>
```
**Example**
```bash
scriptgen: backup all .log files from /var/log to /backup/logs --location /tmp/backup_logs.sh

```
### `scriptfix`

The `scriptfix` command analyzes a shell script file for errors or bugs and automatically suggests fixes or corrections.

**Syntax:**
```bash
scriptfix: <script_file_path>
```
**Example**
```bash
scriptfix: /home/user/test.sh
```

### `summarize`

The `summarize` command provides a concise summary of the output from a shell command or pipeline. It helps quickly understand large or complex outputs.



**Syntax:**
```bash
<command> | summarize 
```

**Example**
```bash
cat server.log | summarize
```

### `summarizer_history`

The `summarizer_history` command summarizes the last *N* shell commands you have executed (max is capped at 50), providing an overview or insights on your recent activity.
**Flags:**

`--brief`: One-paragraph high-level summary.

`--verbose`: Multi-point detailed analysis (`default`).

**Syntax:**
```bash
summarizer_history:<N> [--brief | --verbose]
```
**Example**
```bash
summarizer_history:10 --verbose
```
### `learn:`

The `learn:` command initiates an interactive, step-by-step tutorial on various shell topics like SSH, crontab, chmod, and more. It guides users through concepts with explanations and prompts.

**Syntax:**
```bash
learn: <topic>
```
**Example**
```bash
learn: ssh
```

### `chat`

The `chat` command opens an interactive AI chat session directly inside the shell. You can ask general questions, seek help with commands, or discuss any Linux-related topic in natural language.

**Syntax:**
```bash
chat: 
> <your_question_or_message>
> <your_question_or_message>
```
**Example**
```bash
chat: 
> how to use tar with compression?
```

### Fixing error made easy
When you type a command that is not implemented then it goes to exec() function and if you get any error then AI suggest what when wrong, possible solution or insights by using the stderr. 

`NOTE: Actual error is also printed on terminal`

### Theme Changer

- Supports dynamic shell themes based on user mood commands.
- Command syntax: `set mood: <theme_name>`.
- Currently supports:
  - `hacker` mood: neon-style ASCII banner, colored prompt, and command output with sound effects.
  - `default` mood: standard shell appearance.
- Enhances terminal aesthetics and user experience.


## Implementation Details

- **Language**: C/C++ for core shell implementation; Python for AI integration.
- **System Calls**: `fork()`, `exec()`, `wait()`, `signal()` for process and signal management.
- **Error Handling**: Using `perror()` for system call errors and custom error messages for AI commands.
- **Design**: Modular design with separate functions handling parsing, execution, piping, redirection, and AI command dispatch.
- **AI Features Implementation**:
  - AI commands are identified during input parsing in the shell.
  - The shell uses `popen()` to invoke a Python helper script (`ai_helper.py`), passing user input to it.
  - The Python script loads the OpenAI API key securely from a `.env` file using `python-dotenv`.
  - Requests are sent to the OpenAI API (GPT models) with prompts constructed based on the command type.
  - Responses from OpenAI are read back via `popen()` and displayed in the shell.
  - This cross-language communication allows seamless integration of AI without blocking core shell functionality.


## Requirements

Before you begin, ensure you have the following software installed:

- **g++**: The GNU C++ compiler.
- **Make**: A build automation tool.
- **Readline library**: For command-line editing and auto-completion.
- **Python 3**: Required to run the AI integration scripts.
- **pip**: Python package manager to install dependencies.
- **OpenAI Python SDK**: For accessing GPT APIs.
- **python-dotenv**: To securely load API keys from `.env` file.


## Project Structure

```
/AI-powered-POSIX-Shell
|-- /include              # Header files
|-- /src                  # Source files
|-- /build                # Directory for compiled object files and 
|-- /AI                   # AI integration scripts (Python)
|-- Makefile              # Makefile to build the project
```

### Key Files and Folders

- **include**: Contains header files (`*.h`) for core shell features and AI dispatch functions.
- **src**: C++ implementation files (`*.cpp`) for command execution, piping, redirection, and AI command routing.
- **AI**: Python helper scripts for all AI-powered features.
  - `common.py`: Central script to interact with the OpenAI API.
- **build**: Contains compiled object files and the final executable (`endgame`).
- **Makefile**: Automates the build process — compiles C++ sources and links them into a single binary.
- **.gitignore**: Ensures sensitive files like `.env` are excluded from version control.



## Installation and Setup

1. Clone the repository or download the project:
   ```bash
   git clone https://github.com/zenvisjr/Academics.git
   cd Projects/AI-powered-POSIX-Shell
   ```

2. Install the necessary dependencies. For Ubuntu/Debian:
   ```bash
   # C++ dependencies
   sudo apt-get update
   sudo apt-get install g++ make libreadline-dev

   # Python dependencies
   sudo apt-get install python3 python3-pip
   pip install openai python-dotenv

   #To install the OpenAI SDK:
   pip install openai
   ```


3. Build the project using the `Makefile`. In the root directory of the project:
   ```bash
   make
   ```

   This will compile the source files and generate the executable `endgame` in the `/build` directory.



## Usage

After building the project, you can run the shell by executing the following command:

```bash
./build/endgame
```

## OpenAI API Key Setup

To use the AI-powered features (like `explain:`, `generate:`, `fix:`, etc.), you need an OpenAI API key. Since this key is personal and tied to your billing account, it is **not shared in this repository**.

### Steps to set up your API key:

1. **Get your OpenAI API key**  
   Visit: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)  
   Log in and copy your personal API key (starts with `sk-...`)

2. **Create a `.env` file in the root directory**  
   In your project folder (`AI-powered-POSIX-Shell`), create a new file named `.env`:
   ```bash
   touch .env
   ```
3. **Add your API key to the `.env` file**

   Open `.env` in any text editor and paste the following:
   ```bash
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
⚠️ Never share your .env file or API key publicly. It can be misused for billing or abuse.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Please follow the guidelines for clear and concise commit messages.


## Learning Outcomes

- Process creation and management using `fork()`, `exec()`, and `wait()`.
- System programming in Unix-like environments.
- Command parsing, tokenization, and execution flow.
- Signal handling (e.g., `SIGINT`, `SIGTSTP`) and custom process control.
- I/O redirection and piping techniques.
- History management and job control.
- Integration of C++ with Python for cross-language architecture.
- Use of OpenAI APIs for intelligent terminal features.
- Secure handling of API keys using `.env` and `python-dotenv`.
- Modular and extensible shell design.



## Author

**Ayush Rai**  
Email: ayushrai.cse@gmail.com


## Points to Notice:
- The tab key does not currently work for giving spaces in the terminal as it is used for auto complete.
- Some processes like Nautilus (Ubuntu's file explorer) and Firefox, for which the terminal parent process does not wait, will cause the prompt to return immediately without waiting for the process to complete.
- When using piping with output redirection, the final output is written to the output file, but `execvp` still shows a `perror` message.
- Typing a random process name and running it in the background gives a `perror` in `execvp`, but the terminal gets stuck and does not move to the next line.

---
