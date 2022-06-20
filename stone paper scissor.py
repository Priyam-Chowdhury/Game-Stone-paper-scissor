import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
       if you=='p':
        return True
       elif you=='s':
        return False
    elif comp=='p':
       if you=='r':
        return False
       elif you=='s':
        return True
    elif comp=='s':
       if you=='r':
        return True
       elif you=='p':
        return False


print("Computer turn: Rock (r) Paper (p) or scissor (s)")
rand=random.randint(1,3)

if rand == 1:
    comp='r'
elif rand==2:
    comp='p'
elif rand==3:
    comp='s'

you=input("Your turn:  Rock (r) Paper (p) or scissor (s)?")
game=gamewin(comp,you)
print("Computer Chose " +str(comp))
print("You Chose " +str(you))
if game==None:
    print("The game is a tie")
elif game==True:
    print("You win!!")
else:
    print("You lose!!")


