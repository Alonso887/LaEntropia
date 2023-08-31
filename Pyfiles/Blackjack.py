import random, os, time#♥♣♠♦

symbols = ["♥","♣","♠","♦"]
figures = ["A","J","K","Q"]
def s(n):
    time.sleep(n)
def c():
    os.system('cls')

def generate_figure_card():#Figures like As, king, queen and Joker
    figure_type_ran = random.randint(1,4)
    return figures[figure_type_ran]
def generate_card_values():#I put ran at the variables that i use for determinate a random value
    type_of_card_ran = random.randint(1,52)
    card_symbol_ran = random.randint(1,4)
    if type_of_card_ran > 16:
        figure_type = generate_figure_card
        if figure_type == "A":
    else:
        card_number_ran = random.randint(2,9)
        card_data = [card_symbol_ran,symbols[card_symbol_ran]]
        return card_data