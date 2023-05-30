# two_digit_number = input("Type a two digit number: ")

# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# other method

number = input("Type in any two digit number: ")

# subscripting using [] to get index of value
first_digit = int(number[0]) # convert 'number' to int
second_digit = int(number[1])

result = first_digit + second_digit
print(result)
