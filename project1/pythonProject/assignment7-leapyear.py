# Determine if a year is a leap year

# year = int(input("Enter the year to determine if it is a leap year or not: "))
#
# def leapyear(year):
#     if year % 400 == 0:
#         return year, "is a leap year!"
#     elif year % 100 == 0:
#         return year, "is not a leap year."
#     elif year % 4 == 0:
#         return year, "is a leap year!"
#     return False

y = int(input("enter your year : "))

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) :

    print("It is a leap year")

else :

    print("It is not a leap year")

