#number guess game

import random
print("welcome to number guessing game")

number=random.randint(1,100)
attempt=0
while attempt<5:
    num=int(input("enter a number:"))
    if(num==number):
        print("you are winner..")
        break
    elif num>number:
        print("too high")

    elif num<number:
        print("to low")
    attempt=attempt+1

if attempt==5:
    print("sorry you out from game....\nyou have not any attempt....")