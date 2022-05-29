#rock paper sciscors

import random

choices = {
    0 : 'rock',
    1 : 'paper',
    2 : 'scissors'
}

while (True):
    number = random.randint(0, 2)
    pc_choice = choices.get(number)
        
    print('Rock Paper Sciscors')
    player_choice = input("Input your choice: ").lower()
    print(f'The computer chose {pc_choice}')
    print(f'number: {number}')
    
    if (pc_choice == 'rock'):
        if (player_choice == 'paper'):
            print('You win.')
        if (player_choice == 'rock'):
            print('It is a tie.')
        if (player_choice == 'scissors'):
            print('You lose.')
    
    if (pc_choice == 'paper'):
        if (player_choice == 'paper'):
            print('It is a tie.')
        if (player_choice == 'rock'):
            print('You lose.')
        if (player_choice == 'scissors'):
            print('You win.')
    
    if (pc_choice == 'scissors'):
        if (player_choice == 'paper'):
            print('You lose.')
        if (player_choice == 'rock'):
            print('You win.')
        if (player_choice == 'scissors'):
            print('It is a tie.')
            
    again = input('Play again? Enter y/n: ')
    if again == 'n':
        break
