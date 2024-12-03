import os

# Base directory for the virtual file system
BASE_DIRECTORY = os.path.join(os.getcwd(), "virtual_fs")

# Ensure the base directory exists
if not os.path.exists(BASE_DIRECTORY):
    os.makedirs(BASE_DIRECTORY)

# Current working directory starts at BASE_DIRECTORY
current_directory = BASE_DIRECTORY

# Alias storage
ALIAS_FILE = os.path.join(BASE_DIRECTORY, "aliases.txt")
aliases = {}


# File system operations
def create_folder(folder_name):
    folder_path = os.path.join(current_directory, folder_name)
    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder '{folder_name}' created."
    except Exception as e:
        return f"Error creating folder: {e}"


def create_file(file_name, content=""):
    file_path = os.path.join(current_directory, file_name)
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return f"File '{file_name}' created."
    except Exception as e:
        return f"Error creating file: {e}"


def list_contents():
    try:
        return os.listdir(current_directory)
    except Exception as e:
        return f"Error listing contents: {e}"


def read_file(file_name):
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
    global current_directory
    target_directory = os.path.join(current_directory, new_directory)
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        current_directory = target_directory
        return f"Changed directory to '{print_working_directory()}'."
    else:
        return f"Directory '{new_directory}' does not exist."


def go_back():
    global current_directory
    if current_directory != BASE_DIRECTORY:
        current_directory = os.path.dirname(current_directory)
        return f"Moved back to '{print_working_directory()}'."
    else:
        return "You are already at the base directory."


def print_working_directory():
    return "/" + os.path.relpath(current_directory, BASE_DIRECTORY).replace("\\", "/")


# Alias management
def load_aliases():
    global aliases
    try:
        with open(ALIAS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if "=" in line:
                    alias, command = line.split("=", 1)
                    aliases[alias] = command
    except FileNotFoundError:
        pass


def save_aliases():
    with open(ALIAS_FILE, "w") as file:
        for alias, command in aliases.items():
            file.write(f"{alias}={command}\n")


def add_alias(alias, command):
    aliases[alias] = command
    save_aliases()
    return f"Alias added: {alias} -> {command}"


def remove_alias(alias):
    if alias in aliases:
        del aliases[alias]
        save_aliases()
        return f"Alias '{alias}' removed."
    else:
        return f"Alias '{alias}' does not exist."
