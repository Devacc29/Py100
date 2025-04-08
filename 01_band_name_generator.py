"""
Band Name Generator
"""

print("Hello! Welcome to Band Name Generator")
print("*************************************")
city = input("Enter your city name that you grew up: \n")
pet = input("What is your pet name?\n")
bandname = city + pet
length_of_bandname = len(bandname)
# print("your Band Name is: " + bandname )
# print("Your Band name has "+ str(len(bandname)) + " characters")
print(f"Your Band name is: {bandname} and has {length_of_bandname} characters")
