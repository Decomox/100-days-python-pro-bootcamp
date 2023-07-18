import time

art = '''
  ___ __  __ ___    ___   _   _    ___ _   _ _      _ _____ ___  ___ 
 | _ )  \/  |_ _|  / __| /_\ | |  / __| | | | |    /_\_   _/ _ \| _ \.
 | _ \ |\/| || |  | (__ / _ \| |_| (__| |_| | |__ / _ \| || (_) |   /
 |___/_|  |_|___|  \___/_/ \_\____\___|\___/|____/_/ \_\_| \___/|_|_\.
                                                                     
'''

print(art)
time.sleep(1)

height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / height ** 2
category = ""

if bmi < 18.5:
    category = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    category = "Normal"
elif bmi >= 25 and bmi < 30:
    category = "Overweight"
elif bmi >= 30 and bmi < 35:
    category = "Obese"
else:
    category = "Extremely Obese"

print("\n------------------------------------------------------------")
print("|                   BMI CALCULATOR                         |")
print("------------------------------------------------------------")
print(f"|  Height: {height:.2f} m")
print(f"|  Weight: {weight} kg")
print("------------------------------------------------------------")
print(f"|  BMI:    {bmi:.2f}")
print(f"|  Category: {category}")
print("------------------------------------------------------------")

time.sleep(5)
art2 = '''
   *                                 (                                 
 (  `         (            (         )\ )                              
 )\))(     )  )\ )  (    ( )\ (     (()/(    (           )          )  
((_)()\ ( /( (()/( ))\   )((_))\ )   /(_))  ))\ (  (    (     (  ( /(  
(_()((_))(_)) ((_))((_) ((_)_(()/(  (_))_  /((_))\ )\   )\  ' )\ )\()) 
|  \/  ((_)_  _| (_))    | _ ))(_))  |   \(_)) ((_|(_)_((_)) ((_|(_)\  
| |\/| / _` / _` / -_)   | _ \ || |  | |) / -_) _/ _ \ '  \() _ \ \ /  
|_|  |_\__,_\__,_\___|   |___/\_, |  |___/\___\__\___/_|_|_|\___/_\_\  
                              |__/                                     
'''
print(art2)