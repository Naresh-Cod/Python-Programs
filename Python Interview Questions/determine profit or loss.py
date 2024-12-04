# Function to determine profit or loss
# Get input from the user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
    result = selling_price - cost_price
    print(f"Profit: {result}")
elif selling_price < cost_price:
    result = cost_price - selling_price
    print(f"Loss: {result}")
else:
    print("No profit, no loss: 0")
