import time


def game_over():
    print('All light quickly fades to a darkness and you here\n'
          'a terrible voice ...')
    print()
    time.sleep(2)
    print('Flesh so fine, so fine to tear... and all fades to black')
    print()
    time.sleep(2)
    print('You awake in the room you first woke in but something is different\n'
          'Ragnar sadly smiles at you before fading away and you realize that \n'
          'you perished in the dungeon and now your soul is trapped to help the next\n'
          'adventurer... you only hope Ragnar is finally at rest but you have a feeling\n'
          'his soul was lost to a terrible fat and you hope that you wont suffer the same.')
    print()
    print()
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
time.sleep(1)
print('\nYou wake up in a strange place, the floor is hard stone, covered in\n'
      'dirt, and stained with something that looks like blood.\n'
      'You hear something behind you and turn around to find someone hiding\n'
      'in the shadows.\n'
      '...\n')
time.sleep(3)
print('A man approaches, almost gliding across floor...\n')
time.sleep(1)
player_name = input('Stranger: Hello traveler... what is your name?   \n')
print()
time.sleep(1)
print('Greetings ' + player_name + ' my name is Ragnar Lodbrok and I will be your guide')
time.sleep(2)
print()
print('Many years ago I too was summoned to this strange place')
print('but after perishing in the dungeon my soul was trapped ')
print('only by helping you escape will I be free to rest.\n')
time.sleep(2)
print('To aid you on your journey I can give you one of two items\n'
      'Choose carefully as one of these may save your life\n'
      '\n'
      ' --> The Mystic Sword of Valhalla (sword)\n'
      ' --> The Holy Torch of Dagda (torch)\n'
      '\n'
      'Which will you choose?')
print()
print('enter either "sword" or "torch"')
weapon = input()

# add if statement here to check which was chosen and print different for each

print()
if weapon == 'sword':
    print('Much honor to you ' + player_name + ' you have chosen wisely!\n'
                                               'May Oden and Thor watch over you!')
else:
    print('Very wise, beware of the shadow here and keep hold onto\n'
          'the Torch of Dagda close at all times!\n')

print('And let me give you one last warning.\n'
      'As you make your way through the dungeon NEVER pick the same way twice in a row!')
print()
print()
print('As you hold your new ' + weapon + ' you realize two doors have appeared')
print()
print('To the LEFT a door bangs shut fiercely and you hear bloodcurdling screams\n'
      '\n'
      'To the RIGHT a door slowly creaks open revealing pitch black darkness\n')
print('Which way will you go?')
direction = input('Enter "right" or "left":  ').lower()

if direction == 'left':
    print()
    print('You enter the room and see a man on the ground who looks hurt\n'
          'and you also notice two doorways... the man asks you for HELP')
    print()
    print('To the LEFT: a room filled with the sounds of joy and laughter\n'
          'and the smells of something delicious!\n'
          'To the RIGHT: a dimly lit room with a table sitting in the middle of the room\n'
          'on the table is a single candle casting strange shadows across the room.\n')
    print('What do you do?... [help, right, or left]')
    print()
    new_direction = input().lower()
    while True:
        if new_direction == direction:
            game_over()
            break
        elif new_direction == 'help':
            new_direction == direction
            print()
            print('As you move forward the man smiles an evil smile and transforms\n'
                  'he becomes a monstrous wolf that attacks you...')
            print()
            if weapon == 'sword':
                print('You swing the Sword of Valhalla cutting the beast in two\n'
                      'it fades to a mist and disappears leaving a strange key on the floor\n'
                      'you pick up the key and need to move forward...')
                print()
                print('Which way do you go?... [left ot right]')
                print()
                direction = input().lower()
                if direction == new_direction:
                    game_over()
                    break
                else:
                      print()
                      print('You enter the poorly lit room and approach the table\n'
                            'you find two chests on the table and some how know the key \n'
                            'will unlock one of the chests... But which one?')
                      print()
                      print('Which chest do you unlock? The one to the RIGHT or the LEFT?')
                      print()
                      direction = input().lower()
                      if direction == new_direction:
                            print()
                            print('The chest springs to life and bites your hand...')
                            print()
                            game_over()
                            break
                      else:
                            print()
                            print('The chest clicks open but suddenly vanishes in a flash of light\n'
                                  'the room is suddenly filled with a brilliant light revealing\n'
                                  'two door ways...')
                            print()
                            print('To the RIGHT: a room filled with the sounds of joy and laughter\n'
                                  'and the smells of something delicious!\n'
                                  'To the LEFT: a door creaks open but you cant make out what lays \n'
                                  'on the other side but hear howling winds...')
                            print()
                            print('Which door do you take? The "right" or the "left"?')
                            new_direction = input().lower()
                            if new_direction == direction:
                                  print()
                                  game_over()
                                  break
                            else:
                                  print()
                                  print('You step through the door and find you self in the middle of the woods\n'
                                        'you realize that you have escaped the dungeon!\n'
                                        'turning around you see Ragnar smiling at you.')
                                  print()
                                  print(
                                        'Thank You adventurer!!! You have set me free and I will be eternally grateful\n'
                                        'this is where my journey ends but you must carry on...')
                                  print()
                                  print('You have survived the dungeon but now the BLACK FORREST waits, you steady \n'
                                        'you steady your nerves and move into the clearing ahead.')
                                  print()
                                  print('TO BE CONTINUED!...')
                                  print()
                                  break

