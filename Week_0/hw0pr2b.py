
# this is an adventure game that asks the user a series of questions
# the outcome will depend on which options the user chooses
# if the user chooses the same direction twice in a row the payer will lose

import time


# Here is the Game Over text
def game_over():
    print('\nAll light quickly fades to a darkness and you here\n'
          'a terrible voice ...\n')
    time.sleep(2)
    print('Flesh so fine, so fine to tear... and all fades to black\n')
    time.sleep(2)
    print('You awake in the room you first woke in but something is different\n'
          'Ragnar sadly smiles at you before fading away and you realize that \n'
          'you perished in the dungeon and now your soul is trapped to help the next\n'
          'adventurer... you only hope Ragnar is finally at rest but you have a feeling\n'
          'his soul was lost to a terrible fat and you hope that you wont suffer the same.\n\n')
    time.sleep(4)
    print("""
      ________                           ________                       ._._._.
     /  _____/_____    _____   ____      \_____  \___  __ ___________   | | | |
    /   \  ___\__  \  /     \_/ __ \      /   |   \  \/ // __ \_  __ \  | | | |
    \    \_\  \/ __ \|  Y Y  \  ___/     /    |    \   /\  ___/|  | \/   \|\|\|
     \______  (____  /__|_|  /\___  >    \_______  /\_/  \___  >__|      ______
            \/     \/      \/     \/             \/          \/          \/\/\/

           .                                                      .
            .n                   .                 .                  n.
      .   .dP                  dP                   9b                 9b.    .
     4    qXb         .       dX                     Xb       .        dXp     t
    dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
    9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
     9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
      `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
        `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
            ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                            )b.  .dbo.dP'`v'`9b.odb.  .dX(
                          ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                         dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                        dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                        9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                         `'      9XXXXXX(   )XXXXXXP      `'
                                  XXXX X.`v'.X XXXX
                                  XP^X'`b   d'`X^XX
                                  X. 9  `   '  P )X
                                  `b  `       '  d'
                                   `             '     """)


# initialize variables
room = 'main'
trade = ''
direction = ''
weapon = ''
attack = ''
win = False

