import random


print("Computer's Turn First")
rand_No = random.randint(1,3)
if rand_No == 1:
    com = 's'
elif rand_No == 2:
    com = 'w'  
elif rand_No == 3:
    com = 'g'     

b = input("Player's Turn: Snake(s) Water(w) or Gun(g)?")

def game(com,b):
    if com == b:
        return None
    elif com == 's':
        if com == 'w':
            return False
        elif b == 'g':
            return True
    elif com == 'w':
        if b == 'g':
            return False
        elif b == 's':
            return True


game_res = game(com,b)

if game_res == None:
    print("!!!This a tie!!!")
elif game_res:
    print("You have won the game")
else:
    print("Sorry! You have lost the game")    