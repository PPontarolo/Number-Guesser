import random

RanNum = random.randint(1, 100)

def Game(count=1): ## user always will have one guess
    guess = int(input("Take a Guess: "))

    if guess == RanNum:
        print("=====Congrats, Huge Dub!=====")
        print("Took {} guesses" .format(count))
    elif guess < RanNum:
        print("you are less than the number")
        Game(count+1)
    else:
        print("You are greater than the number")
        Game(count+1)

## Call the function above
if __name__ == '__main__':
    Game()