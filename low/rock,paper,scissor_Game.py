
'''------------------Rock Paper Scissor Game-------------------'''


import random
user_score=comp_score=tie=0
l=["r","p","s"]
n=input("Do you want to start the Game? enter (yes/no): ")
while n=="yes":
    a=int(input("How many times you want to play:"))
    while a>0:
        user=str(input("Enter your choice, any of(r,p,s):")).lower()
        comp=random.choice(l)
        print("computer's choice is:",comp)
        if user==comp:
            print("its a tie")
            a-=1
            tie+=1
        elif user=="r" and comp=="p":
            print("computer scored for 1")
            comp_score+=1
            a-=1
        elif user=="p" and comp=="r":
            print("ypu scored for 1")
            user_score+=1
            a-=1
        elif user=="r" and comp=="s":
            print("you scored for 1")
            user_score+=1
            a-=1
        elif user=="s" and comp=="r":
            print("computer scored for 1")
            comp_score+=1
            a-=1
        elif user=="p" and comp=="s":
            print("computer scored for 1")
            comp_score+=1
            a-=1
        elif user=="s" and comp=="p":
            print("you scored for 1")
            user_score+=1
            a-=1
        else:
            print("try again... : ")
    if user_score>comp_score:
        print("You won the game....yeah")
    elif user_score<comp_score:
        print("computer won the game...hahaha")
    else:
        print("Tie, you both scored same")
    print("Your total score is:",user_score)
    print("computer's total score is:",comp_score)
    print("Total Ties:",tie)
    user_score=0
    comp_score=0
    tie=0
    n=input("Do you still want to play? enter (yes/no): ")
else :
    print("Game Over")
