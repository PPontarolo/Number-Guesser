## PP: make a code that guess the users number that is between 1 - 1000
import random ## random
import math ## this is used to round the numbers

## while loops
x = 0;y = 0

while x < 1:
    ## PP: give "Craig" a number to guess
    Num = int(input("Give a number, that is 1-1000, for Craig to guess: "))
    if Num < 1 or Num > 1000:
        print("Try Agian...")
    else:
        break ## leave the loop

print("Your number is {}" .format(Num))
print("-_-_-_-_-_-_-_-_-_-")

## be able to change the high and low
def Game(low, high):
    count = 0
    CraigGuess = 500

    while y < 1:
        
        count+=1

        if  CraigGuess > Num: ## too high
            print("Craig guessed {}. Craig guess is too high" .format(CraigGuess))
            high = CraigGuess

            CraigGuess = math.trunc(CraigGuess/2)
        elif CraigGuess < Num: ## too low
            print("Craig guessed {}. Craig guess is too low" .format(CraigGuess))
            low = CraigGuess
        else: ## Success!
            break


    ## winner winner chicken dinner
    print("Craig guessed your number!! Your number is {}" .format(CraigGuess))
    print("Took Craig {} guesses" .format(count))
    print("-_-_-_-_-_-_-_-_-_-")

## Run function    
if __name__ == '__main__': 
    Game(1,1000)