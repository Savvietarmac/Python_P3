# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import colorama
colorama.init()
"""
def main_menu():
    
    Main menu for the game, used to send the user further.
    
    print(colorama.Fore.BLUE + colorama.Back.YELLOW + "Welcome to Simonsays!\n")
    print(colorama.Fore.YELLOW + colorama.Back.YELLOW + "Now with Color!\n")
    print(colorama.Fore.CYAN + colorama.Back.WHITE + "Press 'A' to start the game\n")
"""    
desired_amount = input("")

points = 0

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







def main():
    #main_menu()
    green_color_square()
    blue_color_square()

main()
print(points)