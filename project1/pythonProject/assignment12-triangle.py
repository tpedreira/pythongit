#

def print_triangle(rows, char):
    for i in range(1, rows + 1):  # Outer loop for rows
        for j in range(i):  # Inner loop for printing characters
            print(char, end="")
        print()  # Move to the next line after each row


def tri():
    while True:
        try:
            rows = int(input("Enter the number of rows for the triangle: "))
            if rows > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    char = input("Enter the character to use for the pattern: ")

    print_triangle(rows, char)


