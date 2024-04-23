# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import colorama
import random

colorama.init()

#The desired amount of times the game plays
desired_amount = 0
#The deired amount converted into an integer
#desired_amount_integer = int(desired_amount)
#points added for everytime a colored box apperesss
points = 0

colours = {
    "G": colorama.back.GREEN + " " + colorama.Style.RESET_ALL,
    "B": colorama.back.BLUE + " " + colorama.Style.RESET_ALL,
    "R": colorama.back.RED + " " + colorama.Style.RESET_ALL,
    "Y": colorama.back.YELLOW + " " + colorama.Style.RESET_ALL,
}

def generate_sequence(length):
    return [random.choice(list(colours.keys())) for _ in range(length)]

def display_welcome():
    print("Welcome to Simon Says\n")
    print("Use the first letter in each color to guess the order.\n")
    print(colorama.Fore.GREEN + "G " + colorama.Fore.BLUE + "B " + colorama.Fore.RED + "R " + colorama.Fore.YELLOW + "Y ")
    print("choose a number between 3 and 30.\n")

def green_color_square():
    global points
    print(colorama.Back.GREEN + "  \n")
    time.sleep(3)
    points += 1
    
def blue_color_square():
    global points
    print(colorama.Back.BLUE + "  \n")
    time.sleep(3)
    points += 1

def red_color_square():
    global points
    print(colorama.Back.RED + "  \n")
    time.sleep(3)
    points += 1

def yellow_color_square():
    global points
    print(colorama.Back.YELLOW + "  \n")
    time.sleep(3)
    points += 1

"""
All color funtions above, add points to point decleration,
also a delay for each time one activates,
prints the colored boxes in the terminal.
"""
"""
def game():
    randint(1, desired_amount_integer)

while points <= desired_amount_integer:
"""



def main():
    #main_menu()
    green_color_square()
    blue_color_square()
    red_color_square()
    yellow_color_square()

main()
print(points)