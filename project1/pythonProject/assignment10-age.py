# Enter an age - Adult, Minor, Senior

age = int(input("What is your age? "))

if age < 18:
    print("You are a minor!")
elif age >= 18 and age <= 65:
    print("You are an Adult!")
elif age > 65:
    print("You are a Senior Citizen!")
