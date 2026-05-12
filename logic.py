Certainly! Below is an example of how you might implement a Python function named `recursive_file_manager` using recursion to automate the process of managing files in a directory structure.

```python
import os

def recursive_file_manager(directory):
    """
    Recursively manage files in a given directory.
    
    Args:
    - directory (str): The path to the current directory.
    
    Returns:
    - list: A list of tuples containing filenames, file sizes, and modification dates.
    """
    # Initialize an empty list to store files
    files = []

    def traverse(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                path = os.path.join(root, file)
                size = os.path.getsize(path)  # Get the file size
                modified_date = os.path.getmtime(path)  # Get the modification date

                if file not in files:
                    files.append((file, size, modified_date))

    traverse(directory)
    return files

# Example usage: manage a directory structure
directory_path = '/path/to/directory'
files = recursive_file_manager(directory_path)
for filename, size, _ in files:
    print(f"Filename: {filename}, Size: {size} bytes, Modified Date: {_}")
```

### Explanation:

1. **`recursive_file_manager` function**: This function takes a directory path as input and returns a list of tuples containing filenames, file sizes, and modification dates.

2. **`traverse(directory)` inner function**:
    - `os.walk(directory)` generates the directories and files in the specified directory.
    - For each directory, it constructs its full path using `os.path.join`.
    - It then retrieves the size of the current file using `os.path.getsize()`.
    - It also retrieves the modification date using `os.path.getmtime()`.

3. **`files` list**: The function collects all files in the specified directory and their properties.

4. **Example usage**:
    - Replace `/path/to/directory` with the actual path to your directory structure.
    - The script will print out a list of tuples, where each tuple contains the file name, size (in bytes), and modification date.

This is a basic recursive implementation and can be extended or optimized based on specific requirements.