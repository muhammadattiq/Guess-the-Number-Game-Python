## In this program a randon number will be generated and user has to guess the random generated number ##

import random

def guess():
    a = random.randint(0,10)
    while True:
        user = int(input("Enter a number"))
        if(user>a):
            print("your guess is too high")
            print(a)
        elif(user<a):
            print("your guess is too low")
            print(a)
        else:
            print("You won!!")
            prompt = input("Do you wanna play more? if yes then (Y) if no then (N)")
            if(prompt=="Y"):
                guess()  
            elif(prompt=="N"):
                print("Dafa Hooo!!")   
            break       
            
guess()



