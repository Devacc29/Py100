# fruits = ['apple', 'grapes', 'orange']
# for a in fruits:
#     print(a)
#     print (a + " pie")
# print(a)
# # print(fruits)

################################
#average height using for loop
#string to list as user input will be string
# student_heights = input("Input a list of student heights ").split()
# #coverting lists of stings into list of int
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])


# total_height = 0 
# for height in student_heights:
#     total_height += height

   
# no_of_students = 0
# for n in student_heights:
#     no_of_students += 1
   
# average_height = round(total_height / no_of_students)
# print(average_height)

##########################
#highest score using for loop
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for highest in student_scores:
#     if highest > highest_score:
#         highest_score = highest
# print(f'The highest score in the class is: {highest_score}')

#print(sum(range(1,101)))

# total = 0
# for n in range(2,102,2):
#     total += n
# print(total)
####### fizz buzz interview question###########

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0: 
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)
#####   Password generator #######
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for l in range(1,nr_letters+1):
    password += random.choice(letters)
# print(password)
for s in range(1,nr_symbols+1):
    password += random.choice(symbols)
# print(password)
for n in range(1,nr_numbers+1):
    password += random.choice(numbers)
print(password)
random.shuffle(password)
# print(password)
new_pass = ''
for p in password:
    new_pass += p
print(f'Your password is:{new_pass}')
