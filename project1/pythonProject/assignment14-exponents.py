# Exponents My version before class

base = int(input("Please input the base: "))
exponent = int(input("Please input the power: "))
def power(base, exponent):
        return print(base ** exponent)

power(base, exponent)

#Class Versions

def power(base, exponent):
        return base ** exponent

#print(power(2, 3))

def power2(base, exponent):
        return pow(base, exponent)

#print(power2(5, 0))

# def power3(base, exponent):
#         if exponent < 0:
#                 base = 1 / base
#                 exponent = -exponent
#         result = 1
#         for _ in range(exponent):
#                 result *= base
#         return result
# power3(2, 3)
