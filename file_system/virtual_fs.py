# Virtual filesystem definition
virtual_fs = {
    "/": {"home": {}, "var": {}, "tmp": {}},
    "/home": {"user": {}},
    "/home/user": {"file1.txt": "HelloWorld!", "documents": {}},
    "/var": {},
    "/tmp": {},
}

current_path = "/"

def cd(path=None):
    """Change the current directory in the virtual filesystem."""
    global current_path
    if not path or path.strip() == "":
        print(current_path)
    elif path == "..":
        if current_path != "/":
            current_path = "/".join(current_path.rstrip("/").split("/")[:-1])
            if current_path == "":
                current_path = "/"
    elif path in virtual_fs.get(current_path, {}):
        if isinstance(virtual_fs[current_path][path], dict):
            current_path = current_path.rstrip("/") + "/" + path
    else:
        print(f"cd: no such file or directory: {path}")


def ls():
    """List the contents of the current directory."""
    contents = virtual_fs.get(current_path, {})
    for item in contents:
        print(item)

def cat(filename):
    """Simulate opening and reading a file."""
    global current_path
    current_dir_contents = virtual_fs.get(current_path, {})
    
    if filename in current_dir_contents:
        if isinstance(current_dir_contents[filename], str):
            print(current_dir_contents[filename])
        else:
            print(f"cat: {filename}: Is a directory")
    else:
        print(f"cat: {filename}: No such file or directory")

def edit(filename, new_content):
    """Simulate editing the content of a file."""
    global current_path
    current_dir_contents = virtual_fs.get(current_path, {})
    
    if filename in current_dir_contents:
        if isinstance(current_dir_contents[filename], str):
            # Update the content of the file
            current_dir_contents[filename] = new_content
            print(f"File '{filename}' has been updated.")
        else:
            print(f"edit: {filename}: Is a directory")
    else:
        print(f"edit: {filename}: No such file or directory")


def print_tree(path, indent=""):
    """Recursively print the directory tree, listing files and subdirectories."""
    # Get contents of the current path
    contents = virtual_fs.get(path, {})

    # Iterate through the contents of the directory
    for item, content in contents.items():
        # If the content is a dictionary, it's a directory, so print its name and recurse into it
        if isinstance(content, dict):
            print(f"{indent}{item}/")  # Print directory with a slash at the end
            print_tree(f"{path}/{item}", indent + "  ")  # Recurse into the directory
        else:
            # If it's not a dictionary, it's a file, so print its name
            print(f"{indent}{item}")  # Print file name

def tree():
    """Print the tree of the current directory starting from the root."""
    print_tree(current_path)
