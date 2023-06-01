# Leap Year
# print("LEAP YEAR CHECKER")
year = int(input("Type in a year you want to check: \n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a leap year")

# ##### Method 2 #####

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
