def Guess03():
    import random
    x=random.randint(1,1000)
    a=0;
    y=input("Please Guess a number between 1 to 1000 or type quit to quit: ")
    if(x):
        while(x):
            if(str(y)=="quit"):
                print("Thanks for playing the game")
                break
            else:
                if (int(y)==x):
                    a+=0
                    print("Your guess is right!Congratulations!")   
                    print("Number of attempts:",a)
                    print("x=",x)
                    print("y=",y)
                    break
                else:
                    while (int(y)<x):
                        y=input("Guess something higher than this:")
                        if(str(y)=="quit"):
                            print("Thanks for playing the game")
                            break
                        else:
                            y=int(y)
                            a+=1
                    while (int(y)>x):
                        y=input("Guess something lower than this:")
                        if(str(y)=="quit"):
                            print("Thanks for playing the game")
                            break
                        else:
                            y=int(y)
                            a+=1
        
        
    
          
