# Enter an age - Adult, Minor, Senior

# MY WORK BEFORE THURSDAYS CLASS
# age = int(input("What is your age? "))
#
# if age < 18:
#     print("You are a minor!")
# elif age >= 18 and age <= 65:
#     print("You are an Adult!")
# elif age > 65:
#     print("You are a Senior Citizen!")

age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)

    if age > 0:
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")
        else:
            print("Senior Citizen")
    else:
        print("Error: Age must be a positive number")
else:
    print("Error: Invalid input. Please enter a positive number")