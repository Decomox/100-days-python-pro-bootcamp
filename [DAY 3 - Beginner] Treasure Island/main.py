import colorama
import time
from colorama import Fore, Style

colorama.init(autoreset=True)

art = f'''
{Fore.YELLOW}*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"-.__________________|_______
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************{Style.RESET_ALL}
'''

print(art)
time.sleep(1)
print(f"{Fore.CYAN}Welcome to Treasure Island.")
time.sleep(1)
print("Your mission is to find the treasure.")
time.sleep(1)


choice1 = input(f'{Fore.MAGENTA}You\'re at a crossroad. Where do you want to go? Type "left" or "right"\nYOUR CHOICE: ').lower()
if choice1 == "left":
    choice2 = input(f'{Fore.MAGENTA}You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\nYOUR CHOICE: ').lower()
    if choice2 == "wait":
        choice3 = input(f"{Fore.MAGENTA}You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\nYOUR CHOICE: ").lower()
        if choice3 == "red":
            print(f"{Fore.RED}It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print(f"{Fore.GREEN}You found the treasure! You Win!")
        elif choice3 == "blue":
            print(f"{Fore.RED}You enter a room of beasts. Game Over.")
        else:
            print(f"{Fore.RED}You chose a door that doesn't exist. Game Over.")
    else:
        print(f"{Fore.RED}You get attacked by an angry trout. Game Over.")
else:
    print(f"{Fore.RED}You fell into a hole. Game Over.")
