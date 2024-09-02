

# Creating a list of student grades

# grades = [78, 45, 89, 55, 67, 48, 92, 38, 75, 61]
#
# # Calculating the average grade using a for loop
#
# total = 0
#
# for grade in grades:
#     total += grade
#
# average = total / len(grades)

# Determine the number of students who passed and failed using a while loop

# passed = 0
# failed = 0
# index = 0
#
# while index < len(grades):
#     if grades[index] >= 60:
#         passed += 1
#     else:
#         failed += 1
#     index += 1
#
# # Output the results
#
# print("Average Grade: ", average)
# print("Number of students passed: ", passed)
# print("Number of students failed: ", failed)
#
#
#
# print(average)

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 // num2

def ctof(celcius):
    return (celcius * 9/5) + 32

print(ctof(25))

print(add(5, 3))
print(subtract(10, 4))
print(divide(8, 2))