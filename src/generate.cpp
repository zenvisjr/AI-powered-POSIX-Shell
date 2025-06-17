// src/generate.cpp

#include "header.h"
#include "generate.h"
#include "utility.h"

using namespace std;

int generate(string& prompt) {
    return run_python_helper("generate.py", prompt, "unable to generate the command");
}
