# MULTIPLE IFS IN SUCCESSION
# they indicate that all the statements have to be executed
#
# using if...else statements on the other hand,
# shows that only one statement will be executed

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("Yay..you can ride in the rollercoaster!")
    age = int(input("What is your age?  "))
    if age < 12:
        bill = 5
        print("Child tickets are just $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("The adult price is $12. Growing up is no fun..")

    wants_pic = input("Do you want a photo taken? Type Y or N: ")
    if wants_pic == "Y" or "y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you need to grow taller to ride in the rollercoaster")
