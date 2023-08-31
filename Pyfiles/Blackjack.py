import random, os, time#♥♣♠♦

symbols = ["♥","♣","♠","♦"]
figures = ["A","J","K","Q"]
def s(n):
    time.sleep(n)
def c():
    os.system('cls')

def generate_figure_card():#Figures like As, king, queen and Joker
    figure_type_ran = random.randint(0,3)
    return figures[figure_type_ran]
def generate_card_values():#I put ran at the variables that i use for determinate a random value
    type_of_card_ran = random.randint(1,52)
    card_symbol_ran = random.randint(0,3)
    if type_of_card_ran < 16:
        card_data = [generate_figure_card(),symbols[card_symbol_ran]]
        return card_data
    else:
        card_number_ran = random.randint(2,9)
        card_data = [card_number_ran,symbols[card_symbol_ran]]
        return card_data

def print_card(card_data):
    print(f"{card_data[0]}-----{card_data[1]}\n|     |\n|  {card_data[1]}  |\n|     |\n{card_data[1]}-----{card_data[0]}")

num = generate_card_values()
num1 = print_card(num)
print(num1)