# Working with Files in Python

This project improves on the snake game by adding a persistent high score.

It provides an overview of working with files in Python, covering concepts such as reading from and writing to files, methods for opening and closing files, and understanding file paths.

## Files in Python

Files are a fundamental way to store and retrieve data in most programming languages, including Python. Python provides built-in functions and methods to interact with files.


### Opening and Closing Files

To work with a file, you need to open it first. Python's `open()` function is used for this purpose. It takes two arguments: the file name (or path) and the mode in which the file should be opened (read, write, append, etc.).

```python
# Opening a file in read mode
file = open('example.txt', 'r')

# Opening a file in write mode
file = open('output.txt', 'w')

# Opening a file in append mode
file = open('log.txt', 'a')

# It's important to close the file when you're done
file.close()
```

### Reading from Files

Once a file is open, you can read its contents. Python offers methods like `read()`, `readline()`, and `readlines()`.

```python
# Reading the entire content of a file
content = file.read()

# Reading one line at a time
line = file.readline()

# Reading all lines and storing them in a list
lines = file.readlines()
```

### Writing to Files

To write data to a file, you need to open it in write or append mode and then use methods like `write()`.

```python
# Opening a file in write mode
file = open('output.txt', 'w')

# Writing data to the file
file.write("Hello, world!\n")
file.write("This is a new line.")
```

### File Paths

File paths specify the location of a file on the file system. There are two types of file paths: absolute and relative.

- **Absolute Paths**: These paths start from the root directory (e.g., `/home/user/documents/file.txt`).

- **Relative Paths**: These paths are relative to the current working directory of your script (e.g., `../images/pic.jpg`).

Python's `os.path` module provides methods to manipulate paths.

```python
import os

# Joining paths safely
file_path = os.path.join("folder", "file.txt")

# Getting the absolute path
absolute_path = os.path.abspath("file.txt")

# Checking if a path exists
exists = os.path.exists("folder")
```

Remember that when working with files, exceptions can occur (e.g., if the file doesn't exist). Using `try` and `except` blocks for error handling is a good practice.

```python
try:
    file = open('nonexistent.txt', 'r')
except FileNotFoundError:
    print("File not found!")
```

Always close the file after you're done using it to free up system resources.

```python
file.close()
```



## Opening and Closing Files Using `with`

Python's `with` statement provides a cleaner and safer way to open and close files. It automatically takes care of closing the file once the block of code is exited, even if an exception occurs.

```python
# Opening a file in read mode using 'with'
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Opening a file in write mode using 'with'
with open('output.txt', 'w') as file:
    file.write("Hello, world!")

# Opening a file in append mode using 'with'
with open('log.txt', 'a') as file:
    file.write("An event occurred.\n")
```

### Reading from Files

Within the `with` block, you can read the file's contents using methods like `read()`, `readline()`, and `readlines()`.

```python
# Reading one line at a time
with open('example.txt', 'r') as file:
    line = file.readline()
    print(line)

# Reading all lines and storing them in a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
```

### Writing to Files

To write data to a file within a `with` block, use methods like `write()`.

```python
# Writing data to a file using 'with'
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")
```

### File Paths

File paths specify the location of a file on the file system. The `os.path` module provides methods to manipulate paths.

```python
import os

# Joining paths safely
file_path = os.path.join("folder", "file.txt")

# Getting the absolute path
absolute_path = os.path.abspath("file.txt")

# Checking if a path exists
exists = os.path.exists("folder")
```

When using the `with` statement, you don't need to manually close the file; Python handles it for you. This helps prevent resource leaks and makes your code more concise and readable.

---