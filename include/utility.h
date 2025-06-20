#ifndef UTILITY_H
#define UTILITY_H

char* string_to_Cstyle(std::string &input);
std::string trim_both(std::string& command);
std::string trim(std::string &input);
void tokenize_string(std::vector<std::string>& tokens, std::string& input);
void print(std::vector<std::string>);
std::string find_separator(std::vector<std::string>& arguments);
void extract(std::vector<std::string>& arguments, std::string& separator, std::vector<std::string>& command, std::vector<std::string>& output);
std::string tokenize(std::string &input);

//for AI stuff
int run_python_helper(const std::string& script_name, std::string& args, const std::string& error_msg);
bool validate_script_path(const std::string& path);

#endif
