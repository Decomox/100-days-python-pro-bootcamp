import time

art = '''
\033[1;35m  _____ ___ ___    ___   _   _    ___ _   _ _      _ _____ ___  ___ 
 |_   _|_ _| _ \  / __| /_\ | |  / __| | | | |    /_\_   _/ _ \| _ \.
   | |  | ||  _/ | (__ / _ \| |_| (__| |_| | |__ / _ \| || (_) |   /
   |_| |___|_|    \___/_/ \_\____\___|\___/|____/_/ \_\_| \___/|_|_\.\033[0m
'''

print(art)
time.sleep(1)

bill = float(input("\033[1mEnter the total amount of your bill: $\033[0m"))
tip = int(input("\033[1mHow much tip would you like to give? (10, 12, or 15): \033[0m"))
people = int(input("\033[1mHow many people to split the bill? \033[0m"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "${:.2f}".format(bill_per_person)

print()
print("\n╔" + "═" * 56 + "╗")
print("║" + " " * 56 + "║")
print("║" + " " * 21 + "\033[1;36mBILL SPLITTER\033[0m" + " " * 22 + "║")
print("║" + " " * 56 + "║")
print("║" + f"  \033[1mTotal Amount:\033[0m ${bill:.2f}")
print("║" + f"  \033[1mTip Percentage:\033[0m {tip}%")
print("║" + f"  \033[1mNumber of People:\033[0m {people}")
print("║" + " " * 56 + "║")
print("╠" + "═" * 56 + "╣")
print("║" + f"  \033[1mEach person should pay:\033[0m {final_amount}")
print("╚" + "═" * 56 + "╝")
