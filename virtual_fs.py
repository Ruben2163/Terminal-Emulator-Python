# Virtual filesystem definition
virtual_fs = {
    "/": {"bin": {}, "boot": {}, "dev": {}, "etc": {}, "home": {}, "lib": {}, "media": {}, "mnt": {}, "opt": {}, "sbin": {}, "srv": {}, "tmp": {}, "usr": {}, "proc": {}},
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
        return
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

def pwd():
    print(current_path)

def mkdir(directory_name):
    """Create a new directory in the current directory."""
    global current_path
    
    # Get the current directory's contents
    current_dir_contents = virtual_fs.get(current_path, {})
    
    # Check if the directory already exists
    if directory_name in current_dir_contents:
        print(f"mkdir: cannot create directory '{directory_name}': File exists")
    else:
        # Create the new directory as an empty dictionary
        current_dir_contents[directory_name] = {}
        print(f"Directory '{directory_name}' created.")

def touch(filename):
    """Create a new empty text file in the current directory."""
    global current_path
    
    # Get the current directory's contents
    current_dir_contents = virtual_fs.get(current_path, {})
    
    # Check if the file already exists
    if filename in current_dir_contents:
        print(f"touch: cannot create file '{filename}': File exists")
    else:
        # Create the new file with empty content (represented as an empty string)
        current_dir_contents[filename] = ""
        print(f"File '{filename}' created.")
