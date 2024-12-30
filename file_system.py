import os
import psutil
import platform
import pyfiglet
import time
from datetime import timedelta

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
    """Create a new folder in the current directory."""
    folder_path = os.path.join(current_directory, folder_name)
    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder '{folder_name}' created."
    except Exception as e:
        return f"Error creating folder: {e}"


def create_file(file_name, content=""):
    """Create a new file in the current directory."""
    file_path = os.path.join(current_directory, file_name)
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return f"File '{file_name}' created."
    except Exception as e:
        return f"Error creating file: {e}"


def list_contents():
    """List the contents of the current directory."""
    try:
        return os.listdir(current_directory)
    except Exception as e:
        return f"Error listing contents: {e}"


def read_file(file_name):
    """Read the contents of a file."""
    file_path = os.path.join(current_directory, file_name)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {e}"
    return f"File '{file_name}' does not exist."


def delete_file(file_name):
    """Delete a file in the current directory."""
    file_path = os.path.join(current_directory, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return f"File '{file_name}' deleted."
        except Exception as e:
            return f"Error deleting file: {e}"
    return f"File '{file_name}' does not exist."


def delete_folder(folder_name):
    """Delete a folder in the current directory."""
    folder_path = os.path.join(current_directory, folder_name)
    if os.path.exists(folder_path):
        try:
            os.rmdir(folder_path)
            return f"Folder '{folder_name}' deleted."
        except Exception as e:
            return f"Error deleting folder: {e}"
    return f"Folder '{folder_name}' does not exist."


def rename_item(old_name, new_name):
    """Rename a file or folder."""
    old_path = os.path.join(current_directory, old_name)
    new_path = os.path.join(current_directory, new_name)
    if os.path.exists(old_path):
        try:
            os.rename(old_path, new_path)
            return f"'{old_name}' has been renamed to '{new_name}'."
        except Exception as e:
            return f"Error renaming '{old_name}': {e}"
    return f"'{old_name}' does not exist."


def change_directory(new_directory):
    """Change the current working directory."""
    global current_directory
    target_directory = os.path.join(current_directory, new_directory)
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        current_directory = target_directory
        return f"Changed directory to '{print_working_directory()}'."
    return f"Directory '{new_directory}' does not exist."


def go_back():
    """Move to the parent directory."""
    global current_directory
    if current_directory != BASE_DIRECTORY:
        current_directory = os.path.dirname(current_directory)
        return f"Moved back to '{print_working_directory()}'."
    return "You are already at the base directory."


def print_working_directory():
    """Print the current working directory."""
    return "/" + os.path.relpath(current_directory, BASE_DIRECTORY).replace("\\", "/")


# Alias management
def load_aliases():
    """Load aliases from a file."""
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
    """Save aliases to a file."""
    with open(ALIAS_FILE, "w") as file:
        for alias, command in aliases.items():
            file.write(f"{alias}={command}\n")


def add_alias(alias, command):
    """Add a new alias."""
    aliases[alias] = command
    save_aliases()
    return f"Alias added: {alias} -> {command}"


def remove_alias(alias):
    """Remove an alias."""
    if alias in aliases:
        del aliases[alias]
        save_aliases()
        return f"Alias '{alias}' removed."
    return f"Alias '{alias}' does not exist."


def edit_file(file_name):
    """Edit an existing file, clearing its contents first."""
    file_path = os.path.join(current_directory, file_name)

    if not os.path.exists(file_path):
        return f"File '{file_name}' does not exist."

    with open(file_path, "w"):
        pass  # Clear the file content

    print(f"File '{file_name}' has been cleared. You can now edit it.")

    content = []
    while True:
        user_input = input("Enter text to add (or 'exit' to save and exit): ")
        if user_input.lower() == "exit":
            break
        content.append(user_input + "\n")

    with open(file_path, "w") as file:
        file.writelines(content)

    return f"File '{file_name}' has been updated."


# System monitoring functions
def sys_monitor():
    """Display system memory and CPU usage."""
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    print(f"Total Memory: {mem.total / (1024 * 1024):.2f}MB")
    print(f"Used Memory: {mem.used / (1024 * 1024):.2f}MB")
    print(f"Free Memory: {mem.free / (1024 * 1024):.2f}MB")
    print(f"CPU Usage: {cpu}%")


def get_uptime():
    """Get the system uptime."""
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return str(timedelta(seconds=uptime_seconds))


def get_memory():
    """Get total and used memory in GB."""
    mem = psutil.virtual_memory()
    total_mem = mem.total / (1024 ** 3)
    used_mem = mem.used / (1024 ** 3)
    return total_mem, used_mem


def get_cpu():
    """Get CPU core count and frequency."""
    cpu_count = psutil.cpu_count(logical=False)
    cpu_freq = psutil.cpu_freq().current
    return cpu_count, cpu_freq


def get_disk_usage():
    """Get total and used disk space in GB."""
    disk = psutil.disk_usage("/")
    total_disk = disk.total / (1024 ** 3)
    used_disk = disk.used / (1024 ** 3)
    return total_disk, used_disk


def ascii_text(text):
    """Convert text to ASCII art."""
    return pyfiglet.figlet_format(text, font="slant")


def sys_info():
    """Display system information."""
    os_arch = platform.architecture()[0]
    uptime = get_uptime()
    total_mem, used_mem = get_memory()
    cpu_count, cpu_freq = get_cpu()

    print(ascii_text("System Info"))
    print(f"\nOS: Python-terminal 2.3.0 ({os_arch})")
    print(f"Host: Admin")
    print(f"Kernel: 2.3.0")
    print(f"Uptime: {uptime}")
    print(f"Shell: Python-Terminal Shell")
    print(f"CPU: {cpu_count} cores, {cpu_freq:.2f} MHz")
    print(f"RAM: {used_mem:.2f}GB / {total_mem:.2f}GB")