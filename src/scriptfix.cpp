// src/scriptfix.cpp

#include "header.h"
#include "scriptfix.h"
#include "utility.h"

using namespace std;

int scriptfix(string& location) {
    
    return run_python_helper("scriptfix.py", location, "unable to fix the script");
}
