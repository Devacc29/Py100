import random
# import day4_check
# ## random number between range
# random_integer = random.randint(29,73)
# print(random_integer)
# ## random number between 0 and 1
# random_float = random.random()
# print(random_float)
# #import other py files and use it 
# print(day4_check.deva)

####################
### Heads or tails
# random_num = random.randint(0,1)
# print(f'{random_num}')
# if random_num == 1:
#     print("Heads")
# else:
#     print("Tails")

###############################

### data structure : Lists

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# print(states_of_america[0])
# states_of_america[2] = "Deva"

# # print(states_of_america)
# print(states_of_america[-1])
# #print(states_of_america[2:])

# states_of_america.pop()
# states_of_america.append("Chikky")
# print(states_of_america)

#########################
#####Banker Roulette

# print("Welcome to Banker Roulette!!!")
# list_of_names = input("Enter the names followed by comma and space, i.e., a, b, c: ")
# #  split the strings into lists using a delimiter
# names = list_of_names.split(", ")
# print(names)
# lof_name = len(names)
# print(f'length of names: {lof_name}')
# bill_payer = random.randint(0,lof_name - 1)
# print(f'random number generated in names: {bill_payer}')
# print(f'{names[bill_payer]} is going to buy the meal today!')
# ## using random.choice() to select random string
# bill_player2 = random.choice(names)
# print(bill_player2)
#########################

#### Treasure Map
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(map)
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# split_position1 = list(position)
# #print(split_position1)
# x = int(split_position1[0])
# y = int(split_position1[1])
# # split_position = position.split()
# # print(split_position)
# map[y-1][x-1] = "X"
# #print(map)
# print(f"{row1}\n{row2}\n{row3}")

######################################################

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

### rock beats scissor
### scissor beats paper
### paper beats rock
print("Welcome to Rock Paper Scissors!!!")
user_choice = input("Enter your choice:\n")
x = [rock, paper, scissors]
random_choice = random.choice(x)

if user_choice == "rock" and random_choice == "scissors":
    print(f'{rock}')
    print(random_choice)
    print("You Win!")
elif user_choice == "scissors" and random_choice == "scissors":
    print(user_choice)
    print(random_choice)
    print("Draw!")
elif user_choice == "paper" and random_choice == "paper":
    print(user_choice)
    print(random_choice)
    print("Draw!")
elif user_choice == "rock" and random_choice == "rock":
    print(user_choice)
    print(random_choice)
    print("Draw!")
elif user_choice == "paper" and random_choice == "scissors":
    print(user_choice)
    print(random_choice)
    print("You Lose!")
elif user_choice == "scissors" and random_choice == "rock":
    print(user_choice)
    print(random_choice)
    print("You Lose!")
elif user_choice == "rock" and random_choice == "paper":
    print(user_choice)
    print(random_choice)
    print("You Lose!")
elif user_choice == "paper" and random_choice == "rock":
    print(user_choice)
    print(random_choice)
    print("You Win!")
else:
    print(user_choice)
    print(random_choice)
    print("You Win!")