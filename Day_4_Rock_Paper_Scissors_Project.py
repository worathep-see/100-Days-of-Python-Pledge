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
game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(f"You chose! {game_image[user_choice]}")

import random
computer_choice = random.randint(0, 2)
print(f"Computer chose! {game_image[computer_choice]}")

if user_choice == computer_choice:
    print("You choose again!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You typed an invalid number. You lose!")