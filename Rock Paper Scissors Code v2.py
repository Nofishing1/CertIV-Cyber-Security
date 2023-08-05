#Display a welcome message to the players
print('Welcome to the Rock Paper Scissors game!')

# Define the possible choices players can choose from
choices = {'rock': {'rock',},
           'paper': {'paper',},
           'scissors': {'scissors'},
           }

# Define a function to determine the winner of a round (CHATGPT)
def get_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 'tie'
    elif player2_choice in choices[player1_choice]:
        return 'player1'
    else:
        return 'player2'
#Get player names
def get_Name(playerNum):
    name = input(f"What is your name Player {playerNum}: ")
    return name

player1 = get_Name(1)
player2 = get_Name(2)
player1_choice = ""
player2_choice = ""

print("Hello", player1)
print("Hello", player2)

while True:
    
    # Ask the players for their choices
    player1_choice = input(f'{player1}, please choose rock, paper or scissors: ')
    while player1_choice not in choices:
        print('Invalid choice, please try again.')
        continue
    player2_choice = input(f'{player2}, please choose rock, paper, or scissors: ')
    while player2_choice not in choices:
        #print('Invalid choice, please try again.')
        
        winner = get_winner(player1_choice, player2_choice)
    print(winner, "wins congratulations")
    a = input("Would you like play again?")
    if a.lower() == "no" or a.lower() == "n":
        break
    