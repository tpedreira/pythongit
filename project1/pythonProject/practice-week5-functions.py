#Calculating the total cost for a purchase

#Define a function to calculate cost with tax and quantity

def totalcostpurchase(price, quantity, tax_rate):
    if price < 0 or quantity < 0 or tax_rate < 0:
        return "Invalid input: Price, Quantity, and Tax Rate must be a non-negative number"
    subtotal = price * quantity
    total_cost = subtotal * (1 + tax_rate / 100)
    return total_cost

def main():
    price = float(input("Enter the price per item: "))
    quantity = float(input("Enter the quantity of items: "))
    tax_rate = float(input("Enter the tax rate (in percentage): "))

    total_cost = totalcostpurchase(price, quantity, tax_rate)

    if isinstance(total_cost, str):
        print(total_cost)
    else:
        print(f"The total cost including tax is: ${total_cost:.2f}")

main()