if direction == 'right':
    print()
    print('you enter the darkness and hear a whispering rasping voice ')
    print()
    print('Flesh so fine, so fine to tear, to gnash the skin; skin to strip, \n'
          ' so nice, so red the drops that fall; blood so red, so red, so sweet; \n'
          'sweet screams, pretty screams, singing screams, scream your song, \n'
          'sing your screams...')
    print('Who is there? The voice asks... another traveler? Welcome ' + player_name)
    print('What do you have there? That is a powerful ' + weapon)
    print('How about we trade? ... ')
    print('I hold the the key to your salvation and that ' + weapon + ' looks very nice.')
    trade = input('So how about it your ' + ' for my key? [Y/N]').upper()
    while True:
        if trade == 'Y':
            if weapon == 'sword':
                print('Wise choice adventurer... ')
                print('You hand over the Sword of Valhalla and receive the key of salvation')
                print('The blackness seems to fade and the darkness lifts...\n'
                      'you shiver as the voice recedes chanting "sweet screams, pretty screams..."\n'
                      'Looking around you see two door ways. ')
                print()
                print('To the RIGHT: a room filled with the sounds of joy and laughter\n'
                      'and the smells of something delicious!\n'
                      'To the LEFT: a dimly lit room with a table sitting in the middle of the room\n'
                      'on the table is a single candle casting strange shadows across the room.\n')
                print('Which way do you go? [right or left]')
                new_direction = input().lower()
                if new_direction == direction:
                    game_over()
                    break
                else:
                    print()
                    print('You enter the poorly lit room and approach the table\n'
                          'you find two chests on the table and some how know the key \n'
                          'will unlock one of the chests... But which one?')
                    print()
                    print('Which chest do you unlock? The one to the RIGHT or the LEFT?')
                    print()
                    direction = input().lower()
                    if direction == new_direction:
                        print()
                        print('The chest springs to life and bites your hand...')
                        print()
                        game_over()
                        break
                    else:
                        print()
                        print('The chest clicks open but suddenly vanishes in a flash of light\n'
                              'the room is suddenly filled with a brilliant light revealing\n'
                              'two door ways...')
                        print()
                        print('To the RIGHT: a room filled with the sounds of joy and laughter\n'
                              'and the smells of something delicious!\n'
                              'To the LEFT: a door creaks open but you cant make out what lays \n'
                              'on the other side but hear howling winds...')
                        print()
                        print('Which door do you take? The "right" or the "left"?')
                        new_direction = input().lower()
                        if new_direction == direction:
                            print()
                            game_over()
                            break
                        else:
                            print()
                            print('You step through the door and find you self in the middle of the woods\n'
                                  'you realize that you have escaped the dungeon!\n'
                                  'turning around you see Ragnar smiling at you.')
                            print()
                            print('Thank You adventurer!!! You have set me free and I will be eternally grateful\n'
                                  'this is where my journey ends but you must carry on...')
                            print()
                            print('You have survived the dungeon but now the BLACK FORREST waits, you steady \n'
                                  'you steady your nerves and move into the clearing ahead.')
                            print()
                            print('TO BE CONTINUED!...')
                            print()
                            break
            else:
                print('Yesss! The Holy Torch of Dagda is finally mine!!!\n'
                      'This was the only thing that could stop me...\n'
                      'You look so very sweet... SCREAM FOR ME!!!')
                print()
                print('The shadow attacks enveloping you...')
                game_over()
                break
        elif trade == 'N':
            if weapon == 'sword':
                print('You Fool!!! The Shadow screams as it attacks\n'
                      'you try to fight back but your sword is useless...')
                print()
                game_over()
            if weapon == 'torch':
                print()
                print('The darkness screams: How is this possible!!! \n'
                      'the torch of Dagda glows with an intense light \n'
                      'which consumes the shadow burning it away\n'
                      'a key falls to the ground and you pick it up')
                print()
                print('Looking around you see two door ways...\n'
                      '\n'
                      'To the RIGHT: a room filled with the sounds of joy and laughter\n'
                      'and the smells of something delicious!\n'
                      'To the LEFT: a dimly lit room with a table sitting in the middle of the room\n'
                      'on the table is a single candle casting strange shadows across the room.')
                print()
                print('Which way do you go? [right or left]')
                new_direction = input().lower()
                if new_direction == direction:
                      print()
                      game_over()
                      break
                else:
                      print()
                      print('You step through the door and find you self in the middle of the woods\n'
                            'you realize that you have escaped the dungeon!\n'
                            'turning around you see Ragnar smiling at you.')
                      print()
                      print('Thank You adventurer!!! You have set me free and I will be eternally grateful\n'
                            'this is where my journey ends but you must carry on...')
                      print()
                      print('You have survived the dungeon but now the BLACK FORREST waits, you steady \n'
                            'you steady your nerves and move into the clearing ahead.')
                      print()
                      print('TO BE CONTINUED!...')
                      print()
                      break

        else:
            print('Im getting very impatient ' + player_name + ' ... enter "Y" or "N"!')
