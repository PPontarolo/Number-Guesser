## PP: make a code that guess the users number that is between 1 - 100
import random ## random

## while loops
x = 0
y = 0

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
    while y < 1:
        
        RanNum = random.randint(low, high)

        if RanNum == Num: ## Success
            print("Craig guessed your number!! Your number is {}" .format(RanNum))
            count+=1
            print("Took Craig {} guesses" .format(count))
            break ## Leave the loop
        elif RanNum > Num: ## too high
            print("Craig guessed {}. Craig guess is too high" .format(RanNum))
            high = RanNum - 1
            #print("{} - {}" .format(low,high)) ## PP: used this for testing purposes
            count+=1
        elif RanNum < Num: ## too low
            print("Craig guessed {}. Craig guess is too low" .format(RanNum))
            low = RanNum + 1
            #print("{} - {}" .format(low,high)) ## PP: used this for testing purposes
            count+=1
    print("-_-_-_-_-_-_-_-_-_-")


## Run function    
if __name__ == '__main__': 
    Game(1,1000)