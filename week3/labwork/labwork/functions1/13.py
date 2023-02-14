def ran(x,n,c):
    b=int(input())
    if b>n:
        c=c+1
        print("Your guess is too high.\n"+"Take a guess.\n")
        return ran(x,n,c)
    if b<n:
        c=c+1
        print("Your guess is too low.\n"+"Take a guess.\n")
        return ran(x,n,c)
    if b==n:
        c=c+1
        print("Good job, "+x+"! You guessed my number in "+str(c)+" guesses!")
        return 0


import random
print("Hello! What is your name?")
n = random.randint(1, 20)
a=input()
print("Well, "+a+", I am thinking of a number between 1 and 20.\n"+"Take a guess.\n")
ran(a,n,0)