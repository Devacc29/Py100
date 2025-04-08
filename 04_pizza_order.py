print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
pizza_price = 0
if size == "S":
    pizza_price = 15
    if pepperoni == "Y":
        pizza_price += 2
elif size == "M":
    pizza_price = 20
    if pepperoni == "Y":
        pizza_price += 3
else:
    pizza_price = 25
    if pepperoni == "Y":
        pizza_price += 3
if extra_cheese == "Y":
    pizza_price += 1
    print(f"Your final bill is: ${pizza_price}.")
else:
    print(f"Your final bill is: ${pizza_price}.")
