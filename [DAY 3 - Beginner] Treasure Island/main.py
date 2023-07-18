import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Define the ASCII art
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

# Print the ASCII art
print(art)

# Print the game instructions
print(f"{Fore.CYAN}Welcome to Treasure Island.")
print("Your mission is to find the legendary treasure of the Lost City.")

# Get the user's input for choice1
choice1 = input(f'{Fore.GREEN}You\'re at a crossroad. Where do you want to go? Type "left" or "right"\nYOUR CHOICE: ').lower()

if choice1 == "left":
    print("------------------\nYou follow the left path and enter a dark forest. You come across two signs:")
    print("One points to a dangerous cave, and the other to a mysterious temple.")
    # Get the user's input for choice2
    choice2 = input(f'{Fore.GREEN}Which path will you choose? Type "cave" or "temple"\nYOUR CHOICE: ').lower()

    if choice2 == "cave":
        print("------------------\nYou enter the cave and find yourself surrounded by treasures. However, a ferocious dragon blocks your way.")
        # Get the user's input for choice3
        choice3 = input(f'{Fore.GREEN}How do you handle the dragon? Type "fight" or "sneak"\nYOUR CHOICE: ').lower()

        if choice3 == "fight":
            print("------------------\nYou engage in a fierce battle with the dragon but are ultimately defeated.")
            print(f"{Fore.RED}Game Over.")
        elif choice3 == "sneak":
            print("------------------\nYou stealthily move past the dragon, grab a handful of treasures, and make your way out of the cave.")
            # Get the user's input for choice4
            choice4 = input(f'{Fore.GREEN}You find a hidden passage. Do you want to explore it? Type "yes" or "no"\nYOUR CHOICE: ').lower()

            if choice4 == "yes":
                print("------------------\nYou follow the hidden passage and discover an underground river. You build a raft and sail downstream.")
                # Get the user's input for choice5
                choice5 = input(f'{Fore.GREEN}As you sail, you see two paths: one leading to a waterfall and the other to a serene island. Which path do you choose? Type "waterfall" or "island"\nYOUR CHOICE: ').lower()

                if choice5 == "waterfall":
                    print("------------------\nYou go over the waterfall and survive, but all your treasures are lost.")
                    print(f"{Fore.RED}Game Over.")
                elif choice5 == "island":
                    print("------------------\nYou reach the peaceful island and find the entrance to the Lost City. You're one step closer to the treasure.")
                    print("Inside the Lost City, you encounter a series of puzzles and traps. After solving them, you finally stand before the legendary treasure.")
                    print(f"{Fore.YELLOW}Congratulations! You have found the treasure of the Lost City. You Win!")
                else:
                    print("------------------\nYou're indecisive and unable to make a choice.")
                    print(f"{Fore.RED}Game Over.")
            else:
                print("------------------\nYou decide not to explore the hidden passage and continue your journey. Good luck!")
        else:
            print("------------------\nYou hesitate and the dragon attacks you.")
            print(f"{Fore.RED}Game Over.")
    elif choice2 == "temple":
        print("------------------\nYou enter the ancient temple and find yourself in front of three altars:")
        print("One made of gold, one made of silver, and one made of bronze.")
        # Get the user's input for choice6
        choice6 = input(f'{Fore.GREEN}Which altar do you approach? Type "gold", "silver", or "bronze"\nYOUR CHOICE: ').lower()

        if choice6 == "gold":
            print("------------------\nThe altar turns out to be a trap, and you get captured by temple guardians.")
            print(f"{Fore.RED}Game Over.")
        elif choice6 == "silver":
            print("------------------\nYou approach the silver altar, and it reveals a secret passage. You cautiously make your way through it.")
            print("You find yourself in an underground labyrinth filled with deadly traps and illusions.")
            print("After a long and treacherous journey, you reach a hidden chamber.")
            print("Inside the chamber, you find the ancient map leading to the Lost City.")
            print("You are now one step closer to the treasure.")
            print("The adventure continues...")
        elif choice6 == "bronze":
            print("------------------\nAs you approach the bronze altar, it starts trembling, and the ground beneath you gives way.")
            print(f"{Fore.RED}Game Over.")
        else:
            print("------------------\nYou're indecisive and unable to make a choice.")
            print(f"{Fore.RED}Game Over.")
    else:
        print("------------------\nYou're indecisive and unable to make a choice.")
        print(f"{Fore.RED}Game Over.")
else:
    print("------------------\nYou take the right path and come across a deep river. You have two options:")
    print("Swim across or build a raft.")
    # Get the user's input for choice7
    choice7 = input(f'{Fore.GREEN}How do you plan to cross the river? Type "swim" or "raft"\nYOUR CHOICE: ').lower()

    if choice7 == "swim":
        print("------------------\nYou attempt to swim across the river but get caught in a strong current.")
        print(f"{Fore.RED}Game Over.")
    elif choice7 == "raft":
        print("------------------\nYou gather materials and build a sturdy raft. With great effort, you manage to navigate across the river safely.")
        print("On the other side, you find yourself in a dense jungle with a hidden path.")
        print("You follow the path and encounter a group of local tribespeople.")
        print("They offer you guidance to the Lost City, but they warn you about dangerous traps ahead.")
        print("With their help, you successfully navigate through the traps and reach the entrance of the Lost City.")
        print("You're one step closer to the treasure.")
        print("Inside the Lost City, you encounter a series of puzzles and challenges. After solving them, you finally stand before the legendary treasure.")
        print(f"{Fore.YELLOW}Congratulations! You have found the treasure of the Lost City. You Win!")
    else:
        print("------------------\nYou're indecisive and unable to make a choice.")
        print(f"{Fore.RED}Game Over.")
