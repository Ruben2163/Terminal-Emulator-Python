# **Python Terminal**

## **Features**
- **File System Management**:
  - Create folders and files (`mkdir`, `touch`).
  - List directory contents (`ls`).
  - Read and delete files (`read`, `rm`).
  - Rename files or folders (`mv`).
  - Navigate directories (`cd`, `cd ..`, `pwd`).
  - Delete folders (`rmdir`).
- **Aliases**:
  - Define custom aliases for frequently used commands (`alias`).
  - Remove aliases (`unalias`).
  - Save and load aliases automatically.
- **Help Menu**:
  - View all available commands using the `help` command.
- **Persistence**:
  - Virtual file system and aliases persist across sessions.

---

## **Installation**

### **Prerequisites**
- Python 3.6 or higher.

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/Ruben2163/Python-Terminal.git
1. Run Main.py:
   ```bash
   python3 main.py
---
## **Basic commands**

| Commands|Usage|
| -------|------------------ |
| mkdir <folder_name>|Create a folder.|
|touch <file_name>|	Create a file.|
|ls	|List contents of the current directory.|
|read <file_name>	|Display the content of a file.|
|rm <file_name>	|Delete a file.|
|rmdir <folder_name>	|Delete a folder.|
|mv <old_name> <new_name>	|Rename a file or folder.|
|cd <folder_name>	|Navigate to a directory.|
|cd ..	|Go to the parent directory.|
|pwd	|Print the current working directory.|
|help	|Display the help menu.|
|exit	|Exit the terminal.|
|alias <name> <command>	|Create a shortcut for a command.|
|unalias <name>	|Remove an alias.|

---

## **Project Structure**

```plaintext
Python-Terminal/
│
├── main.py            # Main script for the terminal interface
├── file_system.py     # Handles file system and alias logic
├── virtual_fs/        # Virtual file system root directory
└── README.md          # Documentation (this file)
```
---

## **Contributing**

Contributions are welcome! If you have suggestions for improvements or new features, feel free to:

1.    Fork the repository.
2.    Create a new branch.
3.    Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.





