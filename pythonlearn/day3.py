# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120 :
#     print("Go and enjoy the ride")
# else:
#     print("Better luck next time")
    
###################################

# number = int(input("Which number do you want to check? "))
# print(number % 2)
# if number % 2 == 0 :
#     print("Even number")
# else:
#     print("Odd Number")
##########################################

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / (height ** 2))

# if bmi < 18.5:
#     print(f'Your BMI is {bmi}, you are underweight.')
# elif bmi > 18.5 and bmi < 25:
#     print(f'Your BMI is {bmi}, you have a normal weight.')
# elif bmi > 25 and bmi < 30:
#     print(f'Your BMI is {bmi}, you are slightly overweight.')
# elif bmi > 30 and bmi < 35:
#     print(f'Your BMI is {bmi}, you are obese.')
# else:
#     print(f'Your BMI is {bmi}, you are clinically obese.')

##########################################################################

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 != 0:
#         print("Leap year.")   
#     else:
#         if year % 400 == 0:
#             print("Leap year.") 
#         else:
#            print("Not leap year.") 
# else:
#     print("Not leap year.")

#######################################################
# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# total_price = 0
# if size == "S":
#     total_price = 15 
# elif size == "M":
#     total_price = 20
# else:
#     total_price = 25

# if add_pepperoni == "Y" and extra_cheese == "Y":
#     if size == "S":
#         total_price +=3
#         print(f'Your final bill is: ${total_price}.')
#     else:
#         total_price +=4
#         print(f'Your final bill is: ${total_price}.')
# elif add_pepperoni == "Y" and extra_cheese == "N":
#     if size == "S":
#         total_price +=2
#         print(f'Your final bill is: ${total_price}.')
#     else:
#         total_price +=3
#         print(f'Your final bill is: ${total_price}.')
# elif add_pepperoni == "N" and extra_cheese == "Y":
#         total_price +=1
#         print(f'Your final bill is: ${total_price}.')
# else:
#         print(f'Your final bill is: ${total_price}.')



#####################################################

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
true_count = 0
love_count = 0

full_name = name1 + name2

#lower = full_name.lower()

t1 = full_name.count("t")
t2 = full_name.count("r")
t3 = full_name.count("u")
t4 = full_name.count("e")

true_count = t1 + t2 + t3 + t4

l1 = full_name.count("l")
l2 = full_name.count("o")
l3 = full_name.count("v")
l4 = full_name.count("e")

love_count = l1 + l2 + l3 + l4

total_count = int(str(true_count) + str(love_count))
# For Love Scores less than 10 or greater than 90, the message should be:

if total_count < 10 or total_count > 90:
    print(f'Your score is {total_count}, you go together like coke and mentos.')
elif total_count >= 40 and total_count <= 50:
    print(f'Your score is {total_count}, you are alright together.')
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
else:
    print(f'Your score is {total_count}.')
# # "Your score is **y**, you are alright together."
# # Otherwise, the message will just be their score. e.g.:

# # "Your score is **z**."

#################################################
# print('''
#                                                                       ,----,       ,----, 
#                                   ____                              ,/   .`|     ,/   .`| 
#    ,---,           .---.        ,'  , `.           ,---,          ,`   .'  :   ,`   .'  : 
# ,`--.' |          /. ./|     ,-+-,.' _ |          '  .' \       ;    ;     / ;    ;     / 
# |   :  :      .--'.  ' ;  ,-+-. ;   , ||         /  ;    '.   .'___,/    ,'.'___,/    ,'  
# :   |  '     /__./ \ : | ,--.'|'   |  ;|        :  :       \  |    :     | |    :     |   
# |   :  | .--'.  '   \' .|   |  ,', |  ':        :  |   /\   \ ;    |.';  ; ;    |.';  ;   
# '   '  ;/___/ \ |    ' '|   | /  | |  ||        |  :  ' ;.   :`----'  |  | `----'  |  |   
# |   |  |;   \  \;      :'   | :  | :  |,        |  |  ;/  \   \   '   :  ;     '   :  ;   
# '   :  ; \   ;  `      |;   . |  ; |--'         '  :  | \  \ ,'   |   |  '     |   |  '   
# |   |  '  .   \    .\  ;|   : |  | ,            |  |  '  '--'     '   :  |     '   :  |   
# '   :  |   \   \   ' \ ||   : '  |/             |  :  :           ;   |.'      ;   |.'    
# ;   |.'     :   '  |--" ;   | |`-'              |  | ,'           '---'        '---'      
# '---'        \   \ ;    |   ;/                  `--''                                     
#               '---"     '---'                                                             
                                                                                          
#       ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
