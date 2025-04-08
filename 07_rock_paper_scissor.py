import random

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
'''Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.'''
print("Welcome to Rock Paper Scissor")
user_choice = str(input("Choose your choice r for rock p for paper and s for scissor\n")).lower()
# if user_choice == "r" or user_choice == "p" or user_choice == "s":
if user_choice in ["r","p","s"]:
    com_choice=random.randint(0,2)
    if com_choice == 0:
        if user_choice == "r":
            print("Both choose Rock. Match Draw")
            print(rock)
        elif user_choice == "p":
            print(f'You choose \n {paper}')
            print(f'Computer choose \n {rock}')
            print("You Won")
        else:
            print(f'Computer choose \n {rock}')
            print(f'You choose \n {scissors}')
            print("You Lose")
    elif com_choice == 1:
        if user_choice == "r":
            print(f'You choose \n {rock}')
            print(f'Computer choose \n {paper}')
            print("You Lose")
        elif user_choice == "p":
            print("Both choose Paper. Match Draw")
            print(paper)
        else:
            print(f'You choose \n {scissors}')
            print(f'Computer choose \n {paper}')
            print("You Won")
    else:
        if user_choice == "r":
            print(f'You choose \n {rock}')
            print(f'Computer choose \n {scissors}')
            print("You Win")
        elif user_choice == "p":
            print(f'You choose \n {paper}')
            print(f'Computer choose \n {scissors}')
            print("You Lose")
        else:
            print("Both choose scissors. Match Draw")
            print(scissors)
else:
    print("Choose between only r or p or s. Try Again!")