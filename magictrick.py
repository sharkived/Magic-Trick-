import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

#intro
def magician_intro():
    print(Fore.CYAN + "Welcome to my Grand Hall, Mortal!")
    print(Fore.MAGENTA + "I, the Great Magician Shaila, shall now read your thoughts...")
    time.sleep(2)

#gathering info
def select_your_choices():
    fav_animal = input("Think of your favourite animal: ")
    what_youre_craving = input("What food are you craving?: ")
    magic = input("Do you believe in magic?: ")
    return fav_animal, what_youre_craving, magic

#asking questions
def ask_questions():
    print(Fore.RED + "\nAnswer the questions, or, the magic shall abandon you...")
    likes_zoo = input("Do you like to visit the zoo often? (yes/no): ").strip().lower()
    likes_food = input("Do you like sweet or savory food? (sweet/savory): ").strip().lower()
    likes_magic = input("Do you like magicians? (yes/no): ").strip().lower()
    return likes_zoo, likes_food, likes_magic

#making guesses
def make_guess(fav_animal, what_youre_craving, likes_magic):
    print(Fore.GREEN + "\nReading your answers...")
    time.sleep(1)
    print("Casting a spell....Fuu Fuu...no regular spell cuz...I'm special...")
    time.sleep(2)

    magic_believer = 'definitely' if likes_magic == 'yes' else 'maybe not...nvm cuz I do'

    print(Fore.YELLOW + f"\nHmm..I see it now...")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + f"You're thinking of a {fav_animal}, and you're craving {what_youre_craving}!")
    time.sleep(1)
    print(Fore.MAGENTA + f"And you {magic_believer} believe in magic...")

def magician_exit():
    time.sleep(1)
    print(Fore.YELLOW + "\nThank you for visiting The Grand Hall!")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + "Until next time...keep your mind open and your thoughts enchanted!")
    time.sleep(2)
    print(Fore.CYAN + "!POOF!\n")

#running the program
magician_intro()
fav_animal, craving, magic = select_your_choices()
zoo, food, magician = ask_questions()
make_guess(fav_animal, craving, magician)
magician_exit()

