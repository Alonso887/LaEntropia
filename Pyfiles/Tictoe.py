import time, os
#First i put all the variables i will need, those that will always be there, not like Amanda you bitch
tt = [0,0,0,0,0,0,0,0,0] #tt for tictoe

#Then the functions, i'll put some notes in the most importants and confusing ones
def s(n):
    time.sleep(n)
def c():
    os.system("cls")
def print_tt(t):
    n = 1
    for i in t:
        if i == 0:
            print("| ", end="")
        elif i == 1:
            print("|o", end="")
        else:
            print("|x", end="")
        if n % 3 == 0:
            print("|")
        n += 1
def vic_checker():#checks if you win,it checks i by brute force cause i'm laizy and is only 8 posible combinations
    if tt[0] == tt[1] and tt[1] == tt[2] and tt[1] != 0:
        return [True,tt[0]]
    elif tt[3] == tt[4] and tt[4] == tt[5] and tt[4] != 0:
        return [True,tt[3]]
    elif tt[6] == tt[7] and tt[7] == tt[8] and tt[7] != 0:
        return [True,tt[6]]
    elif tt[0] == tt[3] and tt[3] == tt[6] and tt[3] != 0:
        return [True,tt[0]]
    elif tt[1] == tt[4] and tt[4] == tt[7] and tt[4] != 0:
        return [True,tt[1]]
    elif tt[2] == tt[5] and tt[5] == tt[8] and tt[5] != 0:
        return [True,tt[2]]
    elif tt[0] == tt[4] and tt[4] == tt[8] and tt[4] != 0:
        return [True,tt[0]]
    elif tt[2] == tt[4] and tt[4] == tt[6] and tt[4] != 0:
        return [True,tt[2]]
    else:
        return [False,None]
def tie_checker():#well checks if the game ends in a tie before it checks if it ends witha winner
    for i in tt:
        for i in tt:
            if i == 0:
                return False
                break
        return True


def the_game():#I mean is on the name, this is like actually the game bro like the actual
    n = 1
    while True:
        if n % 2 > 0:
            ply_name = "x"
        else:
            ply_name = "o"
        print(f"Player {ply_name}, is your turn!\nChoose the number of the cell you want to put your symbol")
        print_tt(tt)
        ply_choice = int(input("> "))
        if tt[ply_choice - 1] > 0:
            print("That cell is already occupied!")
            s(2)
            continue
        else:
            if ply_name == "o":
                tt[ply_choice - 1] = 1
            elif ply_name == "x":
                tt [ply_choice - 1] = 2
        tie_value = tie_checker()
        if tie_value:
            c()
            s(1)
            print("The game ends in a tie")
            s(2)
            c()
            break
        vict_info = vic_checker()
        if vict_info[0]:
            c()
            s(1)
            print(f"Player{vict_info[1]} wins the game!")
            s(2)
            c()
            break
        n += 1
        s(1.5)
        c()
#Now everything after this line is the actual programm and not the functions, just for better understanding and less nesting
while True:
    print("======================")
    print("Tic Tac Toe")
    print("======================")
    s(1)
    print("Hi, this is tic tac toe, choose an option")
    print("1-New game\n2-Exit")
    player_choice = input("> ")
    if player_choice == "1":
        the_game()
        tt = [0,0,0,0,0,0,0,0,0]
    elif player_choice == "2":
        s(1)
        c()
        print("Well goodbye :)")
        s(2)
        c()
        break
    else:
        c()
        print("That is not an option, try using the numbers of the options")
        s(2)
        c()

    

