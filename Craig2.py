## PP: make a code that guess the users number that is between 1 - 1000
import random ## random

print("This is Craig2") ## so i can keep track
## PP: Got rid of the user side of this to test it
'''

while 1 == 1:
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

    ## made it always random
    Num = random.randint(1, 1000)
    count = 0

    ## 500 check to cut the range into half
    count+=1
    if Num > 500:
        low = 500
    elif Num < 501:
        high = 500
    else:
        ## just in case that the number is 500
        print("Craig guessed your number!! Your number is {}" .format(RanNum))
        print("Took Craig {} guesses" .format(count))
        
    while 1==1:
        
        RanNum = random.randint(low, high)
        count+=1
        if RanNum == Num: ## Success
            print("Craig guessed your number!! Your number is {}" .format(RanNum))
            print("Took Craig {} guesses" .format(count))
            break ## Leave the loop
        elif RanNum > Num: ## too high
            print("Craig guessed {}. Craig guess is too high" .format(RanNum))
            high = RanNum - 1
        elif RanNum < Num: ## too low
            print("Craig guessed {}. Craig guess is too low" .format(RanNum))
            low = RanNum + 1
    #print("{} - {}" .format(low,high))
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
    print(RealCount / p)