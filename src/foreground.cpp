#include "header.h"
#include "foreground.h"
#include "exec.h"
#include "utility.h"

using namespace std;


// void foreground(std::vector<std::string>& arguments)
// {
//     pid_t pid = fork();

//     if(pid == -1)
//     {
//         perror("ERROR in creating child process");
//     }
//     else if(pid == 0)
//     {
//         signal(SIGINT, SIG_DFL);  
//         signal(SIGTSTP, SIG_DFL);
        
//         //cout<<"child: "<<pid<<endl;
//         call_exec(arguments);
//     }
//     else 
//     {
        
//         int status;
//         waitpid(pid, &status, WUNTRACED);   //Also return if a child has stopped
        
//     }
//      //signal(SIGINT, SIG_IGN); 
//      //signal(SIGTSTP, SIG_IGN);
     
// }


//fixing error with AI

void foreground(std::vector<std::string>& arguments)
{
    pid_t pid = fork();

    if (pid == -1)
    {
        perror("ERROR in creating child process");
    }
    else if (pid == 0)
    {
        // Child process
        signal(SIGINT, SIG_DFL);  
        signal(SIGTSTP, SIG_DFL);

        // Redirect stderr to temp file
        std::string error_file = "/tmp/ai_shell_stderr.txt";
        int fd = open(error_file.c_str(), O_WRONLY | O_CREAT | O_TRUNC, 0600);
        if (fd == -1) {
            perror("Failed to open temp stderr file");
            exit(1);
        }
        dup2(fd, STDERR_FILENO);
        close(fd);

        call_exec(arguments);
        exit(1);  // if exec fails
    }
    else
    {
        // Parent process
        int status;
        waitpid(pid, &status, WUNTRACED);

        // Read the captured stderr
        std::ifstream file("/tmp/ai_shell_stderr.txt");
        std::stringstream buffer;
        buffer << file.rdbuf();
        std::string error_output = buffer.str();

        if (!error_output.empty())
        {
            // Show real stderr first
            std::cout << "⚠️  Error:\n" << error_output << std::endl;

            // Reconstruct full command
            std::string full_command;
            for (auto& arg : arguments) full_command += arg + " ";

            std::string input = full_command + "###" + error_output;

            // Show GPT fix next
            std::cout << "🤖 Fix Suggestion:\n";
            run_python_helper("fix.py", input, "Unable to suggest a fix.");
        }
    }
}
