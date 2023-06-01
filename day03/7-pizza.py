# pIZZA PRICE CALCULATOR

print("Welcome to Python Pizza Deliveries!\n")

size = input("What size pizza do you want? S, M, or L? ").upper()
pepperoni = input("Do you want pepperoni? Y or N? ").upper()
extra_cheese = input("Do you want extra cheese? Y or N? ").upper()

bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
        bill += 1

print(f"Your bill is ${bill}")

######## Other method ##########
#if size == "S":
#    bill += 15
#if size == "M":
#    bill += 20
#else:
#    bill += 25

#if pepperoni == "Y":
 #   if size == "S":
  #      bill += 2
   # else:
    #    bill += 3
#
#if extra_cheese == "Y":
 #   bill += 1

#print(f"Your final amount is ${bill}")
