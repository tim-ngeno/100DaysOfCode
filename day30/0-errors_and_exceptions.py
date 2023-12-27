# Handling Errors and Exceptions

try:
    # Try to open a file that doesn't exist => FileNotFoundError
    file = open("file.txt", "r")
    a_dict = {"Key": "Value"}
    print(a_dict["WrongKey"])   # KeyError

# Catch the FileNotFoundError
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("something")

# Catch KeyError
except KeyError as e:
    print(f'The key {e} does not exist')


# Do something with the file if it existed
else:
    content = file.read()
    print(content)

# This line will work regardless of the errors and exceptions above
finally:
    file.close()
