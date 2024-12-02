from file_system.virtual_fs import *  # Import everything from virtual_fs.py

run = True

def get_multiline_input(existing_content=""):
    """Function to get multiline input from the user, showing existing content."""
    print("Enter the content for the file (Type 'DONE' on a new line to finish):")
    
    # Show existing content if available
    if existing_content:
        print("\nCurrent content of the file:")
        print(existing_content)
        print("\nYou can now modify the content. Continue editing...\n")

    content = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":  # If the user types DONE, stop collecting input
            break
        content.append(line)
    return "\n".join(content)  # Join the content with newlines between each line

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
            # Read the current content of the file
            existing_content = cat(filename)
            
            # Get the new content for the file by prompting the user
            new_content = get_multiline_input(existing_content)
            
            # Update the file's content with the new content
            edit(filename, new_content)
            print(f"File '{filename}' has been updated.")
        case ["quit"]:
            run = False
        case ["tree"]:
            tree()
        case _:
            print(f"zsh: command not found: {user_input}")
