// src/explain.cpp

#include "header.h"
#include "explain.h"
#include "utility.h"

using namespace std;

int explain(string& prompt) {
    return run_python_helper("explain.py", prompt, "unable to explain the command");
}
