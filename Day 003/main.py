print('''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \.
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
                                       
''')

print("\nWelcome to Treasure Island!\nYour mission is to find the treasure.")
direction = input("\nYou're at a cross road. Where do you want to go?\nType \"left\" or \"right\"\nR: ").lower()
if direction == 'left':
    lake = input("\nYou've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across.\nR: ").lower()
    if lake == 'wait':
        door = input("\nYou arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which color do you choose?\nR: ").lower()
        if door == 'yellow': 
            print("\nCongratulations! You found the treasure!")
            print('''*******************************************************************************
                            |                   |                  |                     |
                    _________|________________.=""_;=.______________|_____________________|_______
                    |                   |  ,-"_,=""     `"=.|                  |
                    |___________________|__"=._o`"-._        `"=.______________|___________________
                            |                `"=._o`"=._      _`"=._                     |
                    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                    /______/______/______/______/______/______/______/______/______/______/[TomekK]
                    *******************************************************************************
                  ''')
        else: 
            print("\nThere was a trap hidden behind the door. Game over!")
    else:
        print("You've got drown by the lake water. Game over!")
else:
    print("You've been caught into a trap\nGame Over!")