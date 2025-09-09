
# request to the user their name and thei starbucks order. 
# See what is the temperature (H, C), type of coffee(C, M, L) and size(S,M,L) of the order and give a final price

#variables
name = str(input("What is your name?"))
starbucks_order = input("Hello " + name + ". What is your starbucks order? Please let me know the temperature (H, C), type of coffee (Cappucino, Espresso, Latte) and size (S,M,L) of the order.")

temperature, coffee_type, size = starbucks_order.split()

#operations if, else, while, for

available_temperature = ["H","C"]
available_coffee_type = ["Cappucino", "Espresso", "Latte"]
available_size = ["S", "M", "L"]

if temperature not in available_temperature:
    print("Sorry, your desired temperature isn't available.")
elif coffee_type not in available_coffee_type:
    print("Sorry, your desired coffee type isn't available.")
elif size not in available_size:
    print("Sorry, your desired coffee size isn't available.")
else:
    if temperature == "H":
        temp_price = 1.00
    else: temp_price = 0.50

    if coffee_type == "Cappucino":
        coffee_price = 5.00
    elif coffee_type == "Espresso":
        coffee_price = 4.00
    else: coffee_price = 3.00

    if size == "S":
        size_price = 0.50
    elif size == "M":
        size_price = 1.00
    else: size_price = 2.00

    total_price = temp_price + coffee_price + size_price
    #output
    print("The order has been confirmed.")
    print("Your total price is : $", total_price)