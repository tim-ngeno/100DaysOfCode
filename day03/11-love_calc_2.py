# LOVE CALCULATOR
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name?\n").lower()


true = str(name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e') + name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e'))

love = str(name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e') + name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e'))

love_score = true + love

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos")
else:
    print(f"Your love score is {love_score}, you're alright together.")