import colorama
from colorama import Fore, Style
from textblob import TextBlob
import random as rd
import questionary

colorama.init()
print(f"{Fore.CYAN}Welcome to The Number Guessing Game!{Style.RESET_ALL}")

number_to_guess = rd.randint(1, 100)  # The number the user has to guess

user_name = input(f"{Fore.GREEN}Please enter your name: {Style.RESET_ALL}") # The name of the user

if not user_name:
    user_name = "Player"  # Fallback if user doesn't provide a name

input(f"{Fore.CYAN}Hello, {user_name}! I have selected a number between 1 and 100. "
      f"Try to guess it! Press Enter to start the game.{Style.RESET_ALL}")

while True:
    guess = input(f"{Fore.YELLOW}Enter your guess (or type 'exit' to quit): {Style.RESET_ALL}").strip()
    if guess.lower() == "exit":
        print(f"{Fore.CYAN}Goodbye, {user_name}!{Style.RESET_ALL}")
        break
    if not guess.isdigit():
        print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")
        continue
    guess = int(guess)
    if guess == number_to_guess:
        print(f"{Fore.GREEN}Congratulations, {user_name}! You guessed the number!{Style.RESET_ALL}")

        options = questionary.select(
        "Choose a language:",
            choices=[
            "Try again",
            "Quit"
            ]
        ).ask()


        if options == "Try again":
            number_to_guess = rd.randint(1, 100)  # Reset the number
            continue
        elif options == "Quit":
            options = questionary.select(
            "Choose a language:",
                choices=[
                "Cancel",
                "Quit"
                ]
            ).ask()

            if options == "Cancel":
                number_to_guess = rd.randint(1, 100)  # Reset the number
                continue
            elif options == "Quit":
                print(f"{Fore.CYAN}Goodbye, {user_name}!{Style.RESET_ALL}")
            break
    elif guess < number_to_guess:
        print(f"{Fore.BLUE}Too low! Try again.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Too high! Try again.{Style.RESET_ALL}")