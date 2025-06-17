#include "header.h"
#include "utility.h"
#include <regex>
#include "summarizer_history.h"

int summarizer_history(std::string& input) {
    int num_commands = 20; // default
    std::string mode = "verbose"; // default
    std::smatch match;

    // Extract number of commands using regex (e.g., summarize:10)
    std::regex number_pattern(R"(summarize:(\d+))");
    if (std::regex_search(input, match, number_pattern)) {
        num_commands = std::stoi(match[1]);
        if (num_commands > 50) num_commands = 50; // cap to prevent overload
    }

    // Check mode flags
    if (input.find("--brief") != std::string::npos) {
        mode = "brief";
    }

    HIST_ENTRY** hist = history_list();
    if (!hist || history_length == 0) {
        std::cerr << "No command history found.\n";
        return 0;
    }

    int count = std::min(num_commands, history_length);
    std::string joined;

    for (int i = history_length - count; i < history_length; ++i) {
        joined += hist[i]->line;
        if (i != history_length - 1) joined += " && ";
    }

    std::string args = "--mode=" + mode + " --input=\"" + joined + "\"";
    return run_python_helper("summarizer_history.py", args, "Unable to summarize session history");
}
