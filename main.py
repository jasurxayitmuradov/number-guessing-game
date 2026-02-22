import random as rn
import time 
import sys
import platform
import os
from rich import print

def clear_terminal():

    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def loading_animation(duration_seconds=5):
    start_time = time.time()
    base_text = "I'm thinking of a number between 1 and 100"
    
   
    while time.time() - start_time < duration_seconds:
        for dots in [".  ", ".. ", "..."]: 
            sys.stdout.write(f"\r{base_text}{dots}")
            sys.stdout.flush()
            time.sleep(0.5)
    
    
    print("\nOkay, I'm ready!")


    


def main():
    print('''Welcome to the Number Guessing Game!
Please select the difficulty level:
1. [green]Easy (10 chances)[/green]
2. [yellow]Medium (5 chances)[/yellow]
3. [red]Hard (3 chances)[/red]''')
    
    print()
    level = int(input("Enter your choice: "))

    difficulty = ["Easy" , "Medium" , "Hard"]

    while level not in [1,2,3]:
        level = int(input("You have to choice only these numbers 1 , 2, 3: "))

    print(f"Great! You have selected the [blue]{difficulty[level- 1]}[/blue] difficulty level.")

    time.sleep(2)
    
    clear_terminal()

    loading_animation(8)

main()

