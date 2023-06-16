print("Enter a space delimited value of integers for students' heights")
students_heights = input().split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

print(f"List of students' heights: {students_heights}")

total_height = 0
for height in students_heights:
    total_height += int(height)
print(f"Sum total: {total_height}")

students = 0
for student in students_heights:
    students += 1
print(f"Total students: {students}")
average_height = round(total_height / students)

print(f"{average_height} is the average height")
