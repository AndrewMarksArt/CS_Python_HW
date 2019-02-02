import random
import time


# available weapons for the players to choose from
weapons = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# message for who wins or a tie
player_wins = 'How is this possible!!! You have bested me...'
comp_wins = 'HA HA HA you lose!!! How did you ever think you could beat me!!!'
tie = 'This cannot be... we have tied???!!! We must play again!!!'

# add delay for drama
delay = 0.5


def check_who_wins(player, computer):
    """takes the user as player and comp as computer,
    checks to see who won and prints out the tie, player_wins, or comp_wins message"""

    if player == computer:
        time.sleep(delay)
        print(tie)
    elif player == 'rock' and computer in ['scissors', 'lizard']\
            or player == 'paper' and computer in ['spock', 'rock']\
            or player == 'scissors' and computer in ['paper', 'lizard']\
            or player == 'lizard' and computer in ['spock', 'paper']\
            or player == 'spock' and computer in ['rock', 'scissors']:
        time.sleep(delay)
        print(player_wins)
    else:
        time.sleep(delay)
        print(comp_wins)


# welcome message and ask if the player wants to play
print()
print(' Welcome Puny Human '.center(75, '='))
print('You dare challenge me to a game of Rock, Paper, Scissors, Lizard, Spock!!!')
print()
print('Are you sure you want to play? ... [Y/N]')

# While loop to see if the player said yes or no, or entered something invalid
# Also prints out the rules
while True:
    play = input().upper()
    if play == 'Y':
        print('You fool! You have just sealed your doom!')
        print()
        print('So be it. Here are the rules...')
        print(''.ljust(20, '-'))
        print('Scissors cuts Paper, Paper covers Rock,\n'
              'Rock crushes Lizard, Lizard poisons Spock,\n'
              'Spock smashes Scissors, Scissors decapitates Lizard,\n'
              'Lizard eats Paper, Paper disproves Spock,\n'
              'Spock vaporizes Rock, Rock crushes Scissors.')
        print()
        break
    elif play == 'N':
        print('You Coward!!! There is no turning back now!!! '
              'You entered my domain and so we must battle!!!\n'
              'Now enter Y so I may crush you like a grape!!!')
    else:
        print('I am getting very impatient! You must enter Y or N')


# while loop to keep the game going until the player quits
while True:

    # asks the player to choose a weapon and check to see if it is valid
    while True:
        time.sleep(delay)
        print('Choose your weapon: [rock, paper, scissors, lizard, or spock]')
        user = input().lower()
        if user in weapons:
            break
        else:
            print('please choose a valid weapon: rock, paper, scissors, lizard, or spock')

    # computer chooses a weapon at random
    comp = random.choice(weapons)

    # print out what each player has chosen
    time.sleep(delay)
    print('You chose: ' + user)
    print('The computer chose: ' + comp)

    # Check who wins
    check_who_wins(user, comp)

    # asks the player if they want to play again
    while True:
        print(''.ljust(25, '-'))
        print('How about we play again?... [Y/N]')
        play_again = input().upper()
        if play_again == 'Y':
            print('Fantastic!!! Choose your weapon silly mortal!')
            print()
            break
        elif play_again == 'N':
            print('Your cowardice disgusts me, be gone!!!')
            break
        else:
            print('You must enter Y or N')

    # breaks out of play again loop if player doesn't want to play again and the game is over
    if play_again == 'N':
        break

