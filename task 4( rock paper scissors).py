import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def validate_choice(choice):
    return choice.lower() in ['rock', 'paper', 'scissors']

print("Welcome to Rock, Paper, Scissors!")
print("Enter your choice: rock, paper, or scissors")
player_wins = 0
computer_wins = 0
games_played = 0
    
while True:
    player_choice = input("Your choice: ")
    if not validate_choice(player_choice):
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        continue
        
    games_played += 1
    computer_choice = get_computer_choice()
    print("Computer's choice:", computer_choice)
        
    result = determine_winner(player_choice.lower(), computer_choice)
    print("Result:", result)
        
    if result == "You win!":
        player_wins += 1
    elif result == "Computer wins!":
        computer_wins += 1
        
    print("Games played:", games_played)
    print("Your wins:", player_wins)
    print("Computer wins:", computer_wins)    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

