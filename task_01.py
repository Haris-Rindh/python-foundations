import os  # 1. Import the built-in os module

"""
Directory Scanner Script
This script reads the contents of a specified directory
and filters for JavaScript and React files.
"""

# 2. Define the path. '.' represents the current directory.
directory_path = '.'

# 3. Get all files and folders in the directory as a list
all_contents = os.listdir(directory_path)

# 4. Loop through the list and filter using string methods
for file_name in all_contents:
    
    # Check if the file ends with the desired extensions
    if file_name.endswith('.js') or file_name.endswith('.jsx'):
        print(file_name)