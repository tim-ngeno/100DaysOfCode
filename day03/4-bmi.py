# BMI 2.0

print("This is a BMI calculator 2.0")
height = float(input("Enter your height in Metres:  "))
weight = int(input("Enter your weight in kg: "))

bmi = round(weight / (height * height))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are Underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have Normal Weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are Overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are Obese")
else: 
    print(f"Your BMI is {bmi}, you are Clinically Obese and need to see a doctor.")
