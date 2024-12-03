from file_system import *

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
- help                      : Show this help menu
- exit                      : Exit the program
"""
    print(commands)


def main():
    while True:
        command = input("Admin@Python-Terminal ~ % ").strip()
        if not command:
            continue

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
            if isinstance(contents, list):
                print("\n".join(contents) if contents else "Directory is empty.")
            else:
                print(contents)
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
        elif cmd == "back":
            print(go_back())
        elif cmd == "pwd":
            print(print_working_directory())
        elif cmd == "help":
            display_help()
        elif cmd == "exit":
            print("[process Completed]")
            break
        elif cmd == "alias" and arg1 and arg2:
            alias(arg1, arg2)
        elif cmd:
            if arg1:
                arg2 = ""
                search_alias(cmd, arg1, arg2)
            else:
                arg1 = ""
                arg2 = ""
                search_alias(cmd, arg1, arg2)
        else:
            if arg1 and arg2:
                search_alias(arg1, arg2)

if __name__ == "__main__":
    main()
