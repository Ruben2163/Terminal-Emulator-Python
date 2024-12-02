<<<<<<< Updated upstream
from file_system.virtual_fs import *  # Import everything from virtual_fs.py

run = True
=======
from file_system import *


>>>>>>> Stashed changes

def get_multiline_input(existing_content=""):
    """Function to get multiline input from the user, showing existing content."""
    print("Enter the content for the file (Type 'DONE' on a new line to finish):")
    
    # Show existing content if available
    if existing_content:
        print("\nCurrent content of the file:")
        print(existing_content)
        print("\nYou can now modify the content. Continue editing...\n")

<<<<<<< Updated upstream
    content = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":  # If the user types DONE, stop collecting input
            break
        content.append(line)
    return "\n".join(content)  # Join the content with newlines between each line
=======
def main():
    while True:
        command = input("Admin@Python-Terminal ~ % ").strip()
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
        elif cmd == "cat" and arg:
            print(cat(arg))
        elif cmd == "rm" and arg:
            print(delete_file(arg))
        elif cmd == "rmdir" and arg:
            print(delete_folder(arg))
        elif cmd == "cd" and arg:
            print(change_directory(arg))
        elif cmd == "cd ..":
            print(go_back())
        elif cmd == "pwd":
            print(print_working_directory())
        elif cmd == "help":
            display_help()
        elif cmd == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print(f"zsh: command not found: {command}")
>>>>>>> Stashed changes

while run:
    user_input = input(f"Admin@Python-terminal {current_path} % ")

    # Handle empty input case
    if user_input.strip() == "":  # If the user input is empty or just spaces
        continue  # Simply skip to the next loop iteration

    command = user_input.split(maxsplit=1)

    match command:
        case ["cd"]:
            cd()
        case ["cd", path]:
            cd(path)
        case ["ls"]:
            ls()
        case ["cat", filename]:
            cat(filename)
        case ["edit", filename] if len(command) > 1:  # Check if the filename is provided
            existing_content = cat(filename)
            new_content = get_multiline_input(existing_content)
            edit(filename, new_content)
            print(f"File '{filename}' has been updated.")
        case ["quit"]:
            run = False
        case ["pwd"]:
            pwd()
        case ["mkdir", dirname]:
            mkdir(dirname)
        case ["touch", filename]:
            touch(filename)
        case _:
            print(f"zsh: command not found: {user_input}")
