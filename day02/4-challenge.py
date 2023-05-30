# a BMI calculator

print("BMI CALCULATOR\n")
height = input("Enter your height in Metres:  ")
weight = input("Enter your weight in kg: ")

# bmi calculations

# bmi = weight/height^2
bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)

bmi_as_str = str(bmi_as_int)

print("Your BMI is " + bmi_as_str)
