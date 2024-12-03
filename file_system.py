import os


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

aliases = {}
def find_alias(cmd, arg1, arg2):
    cmd = ""
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
    elif cmd == "alias" and arg1 and arg2:
        alias(arg1, arg2)
    else:
        print(f"zsh: command not found: {cmd}")

# Base directory for the virtual file system
BASE_DIRECTORY = os.path.join(os.getcwd(), "virtual_fs")

# Ensure the base directory exists
if not os.path.exists(BASE_DIRECTORY):
    os.makedirs(BASE_DIRECTORY)

# Current working directory starts at BASE_DIRECTORY
current_directory = BASE_DIRECTORY


def create_folder(folder_name):
    """Creates a folder in the current directory."""
    folder_path = os.path.join(current_directory, folder_name)
    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder '{folder_name}' created."
    except Exception as e:
        return f"Error creating folder: {e}"


def create_file(file_name, content=""):
    """Creates a file in the current directory with optional content."""
    file_path = os.path.join(current_directory, file_name)
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return f"File '{file_name}' created."
    except Exception as e:
        return f"Error creating file: {e}"


def list_contents():
    """Lists the contents of the current directory."""
    try:
        return os.listdir(current_directory)
    except Exception as e:
        return f"Error listing contents: {e}"


def read_file(file_name):
    """Reads the content of a file."""
    file_path = os.path.join(current_directory, file_name)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {e}"
    else:
        return f"File '{file_name}' does not exist."


def delete_file(file_name):
    """Deletes a file from the current directory."""
    file_path = os.path.join(current_directory, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return f"File '{file_name}' deleted."
        except Exception as e:
            return f"Error deleting file: {e}"
    else:
        return f"File '{file_name}' does not exist."


def delete_folder(folder_name):
    """Deletes a folder from the current directory."""
    folder_path = os.path.join(current_directory, folder_name)
    if os.path.exists(folder_path):
        try:
            os.rmdir(folder_path)
            return f"Folder '{folder_name}' deleted."
        except Exception as e:
            return f"Error deleting folder: {e}"
    else:
        return f"Folder '{folder_name}' does not exist."


def rename_item(old_name, new_name):
    """Renames a file or folder in the current directory."""
    old_path = os.path.join(current_directory, old_name)
    new_path = os.path.join(current_directory, new_name)
    if os.path.exists(old_path):
        try:
            os.rename(old_path, new_path)
            return f"'{old_name}' has been renamed to '{new_name}'."
        except Exception as e:
            return f"Error renaming '{old_name}': {e}"
    else:
        return f"'{old_name}' does not exist."


def change_directory(new_directory):
    """Changes the current directory."""
    global current_directory
    target_directory = os.path.join(current_directory, new_directory)
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        current_directory = target_directory
        return f"Changed directory to '{print_working_directory()}'."
    else:
        return f"Directory '{new_directory}' does not exist."


def go_back():
    """Navigates to the parent directory."""
    global current_directory
    if current_directory != BASE_DIRECTORY:
        current_directory = os.path.dirname(current_directory)
        return f"Moved back to '{print_working_directory()}'."
    else:
        return "You are already at the base directory."


def print_working_directory():
    """Returns the current working directory, relative to BASE_DIRECTORY."""
    return "/" + os.path.relpath(current_directory, BASE_DIRECTORY).replace("\\", "/")

def alias(alias, command):
    aliases[alias] = command
    print(f"Alias added: {alias} -> {command}")

def search_alias(alias, arg1, arg2):
    if alias in aliases:
        if arg1 and arg2:
            find_alias(alias, arg1, arg2)
        elif arg1:
            arg2 = ""
            find_alias(alias, arg1, arg2)
        else:
            arg1 = ""
            arg2 = ""
            find_alias(alias, arg1, arg2)
    else:
        print(f"zsh: command not found: {alias}")