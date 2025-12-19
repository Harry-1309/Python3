import random

output = ""
my_list = ["rock" ,"paper", "scissor"]
user_input = input("rock/paper/scissor: ").lower()

if user_input not in my_list:
    print("Invalid input")
    exit()

random_input = random.choice(my_list)
print(random_input)

user_choice = my_list.index(user_input)
computer_choice = my_list.index(random_input)

if user_choice == 0 and computer_choice == 2:
    output = "You win!"
elif user_choice < computer_choice:
    output = "You loose"
elif user_choice == computer_choice:
    output = "Draw"


print(output)



