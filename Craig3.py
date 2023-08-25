## PP: make a code that guess the users number that is between 1 - 1000

## o(1)

import random ## random
import math ## helps with rounding
import time ## for testing the program time
start_time = time.time() ## Start

'''
while 1==1:
    play = input("Would you like to play? Y/N ")
    if play == 'Y':
        ## PP: give "Craig" a number to guess
        Num = int(input("Give a number, that is 1-1000, for Craig to guess: "))
        if Num < 1 or Num > 1000:
            print("Try agian...")
        else:
            break ## leave the loop
    elif play == 'N':
        Num = random.randint(1, 1000)
        break
    else:
        print("Try Again...")

print("Your number is {}" .format(Num)) 
print("-_-_-_-_-_-_-_-_-_-")
'''

## be able to change the high and low
def Game(low, high):
    count = 0; first = 0;Num = random.randint(1, 1000)
    
    print("Your number is ", str(Num))
    CraigGuess = 500 ## set the first guess
    while 1==1:
        count+=1

        if  CraigGuess > Num: ## too high
            print("Craig guessed {}. Craig guess is too high" .format(CraigGuess))
            high = CraigGuess
            CraigGuess = math.trunc(((low+high)/2))      
        elif CraigGuess < Num: ## too low
            print("Craig guessed {}. Craig guess is too low" .format(CraigGuess))
            low = CraigGuess
            CraigGuess = math.trunc(((low+high)//2))
        else: ## Success!
            break
        if high - 1 == low + 1 : ## since both numbers are guessed it guesses the middle one
            CraigGuess=high-1
        
    ## winner winner chicken dinner
    print("Craig guessed your number!! Your number is {}" .format(CraigGuess))
    print("Took Craig {} guesses" .format(count))
    print("-_-_-_-_-_-_-_-_-_-")

    ## Getting the Average of the Count
    global RealCount
    RealCount = RealCount + count

## Run function    
if __name__ == '__main__':
    p = 0
    RealCount = 0
    while p < 100: 
        Game(1,1000)
        p+=1
    print(RealCount / p) ## gives the average of guesses
    print("--- %s seconds ---" % (time.time() - start_time))