import os, time, random
box_designs = ["  ______ \n /     /|\n/_____/ |\n|     | |\n| BOX | /\n|_____|/ ",
              "  ┌----┐\n  |    | \n  |____| \n /     /|\n/_____/ |\n|     | |\n| BOX | /\n|_____|/ ",
              "┌──┐ ┌───┐ \n└ ┌-_-┐  ┘\n  |---|_ \n /|---|/|\n/_|___/ |\n|     | |\n| BOX | /\n|_____|/ "]
#[0] is closed box, [1] is opne em´ty box and [2] is open carrot box
box_data = [1,1]# randomly adds 1 to one value so i can randomly choose and save where the carrot is
def s(n):
    time.sleep(n)
def c():
    os.system("cls")
def the_boxgame(bd):#bd means box data, i'm terrible with acronyms
    while True:
        print("Ok one of you two close your eyes, the other one, choose a box, box 1 or 2(use only numbers pls)")
        print(box_designs[0])
        print(box_designs[0])
        n  = random.randint(1,100)#i know, i could use 1-2 but this way it just looks better :)
        if n >= 50:
            bd[0] += 1
        else:
            bd[1] += 1
        choice1 = int(input("> "))#the choice made by the first player
        if choice1 > 2 or choice1 < 1:
            s(1)
            c()
            print("I said choose a number between 1-2 idiot >:(")
            s(2)
            c()
            continue
        s(1)
        c()
        print("Well now wait till this gets erased and try to convince your friend to get the wrong box")
        if choice1 == 1:
            print(box_designs[bd[choice1-1]])#It's a bit hard to understand but it actually makes sense, just see the names
            print(box_designs[0])
        else:
            print(box_designs[0])
            print(box_designs[bd[choice1-1]])
        s(10)
        c()
        print("Now is your turn player 2, will the tricks of your friend make you choose the wrong box or will you be succsesfull")
        print("(Remember to use only number 1 or 2 pls)")
        print(box_designs[0])
        print(box_designs[0])
        choice2 = int(input("> "))
        s(1)
        c()
        if bd[choice2-1] == 2:
            print("Hahahah, smart move, your friend wasn't enough to distract you from the victory")
        elif bd[choice2-1] == 1:
            print("HAHAHA, you fell into the mental traps imposed by your friend, he took the victory from you, really sad")
        if choice2 == 1:
            print(box_designs[bd[choice2-1]])#I just copied this part LMAO 
            print(box_designs[0])
        else:
            print(box_designs[0])
            print(box_designs[bd[choice2-1]])
        s(5)
        c()
        break
the_boxgame(box_data)

