# Ashraf Sehba Tabil Oindry
# ENG 101_03
# Due Date: 03/28/2019
def Guess03(a=0):
    '''Randomly picks a number and askes the user to guess it. Then checks if the user's guess is right '''

    import random #Importing random function

    if (a<=999 & a>=1): # Defining the random number that the computer will pick
        a = a
    elif a==0:
        a=random.randint(0,1000)
    else:
        print('Enter something else')


    b=input("Guess a number between 0-1000: ") # Asking user to guess

    i=1
    while int(b)!=a: # Examining every guess
        if b.lower()=="quit": # Quit option for the user in case he/she wants to end the game
            print("0")
            break

        if int(b)>a: # Checking if the guess is greater than the selected random number
            print("Too High")
            b=input("Please guess again with a different number:")

        if int(b)<a: # Checking if the guess is greater than the selected random number
            print("Too Low")
            b=input("Please guess again with a different number:")

        if int(b)==a: # When the guess is correct.
            print("Correct")
            print("Number of attempts",str(i))# Number of attempts 
            break
        
        i+=1
        


