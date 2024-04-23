# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import colorama
import random

colorama.init()

colours = {
    "G": colorama.back.GREEN + " " + colorama.Style.RESET_ALL,
    "B": colorama.back.BLUE + " " + colorama.Style.RESET_ALL,
    "R": colorama.back.RED + " " + colorama.Style.RESET_ALL,
    "Y": colorama.back.YELLOW + " " + colorama.Style.RESET_ALL,
}

def display_welcome():
    print("Welcome to Simon Says\n")
    print("Use the first letter in each color to guess the order.\n")
    print(colorama.Fore.GREEN + "G " + colorama.Fore.BLUE + "B " + colorama.Fore.RED + "R " + colorama.Fore.YELLOW + "Y ")
    print("choose a number between 3 and 30.\n")

def generate_sequence(length):
    return [random.choice(list(colours.keys())) for _ in range(length)]

def display_sequence(sequence):
    for color in sequence:
        print(colours(color), end=" ")
        time.sleep(1)
    print (colorama.Style.RESET_ALL + "\n")

def get_user_input():
    return input("Enter the sequence of colors using (GRBY):").strip().upper()

def play_game():
    display_welcome()
    while True:
        try:
            length = int(input("Enter length"))
            if length < 3 or length > 30:
                print("error")
                continue
            break
        except ValueError:
            print("Enter valid number")

seq = generate_sequence(length)
display_sequence(seq)
user_guess = get_user_input()

score = 0
for i in range(len(seq)):
    if i < len(user_guess) and seq[i] == user_guess[i]:
        score += 1
