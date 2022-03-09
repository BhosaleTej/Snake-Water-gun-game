# 1st project snake water gun name :

def gamewin(comp,you):
    if comp==you:
        return none
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you =='g':
            return False
            
print("comp turn: snake(s) water(w) gun(g) ?")
import random
randNo = random.randint(1,3)
if randNo ==1:
    comp='s'
elif randNo ==2:
    comp='w'
elif randNo ==3:
    comp='g'
    
you = input("your turn: snake(s) water(w) gun(g) ?")

a=gamewin(comp,you)
if a == None:
    print("Gome is tie")
elif a:
    print("you win")
else:
    print("you lose")
    
print(f"computer choose {comp}")
print(f"you choose {you}")
    