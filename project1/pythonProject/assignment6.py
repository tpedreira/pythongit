# Currency Converter

usd = float(input("Enter the amount in USD: "))

exRate = 0.92

converted = usd * exRate

print("${:,.2f}".format(usd), " USD is equal to ", "£{:,.2f}".format(converted), " EUROS")