#rate = interest_rate / 100

principal = int(input("What is the principal amount?: "))

interest_rate = int(input("What is the interest rate? (without % symbol): "))

time = int(input("How many years?: "))

simple_interest = (principal * interest_rate * time) / 100

print("The simple interest is: ", simple_interest)
#vfdv