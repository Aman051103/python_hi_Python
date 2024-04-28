import random
c=input("do you want to play :")
d=0
while c=='yes' :
        b=random.randint(1,100)
        while d<5 :
            a=int(input('enter number between 1 to 100 :'))    
            if a!=b :
                if a<b :
                        print ('guess a bit high')
                else :
                        print ('guess a bit low')
                d+=1
            else :
                     print ("you won")
                     break
        else :
                print ("you lose")
                print ("The number is :" , b)
                d=0
        c=input("do you want to play :")
else :
    print ("have a good day")
