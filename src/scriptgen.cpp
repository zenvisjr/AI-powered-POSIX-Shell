// src/scriptfix.cpp

#include "header.h"
#include "scriptgen.h"
#include "utility.h"

using namespace std;

int scriptgen(string& prompt) {
    // Extract path from command for pre-validation
    std::string locationFlag = "--location";
    size_t pos = prompt.find(locationFlag);
    if (pos == std::string::npos) {
        std::cerr << "ERROR: Missing --location flag in command\n";
        return 1;
    }

    std::string location = prompt.substr(pos + locationFlag.length());
    location = trim_both(location);

    if (!validate_script_path(location)) {
        return 1;  // Path invalid or not creatable — skip GPT call
    }

    return run_python_helper("scriptgen.py", prompt, "unable to generate the script");
}
