# Provide feedback to the user based on their BMI category

weight = float(input("Enter your weight in KG: "))

height = float(input("Enter your height in Meters: "))

bmi = weight / (height ** 2)

print("Your Body Mass Index or BMI is ", str(bmi))