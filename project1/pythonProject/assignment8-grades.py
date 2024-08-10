# Determine the average grade of 3 subjects

mark1 = float(input("Enter your mark for subject 1: "))
mark2 = float(input("Enter your mark for subject 2: "))
mark3 = float(input("Enter your mark for subject 3: "))

grade = (mark1 + mark2 + mark3) / 3

if grade >= 0 and grade <= 100:
    if grade >= 90:
        print("Your grade is an A", round(grade, 2))
    elif grade >= 80 and grade < 90:
        print("Your grade is a B", round(grade, 2))
    elif grade >= 70 and grade < 80:
        print("Your grade is a C", round(grade, 2))
    elif grade >= 60 and grade < 70:
        print("Your grade is a D", round(grade, 2))
    else:
        print("Your grade is an F", round(grade, 2))
else:
    print("Error: Please enter a only numbers between 0 and 100")

