# Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.

character = input("Please enter a character: ")

rows = int(input("Enter the amount of rows: "))

while True:
    if len(character) == 1:
        break
    else:
        character = input("Please enter only 1 character: ")
while True:
    if rows >= 1:
        break
    else:
        rows = int(input("Please enter an integer greater than or equal to 1: "))

for row in range(0, rows):
    for column in range(0, row + 1):
        print(character, end=' ')
    print()







































# def print_triangle(rows, char):
#     for i in range(1, rows + 1):  # Outer loop for rows
#         for j in range(i):  # Inner loop for printing characters
#             print(char, end="")
#         print()  # Move to the next line after each row
#
#
# def tri():
#     while True:
#         try:
#             rows = int(input("Enter the number of rows for the triangle: "))
#             if rows > 0:
#                 break
#             else:
#                 print("Please enter a positive integer.")
#         except ValueError:
#             print("Invalid input. Please enter a positive integer.")
#
#     char = input("Enter the character to use for the pattern: ")
#
#     print_triangle(rows, char)


