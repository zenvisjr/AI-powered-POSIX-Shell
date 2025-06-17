// src/copilot.cpp

#include "header.h"
#include "copilot.h"
#include "utility.h"

using namespace std;

int copilot(string& prompt) {
    return run_python_helper("copilot.py", prompt, "unable to provide copilot suggestions");
}
