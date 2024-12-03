from file_system import (
    create_folder, create_file, list_contents, read_file, delete_file, 
    delete_folder, rename_item, change_directory, go_back, print_working_directory, 
    load_aliases, save_aliases, add_alias, remove_alias, aliases
)


def display_help():
    commands = """
Available commands:
- mkdir <folder_name>       : Create a folder
- touch <file_name>         : Create a file
- ls                        : List contents of the current directory
- read <file_name>          : Read a file
- rm <file_name>            : Delete a file
- rmdir <folder_name>       : Delete a folder
- mv <old_name> <new_name>  : Rename a file or folder
- cd <folder_name>          : Change directory
- cd ..                     : Move to the parent directory
- pwd                       : Print the current working directory
- alias <name> <command>    : Create an alias
- unalias <name>            : Remove an alias
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
    elif cmd == "read" and arg1:
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
    elif cmd == "help":
        display_help()
    elif cmd == "exit":
        print("[process Completed]")
        save_aliases()
        exit(0)
    else:
        print(f"zsh: command not found: {cmd}")


def main():
    load_aliases()
    while True:
        command = input("Admin@Python-Terminal ~ % ").strip()
        if command:
            execute_command(command)


if __name__ == "__main__":
    main()
