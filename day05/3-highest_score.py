student_scores = input("Input a list of student scores: ").split()
# split() converts input to list (delimiter is a space by default)

# convert the input back to integers
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)
# 45 76 67 34 78 58 89 81 90 99

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is {highest_score}")
