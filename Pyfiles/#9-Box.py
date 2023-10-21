import os, time, random
box_designs = ["  ______ \n /     /|\n/_____/ |\n|     | |\n| BOX | /\n|_____|/ ",
              "  ┌----┐\n  |    | \n  |____| \n /     /|\n/_____/ |\n|     | |\n| BOX | /\n|_____|/ ",
              "┌──┐ ┌───┐ \n└ ┌-_-┐  ┘\n  |---|_ \n /|---|/|\n/_|___/ |\n|     | |\n| BOX | /\n|_____|/ "]
#[0] is closed box, [1] is opne em´ty box and [2] is open carrot box
def s(n):
    time.sleep(n)
def c():
    os.system("cls")

def print_boxes():#bd means boxdata
    None
print(box_designs[2])