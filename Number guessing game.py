import random
num=random.randint(1,100)
apt=0 #attempt=0
gnum=None
name=input("enter your name:")
print("Hello {}!! Welcome to the NUMBER GUESSING GAME".format(name))
print("Guess the number if you can")
while gnum!=num:
    try:
        gnum=int(input("enter your guessed number:"))
        apt=apt+1
        if gnum<num:
            print("Too Low!!try again")
        elif gnum> num:
            print("Too High!! try again")
        else:
            print("Correct guess!! The number is {}".format(num))
            print("You guessed it in {} attempts".format(apt))
    except ValueError:
        print("Please enter a valid number between 1-100!!")
