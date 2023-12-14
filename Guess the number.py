
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
Number=random.choice(range(1,101))

level=(input("Choose a difficulty, type easy or hard: "))
if level=="easy":
    attempts=10
    print (f"you have {attempts}  attempts to guess the number.")
else:
    attempts=5
    print (f"you have {attempts} attempts to guess the number.")
def number_guess():
    global attempts
    guess_number=False
    while not guess_number :
        a=int(input("Make a guess: "))
        
        if a==Number:
            print("You win, you have got the number.")
            guess_number=True
        elif a>Number:
            print("Too high")
            print(f"you have {attempts -1} attempts remaining")
            attempts=attempts-1
            if attempts==0:
                print("You loose")
                guess_number=True
        elif a<Number:
            print("Too low")
            print(f"you have {attempts -1} attempts remaining")
            attempts=attempts-1
            if attempts==0:
                print("You loose")
                guess_number=True
number_guess()
    
    
