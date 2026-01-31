import random

easy_level = 10
hard_level = 5
def set_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
       return easy_level
    else:
        return hard_level

def check_answer(user_guess, actual_answer, turns):
    if user_guess < actual_answer:
        print(f"Too low.")
        return turns - 1
    elif user_guess > actual_answer:
        print(f"Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")
        return turns

def game():
    logo = r"""
      / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
     / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
    / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
    \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
    """
    print(logo)
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a Number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_level()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose.")
            return
        elif guess !=  answer:
            print(f"Guess again")

game()
