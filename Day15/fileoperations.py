"""
Day 15 - File Operations Module
Reusable functions for file and directory management operations.
This module provides convenient wrapper functions for common file/directory tasks.
This module covers:
- Writing and appending to files
- Reading files with different modes
- File rename and delete operations
- Directory creation and management
- Current working directory handling
"""

import os
import shutil


# Helper function that writes write to file.
def write_to_file(file_path, content):
    """
    Write content to a file.
    Creates new file if it doesn't exist, overwrites if it does.

    Args:
        file_path: Path to the file
        content: Content to write to file
    """
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}")


# Helper function that appends append to file.
def append_to_file(file_path, content):
    """
    Append content to an existing file.
    Adds content without overwriting existing data.

    Args:
        file_path: Path to the file
        content: Content to append to file
    """
    with open(file_path, 'a') as file:
        file.write(content)
    print(f"Content appended to {file_path}")


# Helper function that reads read file.
def read_file(file_path, mode="all"):
    """
    Read file with flexible modes.

    Args:
        file_path: Path to the file
        mode: Read mode - "all" (entire file), "line" (single line), or "lines" (list of lines)

    Returns:
        File content based on mode selected

    Raises:
        ValueError: If invalid mode is specified
    """
    with open(file_path, 'r') as file:
        if mode == "all":
            return file.read()         # Read entire file
        elif mode == "line":
            return file.readline()     # Read single line
        elif mode == "lines":
            return file.readlines()    # Read all lines as list
        else:
            raise ValueError("Invalid mode. Use 'all', 'line', or 'lines'.")


# Helper function that renames rename file.
def rename_file(source, target):
    """
    Rename a file from source name to target name.

    Args:
        source: Current file path
        target: New file path
    """
    os.rename(source, target)
    print(f"File renamed from {source} to {target}")


# Helper function that deletes delete file.
def delete_file(file_path):
    """
    Delete a file if it exists.

    Args:
        file_path: Path to the file to delete
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted")
    else:
        print(f"File {file_path} does not exist")


# Helper function that creates create directory.
def create_directory(dir_path):
    """
    Create a new directory.

    Args:
        dir_path: Path for the new directory
    """
    os.mkdir(dir_path)
    print(f"Directory {dir_path} created")


# Helper function that checks check directory exists.
def check_directory_exists(dir_path):
    """
    Check if a directory exists.

    Args:
        dir_path: Path to check

    Returns:
        True if directory exists, False otherwise
    """
    return os.path.exists(dir_path)


# Helper function that renames rename directory.
def rename_directory(source, target):
    """
    Rename a directory from source name to target name.

    Args:
        source: Current directory path
        target: New directory path
    """
    os.rename(source, target)
    print(f"Directory renamed from {source} to {target}")


# Function demonstrating the remove directory concept.
def remove_directory(dir_path, force=False):
    """
    Remove a directory.

    Args:
        dir_path: Path to directory to remove
        force: If True, removes directory even if not empty
               If False, only removes empty directories
    """
    if force:
        shutil.rmtree(dir_path)  # Removes directory and all contents
    else:
        os.rmdir(dir_path)       # Only removes if directory is empty
    print(f"Directory {dir_path} removed")


# Helper function that gets get current working directory.
def get_current_working_directory():
    """
    Get the current working directory path.

    Returns:
        Absolute path of current working directory
    """
    return os.getcwd()
