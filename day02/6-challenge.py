# Tip Calculator

print('Welcome to the Tip Calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

# The math and logic

# tip amount = (tip/100) * total bill
tip_percentage = (tip / 100) * bill
total_amount = tip_percentage + bill

personal_bill = total_amount / people

amount = round(personal_bill, 2)
# amount = "{:.2f}".format(amount) # format to 2 decimal places

print(f"Each person should pay: ${amount}")
