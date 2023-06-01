# NESTED IF/ELSE STATEMENTS

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Yay..you can ride in the rollercoaster!")
    age = int(input("What is your age? \n"))
    if age < 12:
        print("The price for kids is just $5")
    elif age <= 18:
        print("Please avail $7 to the cashier")
    else:
        print("The adult price is $12. Growing up is no fun..")
else:
    print("Sorry, you need to grow taller to ride in the rollercoaster")
