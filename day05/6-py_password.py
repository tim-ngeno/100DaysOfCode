import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^&', '*', '+', '?', ',', '/']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password = ""
for x in range(0, nr_letters):
    password += random.choice(letters)

for number in range(0, nr_numbers):
    password += random.choice(numbers)

for symbol in range(0, nr_symbols):
    password += random.choice(symbols)

print(password)


# Shuffling the password
password_list = list(password)
random.shuffle(password_list)
new_password = ""
for char in password_list:
    new_password += char

print(f"Your strong password is: {new_password}")
