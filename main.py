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
    
    if level == 1:
        chances = 10
    elif level == 2:
        chances = 5
    else:
        chances = 3
    random_number = rn.randint(1 , 100)
    print(random_number)
    print(f"Great! You have selected the [blue]{difficulty[level- 1]}[/blue] difficulty level.")

    time.sleep(2)
    
    clear_terminal()

    loading_animation(5)

    

    clear_terminal()
    
    temp = chances
    while(chances > 0):
        chances-=1
        number = int(input("Enter your guess: "))
        if number < random_number:
            print(f"Incorrect! The number is greater than {number}.")
        elif number > random_number:
            print(f"Incorrect! The number is less than {number}.")
        else:
            print(f"Congratulations! You guessed the correct number in {temp - chances} attempts.")
            print("If you want you can play again just tell me")
            again = int(input("Do you want to play again (1-Yes , 2 - No): "))
            while(again not in [1,2]):
                again = int(input("Please enter 1 or 2: "))
            if again == 1:
                main()
            else:
                return
        

    if not chances:
        print(f"You have used all of your chances. The number was [red]{random_number}[/red]")
        again = int(input("Do you want to play again (1-Yes , 2 - No): "))
        while(again not in [1,2]):
            again = int(input("Please enter 1 or 2: "))
        if again == 1:
            main()
        else:
            return  


main()
