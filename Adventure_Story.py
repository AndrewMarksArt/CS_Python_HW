import time


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
print('You wake up in a strange place, the floor is hard stone, covered in\n'
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
    print('Much honor to you '+ player_name + ' you have chosen wisely!\n'
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
print('To the LEFT a door bangs shut fiercely and you hear blood curteling screams\n'
      '\n'
      'To the RIGHT a door slowly creaks open revealing pitch black darkness\n')
print('Which way will you go?')
direction = input('Enter "right" or "left":  ')

# if needed to see which way to go

'''---------------------- LEVEL 1 ------------------------------------'''

''' RIGHT FROM START: you oen the door and find what looks like a small 
    cat sitting in the middle of the room next to a man who is lying on 
    the floor injured pleading for help. Hallway to the right, well lit 
    with the sounds of music and laughter. Room off to the left with a 
    single candle sitting on the table flickering.
    
    --> Do you help the man on the floor?
        = if yes the cat and man merge into a shadow beast which can be 
          slain with the Torch, the Sword passes through the monster 
          which kills you. --> if you survive you find a key on the floor 
                               and need to pick LEFT / RIGHT
    --> Do you go to the right? --> a shadow descends on you and returns 
                                    you to the start.
    --> Do you go to the left? --> move to next room'''

''' LEFT FROM START: You enter the darkness and hear a rasping voice. 
    It tells you its sooooo tired, soooo hungry, and asks if you are 
    there to kill it?
    
    --> Yes = if you have the Torch it attacks but the fire burns it away
              filling the room with light and revealing a key on the floor.
            = if you have the Sword it passes through the shadowy beast 
              without harming it and you are ripped to shreds!
    --> No  = if you have the Torch he says he will let you pass if you
              put it out --> if you put it out he attacks and kills you
                         --> you see through his ruse and attack burning 
                             the shadow away revealing a key on the floor.
            = if you have the Sword if glows with magic and he tells you 
              he will trade his key the Sword --> if you give him the Sword 
                                                  he vanishes filling the 
                                                  room with light and a key 
                                                  is on the floor
                                              --> if you say no he attacks 
                                                  and kills you.
    
    After the monster is gone you see a hallway to the left well lit 
    with the sounds of music and laughter. To the right a room off to the
    left with a single candle sitting on the table flickering.
    
    --> Do you go to the Right? --> enter the room and the candle goes out.
    
    --> DO you go to the Left? --> a shadow descends on you and returns 
                                    you to the start.'''


''' Back to start death ---------------------------

    Did you end up back where you started? If so you see the ghost who 
    helped you when you first woke up who smiles sadly at you as he disappears
    and you realize you are dead and your spirit has taken the place of the
    ghost, you know you will be free only when the next traveler survives the
    cave but if that's the case then what happened to the other ghost and if 
    you fail what new torment will await your soul?'''


'''---------------------- LEVEL 2 -----------------------------------------'''

''' Table room from PITCH BLACK room: You enter the room and approach the table
    and see two chests, one on the right labeled 'Destiny' and the one on the left 
    labeled 'Luck'. You take out the key... which one do you open?
    
    --> if RIGHT: the chest turns into a mimic and eats you.
    
    --> if LEFT: you find a piece of paper with strange writing on it, it looks
                 like a spell and when you read it two door ways appear, one to 
                 the left that leads to a massive treasure room. To the RIGHT 
                 pitch black with the sounds of howling winds. Which way do you go?
                        --> if LEFT: you step into the treasure room and start
                            sinking into the floor like its quick sand, you grasp
                            for anything to grab hold of but everything turns to
                            liquid in your hands. Gasping for breath you try to
                            scream but black out waking in back in the main room.
                        --> if RIGHT: you step through the doorway and out into 
                            what appears to be the middle of a clearing in the
                            middle of the woods. The ghost you saw at the begging
                            of your quest greets you laughing and thanks you for
                            saving him as he fades away. You hear a voice behind
                            you... Greetings adventurer, they way ahead is dangerous
                            and filled with may perils, choose your path carefully.
                            
                            You realize your quest is not over but has only begun,
                            turning to see you greeted you, you take a deep breath 
                            steadying your resolve as you prepare to try and survive
                            what lies ahead...
                            
                            TO BE CONTINUED!!!'''

"""
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
                               `             '     """