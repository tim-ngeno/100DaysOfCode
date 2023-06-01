# A love calculator!

print("Welcome to the Love Calculator!\n")

my_name = input("What is your name? (Write full names for better scores)\n").lower()
their_name = input("What is their name?\n").lower()

names = my_name + their_name
true = names.count('t') + names.count('r') + names.count('u') + names.count('e')
love = names.count('l') + names.count('o') + names.count('v') + names.count('e')

print(f"True total is: {true}")
print(f"Love total is: {love}")
score = int(str(true) + str(love))

if score  < 10 or score > 90:
    print(f"Your love score is {score}, you go \
    together like mentos and coke")
elif 40 <= score <= 50:
    print(f"Your love score is {score}, you are alright together")
else:
    print(f"Your love score is {score}")
