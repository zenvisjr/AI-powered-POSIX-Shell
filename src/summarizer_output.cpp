

// src/scriptfix.cpp

#include "header.h"
#include "summarizer_output.h"
#include "utility.h"

using namespace std;


int summarizer_output() {  // ✅ fixed name
    std::ifstream file("/tmp/ai_summarizer_output.txt");
    if (!file.is_open()) {
        std::cerr << "Error: Unable to open summarizer output file." << std::endl;
        return 0;
    }

    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string output_content = buffer.str();
    file.close();

    if (output_content.empty()) {
        std::cout << "No output to summarize." << std::endl;
        return 0;
    }
    string location = "/tmp/ai_summarizer_output.txt";
    return run_python_helper("summarizer_output.py", location, "Failed to summarize output.");
}

