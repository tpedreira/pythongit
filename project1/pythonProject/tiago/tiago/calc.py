

while True:
    try:
        principal = int(input("What is the principal amount?: "))
        break
    except ValueError:
        print("Invalid Input")

while True:
    try:
        interest_rate = int(input("What is the interest rate? (without % symbol): "))
        break
    except ValueError:
        print("Invalid input")

while True:
    try:
        time = int(input("How many years?: "))
        break
    except ValueError:
        print("Invalid input")

#rate = interest_rate / 100

simple_interest = (principal * interest_rate * time) / 100

print("The simple interest is: ", simple_interest)
