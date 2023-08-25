## PP: This Craig will be utilizing Binary search to increase search time
## this is hard because its not guessing anymore it is effectively searching

## o(log n)

import random ## for the random number to guess
import time ## for testing the program time
start_time = time.time() ## Start

def BinaryS(arr,low,high,ran):
    
    global count
    count+=1

    if high >= low: ## always goes in here
        middle = (high + low)//2

        if middle == ran: ## guessed the number
            print("Craig guessed your number!! Your number is {}" .format(middle))
            print("Took Craig {} guesses" .format(count))

            ## for overall average
            global RealCount
            RealCount = RealCount + count

            print("-_-_-_-_-_-_-_-_-_-")
            return middle
        elif middle > ran: ## too high
            print("Craig guessed {}. Craig guess is too high" .format(middle))
            return BinaryS(arr, low, middle-1,ran) ## change high
        else: ## too low
            print("Craig guessed {}. Craig guess is too low" .format(middle))
            return BinaryS(arr, middle+1,high,ran) ## change low
    ## dont need an else because it will always be within the bounds of the range
    

if __name__ == '__main__':
    
    start_time = time.time()
    p = 0;RealCount = 0;count = 0;arr = [*range(1,1001,1)]
    
    while p < 100:
        ran = random.randint(1, 1000)
        print("Your number is ", str(ran))
        BinaryS(arr, 0, len(arr), ran)
        count = 0
        p+=1

    print(RealCount/p) ## gives the average of guesses
    print("--- %s seconds ---" % (time.time() - start_time)) ## Stop



    


