import random  # This will allow the computer to randomly generate a choice.

possible_actions = ["rock", "paper", "scissors"]

user_action = input("Enter a choice (rock, paper, scissors): ").lower()  # Prompts the user for input and converts it to lowercase
computer_action = random.choice(possible_actions)

print("You chose: {}".format(user_action))
print("The computer chose: {}".format(computer_action))

if user_action not in possible_actions:  # This will cover if a user gives an option not listed.
    print("Invalid choice.")
elif user_action == computer_action:
    print('It is a tie!')
elif user_action == 'rock' and computer_action == 'paper':
    print("Paper beats Rock. You lose!")
elif user_action == 'rock' and computer_action == 'scissors':
    print("Rock beats Scissors. You win!")
elif user_action == 'paper' and computer_action == 'rock':
    print('Paper beats Rock. You win!')
elif user_action == 'paper' and computer_action == 'scissors':
    print("Scissors beats paper. You lose!")
elif user_action == 'scissors' and computer_action == 'paper':
    print("Scissors beats Paper. You win!")
elif user_action == 'scissors' and computer_action == 'rock':
    print("Rock beats Scissors. You lose!")
