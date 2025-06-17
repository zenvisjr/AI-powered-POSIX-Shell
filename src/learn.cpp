
// src/chat.cpp

#include "header.h"
#include "learn.h"
#include "utility.h"

using namespace std;

int learn(string& prompt) {
    return run_python_helper("learn.py", prompt, "unable to provide explanation of the topic");
}
