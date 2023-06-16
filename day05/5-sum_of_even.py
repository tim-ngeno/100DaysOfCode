# ADDING EVEN NUMBERS BETWEEN 1 AND 100, INCLUDING 1 AND 100

total = 1
for number in range(0, 101, 2):
    total += number
print(f"Sum of even numbers: {total}")

odd = 0
for number in range(1, 100, 2):
    odd += number
print(f"Sum of odd numbers: {odd}")
