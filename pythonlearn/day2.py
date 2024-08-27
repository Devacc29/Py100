user_name = input("what is your name?\n")
len_user_name = len(user_name)

#print(type(user_name))
#print(len_user_name)
#type conversion int to string
conv_user_len = str(len_user_name)
print("Your name has " + conv_user_len + " characters.")

######################################################
####sum of a 2 digit number ###
two_digit_number = input("Type a two digit number:\n")
conv_num = str(two_digit_number)
first_num = int(conv_num[0])
second_num = int(conv_num[1])
print(first_num + second_num)

#####PEMDAS####
#### BMI Calculator #############
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

conv_height = float(height)
conv_weight = float(weight)

bmi_result = conv_weight / (conv_height **2)

print(int(bmi_result))
# ########BMI = WEIGHT/HEIGHT**2(M)#####
######################################################
#round(), f-string()
print(29 / 7)
print(29 // 7)
print(round(29 / 7))
print(round(29 / 7, 2))

height = 166.5
weight = 92.6
job = True

print('your height is: ' + str(height),'\nyour weight is: '+ str(weight), '\nJob holder: ' + str(job))

print(f'Your weight is {weight}\nYour Height is {height}\nJob holder: {job}')

####### Life in Weeks untill 90 ##############
#####You have 12410 days, 1768 weeks, and 408 months left.######
days_in_year = 365
weeks_in_year = 52
months_in_year = 12

user_age = input('Enter your age:\n')
years_left = 90 - int(user_age)
days_left = years_left * days_in_year
weeks_left = years_left * weeks_in_year
months_left = years_left * months_in_year

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left untill 90.')


print(6 + 4 // 2 - (1 * 2))
print(6 + 4 / 2 - (1 * 2))
a = int("5") / int(2.7)
print(a)

###### Tip Calculator #########
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip Calculator!")
bill_amount = float(input("Enter your bill amount: "))
total_people = int(input("How many people you want to split the amount: "))
tip_per = int(input("How much tip % you wnat to give 10 or 12 or 15: "))

tip_cal = bill_amount * tip_per/100
total_bill = bill_amount + tip_cal

calculation = round((total_bill / total_people) ,2)
print(f'Your total Bill per person is: {calculation}')
print(f'Total bill: {total_bill}')