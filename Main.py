from file_system import create_folder, create_file, list_contents, read_file, delete_file, delete_folder

def display_help():
    """Displays available commands."""
    commands = """
Available commands:
- mkdir <folder_name>       : Create a folder
- touch <file_name>         : Create a file
- ls                        : List contents of the virtual directory
- read <file_name>          : Read a file
- rm <file_name>            : Delete a file
- rmdir <folder_name>       : Delete a folder
- help                      : Show this help menu
- exit                      : Exit the program
"""
    print(commands)


def main():
    """Command interpreter for the file system."""
    print("Welcome to the Python Terminal Virtual File System!")
    display_help()

    while True:
        command = input("\n>>> ").strip()
        if not command:
            continue

        parts = command.split(" ", 1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None

        if cmd == "mkdir" and arg:
            print(create_folder(arg))
        elif cmd == "touch" and arg:
            print(create_file(arg))
        elif cmd == "ls":
            contents = list_contents()
            if isinstance(contents, list):
                print("\n".join(contents) if contents else "Directory is empty.")
            else:
                print(contents)
        elif cmd == "read" and arg:
            print(read_file(arg))
        elif cmd == "rm" and arg:
            print(delete_file(arg))
        elif cmd == "rmdir" and arg:
            print(delete_folder(arg))
        elif cmd == "help":
            display_help()
        elif cmd == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
