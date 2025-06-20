#include "header.h"
#include "utility.h"
using namespace std;

char* string_to_Cstyle(string &input)
{
    char *a = new char[input.length()+1];
    strcpy(a, input.c_str());
    return a;

}

string trim(string &input)
{
    int s = input.find_first_not_of(" \t");
    input = input.substr(s);
    return input;
}

string trim_both(string& command)
{
    size_t s = command.find_first_not_of(" \t");
    size_t e = command.find_last_not_of(" \t");

    if(s != string::npos && e != string::npos)
    {
        command = command.substr(s, e-s+1);
    }
    else
    {
        cout<<"not a valid commamd"<<endl;
    }
    return command;
}

void tokenize_string(vector<string>& arguments, string& command)
{
    string arg;
                
    bool sq = false, dq= false;
    
    for(char v: command) 
    {
        if(v == '\'') 
        {
            sq = !sq; 
        } 
        else if(v == '\"') 
        {
            dq = !dq; 
        } 
        else if(v == ' ' && !sq && !dq) 
        {
            if(!arg.empty()) 
            {
                arguments.push_back(arg);
                arg.clear();
            }
        } 
        else 
        {
            arg += v;
        }
    }

    // Push the last command
    if(!arg.empty()) 
    {
        arguments.push_back(arg);
    }
    //print(arguments);
}

string find_separator(vector<string>& arguments) 
{
    // Define a list of possible separators
    vector<string> sep = {">", "<", ">>", "|"};

    for (auto v : arguments) 
    {
        if (find(sep.begin(), sep.end(), v) != sep.end()) 
        {
            return v;  // Return the first separator found
        }
    }

    return "";  // Return an empty string if no separator is found
}

void print(vector<string> list)
{
    for (auto args : list)
    {
    cout << "Argument: " << args << endl;
    }
    cout<<endl;
}

void extract(vector<string>& arguments, string &separator, vector<string>& com, vector<string>& output)
{

    bool find_sep = false;

    for(auto v : arguments)
    {
        if(v == separator) find_sep = true;
        else
        {
            if(find_sep == false)
            {
                com.push_back(v);
                //com += " ";

            }
            else
            {
                output.push_back(v);
                //output += " ";
            }
        }
    }
}

string tokenize(string &input) {
    string res = "";
    string temp = "";
    for (char ch : input) {
        if(ch == ' ') {
            if(temp.size() > 0) res += temp + " ";
            temp = "";
        }
        else temp += ch;
    }
    if(temp.size() > 0) res += temp;
    else temp.pop_back();     //remove last blank space
    return res;
}



//for AI stuff

std::string escape_quotes(const std::string& input) {
    std::string escaped;
    for (char c : input) {
        if (c == '"') escaped += "\\\"";
        else escaped += c;
    }
    return escaped;
}

int run_python_helper(const std::string& script_name, std::string& args, const std::string& error_msg) {
    std::string escaped_args;
    for (char ch : args) {
        if (ch == '\'')
            escaped_args += "'\\''";
        else
            escaped_args += ch;
    }

    std::string cmd = "python3 AI/" + script_name + " '" + escaped_args + "'";
    FILE* pipe = popen(cmd.c_str(), "r");

    if (!pipe) {
        std::cerr << "Failed to run " << script_name << std::endl;
        return 0;
    }

    char buffer[256];
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        std::cout << buffer;
    }

    int result = pclose(pipe);
    if (result != 0) {
        std::cerr << error_msg << std::endl;
        return 0;
    }

    return 1;
}



#include "header.h"
#include <filesystem>  // for std::filesystem::*

bool validate_script_path(const std::string& path) {
    try {
        std::filesystem::path outputPath(path);
        auto parent = outputPath.parent_path();

        if (parent.empty()) {
            std::cerr << "ERROR: Path must include a directory (e.g. /tmp/file.sh)\n";
            return false;
        }

        if (std::filesystem::exists(parent) && !std::filesystem::is_directory(parent)) {
            std::cerr << "ERROR: '" << parent << "' exists but is not a directory\n";
            return false;
        }

        std::filesystem::create_directories(parent);  // Create if not exists
        return true;

    } catch (const std::exception& e) {
        std::cerr << "ERROR: Path check failed — " << e.what() << "\n";
        return false;
    }
}
