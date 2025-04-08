import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#method 1
user_password=""

for l in range(0, nr_letters):
    user_password += random.choice(letters)
for s in range(0, nr_symbols):
    user_password += random.choice(symbols)
for n in range(0, nr_numbers):
    user_password += random.choice(numbers)

print(user_password)


#method2

user_pass= []

for l in range(0, nr_letters):
    user_pass.append(random.choice(letters))
for s in range(0, nr_symbols):
    user_pass.append(random.choice(symbols))
for n in range(0, nr_numbers):
    user_pass.append(random.choice(numbers))

print(user_pass)
random.shuffle(user_pass)
print(user_pass)

us_pass = ""
for p in user_pass:
    us_pass += p
print(f'your password is: {us_pass}')

