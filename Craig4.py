## PP: This Craig will be utilizing Binary search to increase search time
## this is hard because its not guessing anymore it is effectively searching

## o(log n)

import random
import time
start_time = time.time()

def BinaryS(nums,low,high,ran):
    
    global count
    count+=1

    if high >= low:
        middle = (high + low)//2

        if middle == ran:
            print("Craig guessed {}. Craig guess is too high" .format(middle))
            print("Took Craig {} guesses" .format(count))

            global RealCount
            RealCount = RealCount + count
            print("-_-_-_-_-_-_-_-_-_-")
            return middle
        elif middle > ran:
            print("Middle is ", str(middle))
            return BinaryS(nums, low, middle-1,ran)
        else:
            
            print("Craig guessed {}. Craig guess is too low" .format(middle))
            return BinaryS(nums, middle+1,high,ran)
    

if __name__ == '__main__':
    
    start_time = time.time()
    p = 0
    RealCount = 0
    nums = [*range(1,1001,1)]
    count = 0
    print(len(nums))

    while p < 100:
        ran = random.randint(1, 1000)
        print("Your number is ", str(ran))
        BinaryS(nums, 0, len(nums), ran)
        count = 0
        p+=1
    print(RealCount/p)
    print("--- %s seconds ---" % (time.time() - start_time))



    


