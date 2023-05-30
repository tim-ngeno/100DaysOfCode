# Calculate how much time you have before you're 90

print("Let's calculate how much time you have before you turn 90")
age = input("What is your current age? ")

days = (90 - int(age)) * 365
weeks = (90 - int(age)) * 52
months = (90 - int(age)) * 12

message = (f"You have {days} days, {weeks} weeks, and {months} months before you turn 90")

print(message)
