## PP: make a code that guess the users number that is between 1 - 1000
import random ## random
import math ## helps with rounding

## while loops
x = 0;y = 0

while x < 1:
    play = input("Would you like to play? Y/N ")
    if play == 'Y':
        ## PP: give "Craig" a number to guess
        Num = int(input("Give a number, that is 1-1000, for Craig to guess: "))
        if Num < 1 or Num > 1000:
            print("Try Agian...")
        else:
            break ## leave the loop
    elif play == 'N':
        Num = random.randint(1, 1000)
        break
    else:
        print("Try Again...")

print("Your number is {}" .format(Num)) 
print("-_-_-_-_-_-_-_-_-_-")

## be able to change the high and low
def Game(low, high):
    count = 0; first = 0
    CraigGuess = 500 ## set the first guess
    while y < 1:
        count+=1
        '''
        if count == 12: ##Testing Purposes
            break
        '''
        if  CraigGuess > Num: ## too high
            print("Craig guessed {}. Craig guess is too high" .format(CraigGuess))
            high = CraigGuess
            CraigGuess = math.trunc(((low+high)/2))      
        elif CraigGuess < Num: ## too low
            print("Craig guessed {}. Craig guess is too low" .format(CraigGuess))
            low = CraigGuess
            CraigGuess = math.trunc(((low+high)/2))
        else: ## Success!
            break
        if high - 1 == low + 1 : ## since both numbers are guessed it guesses the middle one
            CraigGuess=high-1
        
    ## winner winner chicken dinner
    print("Craig guessed your number!! Your number is {}" .format(CraigGuess))
    print("Took Craig {} guesses" .format(count))
    print("-_-_-_-_-_-_-_-_-_-")

## Run function    
if __name__ == '__main__': 
    Game(1,1000)