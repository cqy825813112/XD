#Qinyun Cao
#2/18/2017
#Guess Game

#import statement
import random
secret = random.randint(1,100)

#print statement
print("---------------Number Game----------")
temp = input("Guess which number I am thinking from 1 to 100.\n")
guess = int(temp)
if guess == secret:
        print("How did you get it ?")
        print("You will not get any prize even though you get the number.")
else:
    while guess != secret:
        if guess > secret:
            print("You are wrong! The number should be smaller.")
        else:
            print("You are wrong! The number should be higher.")
        temp = input("Give you one more chance to guess the number:\n")
        guess = int(temp)
        if guess == secret:
                print("How did you get it ?")
                print("You will not get any prize even though you get the number.")

    
print("Game Over")

input("\n\nPress enter key to exit.")
