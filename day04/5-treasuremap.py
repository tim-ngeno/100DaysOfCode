row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\
\nInput a 2-digit coordinate without spaces:\n")

# Get the user input separately
column = int(position[0]) - 1
row = int(position[1]) - 1

# # finding the coordinates
# if column == 0 and row == 0:
#     row1[0] = "X"
# if column == 0 and row == 1:
#     row2[0] = "X"
# if column == 0 and row == 2:
#     row3[0] = "X"
# if column == 1 and row == 0:
#     row1[1] = "X"
# if column == 1 and row == 1:
#     row2[1] = "X"
# if column == 1 and row == 2:
#     row3[1] = "X"
# if column == 2 and row == 0:
#     row1[2] = "X"
# if column == 2 and row == 1:
#     row2[2] = "X"
# if column == 2 and row == 2:
#     row3[2] = "X"

# print(f"{row1}\n{row2}\n{row3}")


# Angela Yu's way

map[row][column] = "X"
print(f"{row1}\n{row2}\n{row3}")
