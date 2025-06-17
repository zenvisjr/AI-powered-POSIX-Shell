
// src/chat.cpp

#include "header.h"
#include "chat.h"
#include "utility.h"

using namespace std;

int chat(string& prompt) {
    return run_python_helper("chat.py", prompt, "unable to respond to user");
}
