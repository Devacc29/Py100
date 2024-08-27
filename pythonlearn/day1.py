#print() function
print("Welcome to python World!")

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# #double quotes in single quotes/ single quotes in double 
print("print('what to print')")
print('print("what to print")')

# print("Day 1 - Python Print Function \nThe function is declared like this:\nprint('what to print')")

# ###############################################################
print("Welcome to python World!" + "Deva")

print("Welcome to python World!" + " "+ "Deva")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

##################################################################
#input(), len()

X = (input("What is your name? "))
l = len(X)
print(l)

print(len(input("What is your name? ")))

##############Band name generator####################

#1. Create a greeting for your program.
print("Welcome to Band Name Generator!")
#2. Ask the user for the city that they grew up in.
city_name = input("Which City you grep up?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What is your Pet name?\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + " "+ pet_name
#5. Make sure the input cursor shows on a new line:
print('Your Band name: ' + band_name)
