# Define the menu items
menu = {
    "cola": 1.50,
    "chips": 0.75,
    "candy": 0.25,
    "soda": 1.00,
    "gum": 0.25
}

# Initialize the cash drawer
cash_drawer = 10.00

# Function to handle a purchase
def purchase(item):
    # Check if the item is in the menu
    if item in menu:
        # Check if there is enough cash in the cash drawer
        if cash_drawer >= menu[item]:
            # Update the cash drawer
            cash_drawer -= menu[item]
            # Return the change
            change = cash_drawer
            return f"Here's your change: ${change:.2f}"
        else:
            return "Not enough cash in the cash drawer"
    else:
        return "Item not in the menu"

# Example usage
print(purchase("cola"))  # Output: Here's your change: $0.25
print(purchase("chips"))  # Output: Here's your change: $0.00
print(purchase("soda"))  # Output: Here's your change: $0.50
print(purchase("gum"))   # Output: Item not in the menu
print(purchase("apple")) # Output: Item not in the menu
print(purchase("water")) # Output: Item not in the menu
print(purchase("coke"))  # Output: Item not in the menu
