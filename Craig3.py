## PP: make a code that guess the users number that is between 1 - 1000
import random ## random

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
    count = 0; first = 0
    CraigGuess = 500.0

    while y < 1:

        count+=1
        if count == 6: ## debugging
            break  
        if  CraigGuess > Num: ## too high
            print("Craig guessed {}. Craig guess is too high" .format(CraigGuess))
            #high = (low+high)/2 + 1
            if first==0:
                high = CraigGuess-1
                CraigGuess = ((low+high)/2 )- 1
                first+=1
            else:
                high = CraigGuess
                CraigGuess = ((low+high)/2 )- 1
                
        elif CraigGuess < Num: ## too low
            print("Craig guessed {}. Craig guess is too low" .format(CraigGuess))
            #low = (low+high)/2 - 1
            if first==0:
                low = CraigGuess+1
                CraigGuess = ((low+high)/2 )+ 1
                first+=1
            else:
                low = CraigGuess
                CraigGuess = ((low+high)/2 )+ 1  
        else: ## Success!
            break



    ## winner winner chicken dinner
    print("Craig guessed your number!! Your number is {}" .format(CraigGuess))
    print("Took Craig {} guesses" .format(count))
    print("-_-_-_-_-_-_-_-_-_-")

## Run function    
if __name__ == '__main__': 
    Game(1,1000)