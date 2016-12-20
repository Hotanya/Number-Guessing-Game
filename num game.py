import random

number = random.randint(1, 100)
print("Welcome to the Guessing Game!")
print("Guess a number:")
#again = "y"

boo = False
x = input()
while boo != True:
    if int(x) > number:
        print("too high, guess again")
        x = input("try again: ")
        
    elif int(x) < number:
        print("sorry too low,guess again")
        x = input("try again: ")
        
    elif int(x) == number:
        print ("congrats, u win")
        boo = True

def game():

    count = 0
    
        
    number = random.randint(1, 100)
    print("Welcome to the Guessing Game!")
    print("Guess a number:")
    
    x = input()
    boo = False
    
    while boo != True:
        if int(x) > number:
            print("too high, guess again")
            x = input("try again: ")
            
        elif int(x) < number:
            print("sorry too low,guess again")
            x = input("try again: ")
            
        elif int(x) == number:
            print ("congrats, u win")
            boo = True
        
            
a = input("Would you like to play again?")

if a == ("yes"):
    game()

elif a == ("y"):
    game()
            
else:
    boo = True
print("Goodbye")

