import readline
from file_system import *


def display_help():
    commands = """
Available commands:
- mkdir <folder_name>       : Create a folder
- touch <file_name>         : Create a file
- ls                        : List contents of the current directory
- cat <file_name>           : Read a file
- rm <file_name>            : Delete a file
- rmdir <folder_name>       : Delete a folder
- mv <old_name> <new_name>  : Rename a file or folder
- cd <folder_name>          : Change directory
- cd ..                     : Move to the parent directory
- pwd                       : Print the current working directory
- alias <name> <command>    : Create an alias
- unalias <name>            : Remove an alias
- edit <file_name>          : Edit a file (opens in a basic text editor)
- help                      : Show this help menu
- exit                      : Exit the program
"""
    print(commands)


def execute_command(command):
    parts = command.split(" ", 2)
    cmd = parts[0].lower()

    # Check if the command matches an alias
    if cmd in aliases:
        command = aliases[cmd]
        parts = command.split(" ", 2)
        cmd = parts[0].lower()

    arg1 = parts[1] if len(parts) > 1 else None
    arg2 = parts[2] if len(parts) > 2 else None

    if cmd == "mkdir" and arg1:
        print(create_folder(arg1))
    elif cmd == "touch" and arg1:
        print(create_file(arg1))
    elif cmd == "ls":
        contents = list_contents()
        print("\n".join(contents) if contents else "Directory is empty.")
    elif cmd == "cat" and arg1:
        print(read_file(arg1))
    elif cmd == "rm" and arg1:
        print(delete_file(arg1))
    elif cmd == "rmdir" and arg1:
        print(delete_folder(arg1))
    elif cmd == "mv" and arg1 and arg2:
        print(rename_item(arg1, arg2))
    elif cmd == "cd" and arg1:
        print(change_directory(arg1))
    elif cmd == "cd":
        print("zsh: cd must have 1 argument")
    elif cmd == "pwd":
        print(print_working_directory())
    elif cmd == "alias" and arg1 and arg2:
        print(add_alias(arg1, arg2))
    elif cmd == "unalias" and arg1:
        print(remove_alias(arg1))
    elif cmd == "sysmonitor":
        sys_monitor()
    elif cmd == "sysinfo":
        sys_info()
    elif cmd == "help":
        display_help()
    elif cmd == "exit":
        print("[process Completed]")
        save_aliases()
        exit(0)
    elif cmd == "edit" and arg1:
        print(edit_file(arg1))  # Call the edit_file function
    else:
        print(f"zsh: command not found: {cmd}")


def main():
    load_aliases()

    # Set up history using the readline module
    readline.set_history_length(100)

    # Load previous history if available
    try:
        with open("history.txt", "r") as history_file:
            for line in history_file:
                readline.add_history(line.strip())
    except FileNotFoundError:
        pass

    while True:
        command = input("Admin@Python-Terminal ~ % ").strip()

        if command:
            # Add the command to the history after execution
            readline.add_history(command)
            # Save the history to a file
            with open("history.txt", "a") as history_file:
                history_file.write(command + "\n")

            execute_command(command)


if __name__ == "__main__":
    main()