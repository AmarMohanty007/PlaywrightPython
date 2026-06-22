"""
Day 15 - File Handling in Python
Comprehensive demonstration of file and directory operations.
This module covers:
- Creating/Writing files
- Appending data to files
- Reading data from files (read, readline, readlines)
- File operations (rename, delete)
- Directory/Folder operations (create, check, rename, delete)
- File modes: 'r' (read), 'w' (write), 'a' (append)
"""

# Example 1: Create/Write a file

# Approach 1: Basic file operations
# file = open("d:\\Automation\\myfile.txt", 'w')  # 'w' = write mode
# file.write("Welcome to python \n File handling")
# file.close()


# Approach 2: Using 'with' statement (recommended - auto closes file)
# with open("C:\\Automation\\automationFiles\\myfile.txt", 'w') as file:
#     file.write("Welcome to python \n File handling")
#     # file automatically closes when exiting 'with' block



# Example 2: Appending data into file
# 'a' = append mode (adds data without overwriting)
# file = open("d:\\Automation\\myfile.txt", 'a')
# file.write("\n This line is appended...")
# file.close()


# Example 3: Reading data from text file
# 'r' = read mode
# read()     - reads entire file content
# readline() - reads single line
# readlines() - reads all lines into list format

# file = open("d:\\Automation\\myfile.txt", 'r')
# content = file.read()      # Read all content
# # content = file.readline()   # Read single line
# # content = file.readlines()  # Read all lines as list
# print(content)
# file.close()


# Example 4: Renaming a file
# import os
# os.rename("d:\\Automation\\myfile.txt", "d:\\Automation\\myfile1.txt")
# print("File renamed...")


# Example 5: Deleting a file
# import os
#
# file = "d:\\Automation\\myfile1.txt"
#
# if os.path.exists(file):  # Check if file exists
#     os.remove(file)        # Remove/delete the file
# else:
#     print("File does not exist")


# Example 6: Creating a directory/folder
# import os
# os.mkdir("C:\\Automation\\automationFiles\\mydir")  # Create new directory
# print("Directory created..")


# Example 7: Check if directory exists
# import os
# mydir = "C:\\Automation\\automationFiles\\mydir"
#
# if os.path.exists(mydir):
#     print("Directory exists")
# else:
#     print("Directory does not exist")


# Example 8: Rename a directory
# import os
#
# os.rename("C:\\Automation\\automationFiles\\mydir",
#           "C:\\Automation\\automationFiles\\mydir1")
# print("Directory renamed...")


# Example 9: Remove/Delete a directory
# import os
# import shutil
#
# os.rmdir("C:\\Automation\\automationFiles\\mydir123")  # For empty directories
# # shutil.rmtree("C:\\Automation\\automationFiles\\mydir123")  # For non-empty directories


# Example 10: Get the current working directory
# import os
# print(os.getcwd())  # Returns the current working directory path