# This while loop keeps the player in the game until there is a game over
while True:
    # Title Message and game beginning
    print()
    print(''.ljust(60, '|'))
    print("""
        ________                                             
        \______ \  __ __  ____    ____   ____  ____   ____   
         |    |  \|  |  \/    \  / ___\ / __ \/  _ \ /    \  
         |    `   \  |  /   |  \/ /_/  \  ___(_ |_| )   |  \ 
        /_______  /____/|___|  /\___  / \___  /____/|___|  / 
                \/           \//_____/      \/           \/  
         ___________                                         
         \_   _____/  _______ ____  _____  ______    ____        
          |    __)_  /  ____// ___\ \__  \ \____ \  / __ \       
          |        \ \___ \ \  \___  / __ \ |  |_>\ \  ___/      
         /_______  / ____  / \___  / ____  /|   __/  \___ /      
                 \/      \/      \/      \/ |__|        \/        

            """)
    print('By: Andrew Marks\n')
    print(''.ljust(60, '|'))
    print()

    """ --------------------        THIS IS THE MAIN ROOM       -------------------- """

    # Main room, ask for player name, into guide, ask which weapon
    print('\nYou wake up in a strange place, the floor is hard stone, covered in\n'
          'dirt, and stained with something that looks like blood.\n'
          'You hear something behind you and turn around to find someone hiding\n'
          'in the shadows.\n'
          '...\n')
    time.sleep(3)
    print('A man approaches, almost gliding across floor...\n')
    time.sleep(1)
    player_name = input('Stranger: Hello traveler... what is your name? \n')
    time.sleep(1)
    print('Greetings ' + player_name + ' my name is Ragnar and I will be your guide\n')
    time.sleep(2)
    print('\nMany years ago I too was summoned to this strange place\n'
          'but after perishing in the dungeon my soul was trapped\n'
          'only by helping you escape will I be free to rest.\n')
    time.sleep(2)
    print('\nTo aid you on your journey I can give you one of two items\n'
          'Choose carefully as one of these may save your life\n'
          ' --> The Mystic Sword of Valhalla (sword)\n'
          ' --> The Holy Torch of Dagda (torch)\n'
          'Which will you choose?\n')
    print('enter either "sword" or "torch"\n')
    weapon = input().lower()

    # check to see if the input is valid, if not ask again until there is a valid response
    while True:
        if weapon not in ['sword', 'torch']:
            print('Please enter a valid weapon: sword or torch')
            weapon = input()
        else:
            break

    if weapon == 'sword':
        print('\nMuch honor to you ' + player_name + ' you have chosen wisely!\n'
                                                     'May Odin and Thor watch over you!')
    else:
        print('\nVery wise, beware of the shadow here and keep hold onto\n'
              'the Torch of Dagda NEVER GIVE IT UP or you will be doomed!\n')

    print('And let me give you one last warning.\n'
          'As you make your way through the dungeon NEVER pick the same way twice in a row!\n')
    print('\nAs you hold your new ' + weapon + ' you realize two doors have appeared\n')
    print('\nTo the LEFT a door bangs shut fiercely and you hear bloodcurdling screams\n'
          'To the RIGHT a door slowly creaks open revealing pitch black darkness\n')
    print('\nWhich way will you go?\n')
    print('Enter "right" or "left":  ')
    direction = input().lower()

    # check to see if the direction is valid and ask again if not
    while True:
        if direction == 'right' or direction == 'left':
            break
        else:
            print('Please enter a valid direction: right or left')
            direction = input().lower()

    """ --------------------        THIS IS THE DARKNESS ROOM        -------------------- """

    # This starts the path down the right side of the dungeon
    if direction == 'right' and room == 'main':
        room = 'darkness'
        print('\nyou enter the darkness and hear a whispering rasping voice\n')
        print('Flesh so fine, so fine to tear, to gnash the skin; skin to strip, \n'
              ' so nice, so red the drops that fall; blood so red, so red, so sweet; \n'
              'sweet screams, pretty screams, singing screams, scream your song, \n'
              'sing your screams...')
        print('\nWho is there? The voice asks... another traveler? Welcome ' + player_name)
        print('What do you have there? That is a powerful ' + weapon)
        print('How about we trade? ... \n'
              'I hold the the key to your salvation and that ' + weapon + ' looks very nice.\n')
        print('So how about it your ' + ' for my key? [Y/N]')
        trade = input().upper()

        # check to see if the input is valid
        while True:
            if trade == 'Y' or trade == 'N':
                break
            else:
                print('Please enter a valid answer: Y or N')
                trade = input().upper()

        # if trade is Y and weapon is torch or trade is N and weapon is sword the player loses
        # all others leads to the shadow leaving and player getting a key
        if trade == 'Y' and weapon == 'sword':
            print('Wise choice adventurer... \n'
                  'You hand over the Sword of Valhalla and receive the key of salvation\n'
                  'The blackness seems to fade and the darkness lifts...\n'
                  'you shiver as the voice recedes chanting "sweet screams, pretty screams..."\n'
                  'Looking around you see two door ways.\n\n')
        elif trade == 'Y' and weapon == 'torch':
            print('Yesss! The Holy Torch of Dagda is finally mine!!!\n'
                  'This was the only thing that could stop me...\n'
                  'You look so very sweet... SCREAM FOR ME!!!\n\n')
            print('The shadow attacks enveloping you...')
            game_over()
            break
        elif trade == 'N' and weapon == 'sword':
            print('You Fool!!! The Shadow screams as it attacks\n'
                  'you try to fight back but your sword is useless...\n')
            game_over()
            break
        elif trade == 'N' and weapon == 'torch':
            print('The darkness screams: How is this possible!!! \n'
                  'the torch of Dagda glows with an intense light \n'
                  'which consumes the shadow burning it away\n'
                  'a key falls to the ground and you pick it up\n\n')

    """ --------------------        THIS IS THE MONSTER ROOM       -------------------- """

    if direction == 'left' and room == 'main':
        room = 'monster'
        print('You enter the room and see a man on the ground who looks hurt\n'
              'however he seems to shimmer slightly and looks unnatural... \n'
              'the man asks you for HELP\n')
        print('Do you help the man or attack him? [attack / help]')
        attack = input().lower()

        # check to see if the input is valid
        while True:
            if attack == 'attack' or attack == 'help':
                break
            else:
                print('Please enter a valid answer: attack or help')

        # if trade is Y and weapon is torch or trade is N and weapon is sword the player loses
        # all others leads to the shadow leaving and player getting a key
        if attack == 'attack' and weapon == 'sword':
            print('The man shimmers and starts to transform into a horrible beast...\n'
                  'lunging forward you attack with the sword of Valhalla\n'
                  'you slice the beast in half and it fades away leaving a key on the floor.\n\n')
        elif attack == 'attack' and weapon == 'torch':
            print('The man shimmers and starts to transform into a horrible beast...\n'
                  'you raise the Holly Torch of Dagda and the flame grows into a blinding light\n'
                  'the monstrous beast is burned away and leaves behind a key on the floor.\n\n')
        elif attack == 'help' and weapon == 'sword':
            print('You move forward to help the man to his feet but suddenly the man starts to transform...\n'
                  'the man turns into a horrible beast that lunges at you...')
            game_over()
            break
        else:
            print('You move forward to help the man to his feet but suddenly the man starts to transform...\n'
                  'the man turns into a horrible beast that lunges at you...')
            game_over()
            break

    """ --------------------        MOVING ON TO CHEST ROOM FROM DARKNESS OR MONSTER       -------------------- """

    if room == 'darkness':
        print('To the RIGHT: a room filled with the sounds of joy and laughter\n'
              'and the smells of something delicious!\n'
              'To the LEFT: a dimly lit room with a table in the middle\n'
              'on the table is a single candle casting strange shadows across the room.\n')
        print('Which way do you go? [right or left]')
        direction = input().lower()
    elif room == 'monster':
        print('To the LEFT: a room filled with the sounds of joy and laughter\n'
              'and the smells of something delicious!\n'
              'To the RIGHT: a dimly lit room with a table in the middle\n'
              'on the table is a single candle casting strange shadows across the room.\n')
        print('Which way do you go? [right or left]')
        direction = input().lower()

    while True:
        if direction == 'right' or direction == 'left':
            break
        else:
            print('Please enter a valid direction: right or left')
            direction = input().lower()

    if room == 'darkness' and direction == 'right' or room == 'monster' and direction == 'left':
        game_over()
        break
    else:
        room = 'chest room'

    """ --------------------        THIS IS THE CHEST ROOM ROOM       -------------------- """

    # enter room from darkness room
    if direction == 'left':
        print('You enter the poorly lit room and approach the table\n'
              'you find two chests on the table and some how know the key \n'
              'will unlock one of the chests... But which one?\n\n')
        print('Which chest do you unlock? The one to the RIGHT or the LEFT?\n')
        direction = input().lower()

        while True:
            if direction == 'right' or direction == 'left':
                break
            else:
                print('Please enter a valid direction: right or left\n')
                direction = input().lower()

        if direction == 'left':
            print('The chest springs to life and bites your hand...\n')
            game_over()
            break
        else:
            print('The chest clicks open but suddenly vanishes in a flash of light\n'
                  'the room is suddenly filled with a brilliant light revealing\n'
                  'two door ways...\n\n')
            print('To the RIGHT: a room filled with the sounds of joy and laughter\n'
                  'and the smells of something delicious!\n'
                  'To the LEFT: a door creaks open but you cant make out what lays \n'
                  'on the other side but hear howling winds...\n\n')
            print('Which door do you take? The "right" or the "left"?\n')
            direction = input().lower()

            while True:
                if direction == 'right' or direction == 'left':
                    break
                else:
                    print('Please enter a valid direction: right or left\n')
                    direction = input().lower()

            if direction == 'right':
                game_over()
                break
            else:
                print('You step through the door and find you self in the middle of the woods\n'
                      'you realize that you have escaped the dungeon!\n'
                      'turning around you see Ragnar smiling at you.\n\n')
                print('Thank You adventurer!!! You have set me free and I will be eternally grateful\n'
                      'this is where my journey ends but you must carry on...\n\n')
                print('You have survived the dungeon but now the BLACK FORREST waits, you steady \n'
                      'you steady your nerves and move into the clearing ahead.\n\n')
                print('TO BE CONTINUED!...\n')
                win = True

    # enter room from monster room last direction was right
    else:
        print('You enter the poorly lit room and approach the table\n'
              'you find two chests on the table and some how know the key \n'
              'will unlock one of the chests... But which one?\n\n')
        print('Which chest do you unlock? The one to the RIGHT or the LEFT?\n')
        direction = input().lower()

        while True:
            if direction == 'right' or direction == 'left':
                break
            else:
                print('Please enter a valid direction: right or left\n')
                direction = input().lower()

        if direction == 'right':
            print('The chest springs to life and bites your hand...\n')
            game_over()
            break
        else:
            print('The chest clicks open but suddenly vanishes in a flash of light\n'
                  'the room is suddenly filled with a brilliant light revealing\n'
                  'two door ways...\n\n')
            print('To the LEFT: a room filled with the sounds of joy and laughter\n'
                  'and the smells of something delicious!\n'
                  'To the RIGHT: a door creaks open but you cant make out what lays \n'
                  'on the other side but hear howling winds...\n\n')
            print('Which door do you take? The "right" or the "left"?\n')
            direction = input().lower()

            while True:
                if direction == 'right' or direction == 'left':
                    break
                else:
                    print('Please enter a valid direction: right or left\n')
                    direction = input().lower()

            if direction == 'left':
                game_over()
                break
            else:
                print('You step through the door and find you self in the middle of the woods\n'
                      'you realize that you have escaped the dungeon!\n'
                      'turning around you see Ragnar smiling at you.\n\n')
                print('Thank You adventurer!!! You have set me free and I will be eternally grateful\n'
                      'this is where my journey ends but you must carry on...\n\n')
                print('You have survived the dungeon but now the BLACK FORREST waits, you steady \n'
                      'you steady your nerves and move into the clearing ahead.\n\n')
                print('TO BE CONTINUED!...\n')
                win = True

    if win is True:
        break

