print("Input a number to check if it is odd or even")

number = int(input("Type your number here: "))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


# DIVISBLE BY THREE

three = int(input("Type a number to check if divisible by 3: \n"))

if three % 3 == 0:
    print(f"{three} is divisible by 3")
else:
    print(f"{three} is not divisible by 3?")
