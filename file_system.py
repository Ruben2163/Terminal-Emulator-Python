import os
import shutil

# Base directory for the virtual file system
BASE_DIRECTORY = os.path.join(os.getcwd(), "virtual_fs")

# Ensure the base directory exists
if not os.path.exists(BASE_DIRECTORY):
    os.makedirs(BASE_DIRECTORY)


def create_folder(folder_name):
    """Creates a folder in the base directory."""
    folder_path = os.path.join(BASE_DIRECTORY, folder_name)
    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder '{folder_name}' created."
    except Exception as e:
        return f"Error creating folder: {e}"


def create_file(file_name, content=""):
    """Creates a file in the base directory with optional content."""
    file_path = os.path.join(BASE_DIRECTORY, file_name)
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return f"File '{file_name}' created."
    except Exception as e:
        return f"Error creating file: {e}"


def list_contents():
    """Lists the contents of the base directory."""
    try:
        return os.listdir(BASE_DIRECTORY)
    except Exception as e:
        return f"Error listing contents: {e}"


def read_file(file_name):
    """Reads the content of a file."""
    file_path = os.path.join(BASE_DIRECTORY, file_name)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {e}"
    else:
        return f"File '{file_name}' does not exist."


def delete_file(file_name):
    """Deletes a file from the base directory."""
    file_path = os.path.join(BASE_DIRECTORY, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return f"File '{file_name}' deleted."
        except Exception as e:
            return f"Error deleting file: {e}"
    else:
        return f"File '{file_name}' does not exist."


def delete_folder(folder_name):
    """Deletes a folder from the base directory."""
    folder_path = os.path.join(BASE_DIRECTORY, folder_name)
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            return f"Folder '{folder_name}' deleted."
        except Exception as e:
            return f"Error deleting folder: {e}"
    else:
        return f"Folder '{folder_name}' does not exist."
