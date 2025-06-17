// src/fix.cpp

#include "header.h"
#include "fix.h"
#include "utility.h"

using namespace std;

int fix(string& prompt) {
    return run_python_helper("fix.py", prompt, "unable to fix the command");
}
