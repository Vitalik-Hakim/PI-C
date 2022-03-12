import sys
from pi import *

######### IDKK####################
with open ("ftexts/Alice.txt", "r") as file:
    Alice = file.read().replace('\n', '')

with open ("ftexts/Bob.txt", "r") as file:
    Bob = file.read().replace('\n', '')

bob = Bob
alice = Alice


user1 = input("Player one name: ")
user2 = input("Player two name: ")


#alice = input("{} Say the pi you know: ".format(user1))
#bob = input("{} Say the pi you know: ".format(user2))

alist = list(alice)
blist = list(bob)

lenA  = len(alist)
lenB  = len(blist)


#Verify order or pi numbers



#Alice verify
for pis in range(lenA):
    global correct1
    if pi_100[0:lenA] == alice:
        pass
        correct1 = True
    else:
        print("{} is incorrect! :(\n".format(user1))
        correct1 = False
        break

#Bob verify
for pis in range(lenB):
    global correct2
    if pi_100[0:lenB] == bob:
        correct2 = True
        pass
    else:
        print("{} is incorrect! :(\n".format(user2))
        correct2 = False
        break


if correct1 == False and correct2 == False:
    print("You both suck! nyeh")
    sys.exit()
elif correct1 == True and correct2 == False:
    Winner = "{} is the winner!".format(user1)
    print(Winner)
    sys.exit()
elif correct2 == True and correct1 == False:
    Winner = "{} is the winner!".format(user2)
    print(Winner)
    sys.exit()
else:
    pass



#If they cross this line then its time for lenEval

if len(alice) > len(bob):
    Winner = "{} is the winner!".format(user1)
    print(Winner)
elif len(bob) > len(alice):
    Winner = "{} is the winner!".format(user2)
    print(Winner)
else:
    print("Its a tie between {} and {}".format(user1,user2))

