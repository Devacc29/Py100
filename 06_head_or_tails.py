import random

user_choice =input("Choose your side H for Head or T for Tails\n").lower()

rand_h_t = random.randint(0,1)
# print(rand_h_t)

if rand_h_t == 0 and user_choice == "t":
    print("It's Tails. You Won")
elif rand_h_t == 1 and user_choice == "t":
    print("It's Heads. You Lose")
elif rand_h_t == 0 and user_choice == "h":
    print("It's Tails. You Lose")
else:
    print("It's Heads. You Won")

# rand_h_t = random.randint(0,1)
# # print(rand_h_t)
# if rand_h_t == 0:
#     print("Tails")
# else:
#     print("Heads")