# Number-Guesser

These are fun little projects that I randomly think of and start working on. they are for me to refresh my knowledge of Python.

## Craig's  

My goal is to try to have Craig Guess the user's number with the least number of guesses. Craig uses a random number to make a guess that is between 1-1000

### Craig.py
Give Craig a number and Craig will try to guess the number that the user gives. </br>
    -This version of Craig is all base on luck and random numbers with narrowing down his range. </br>
        -when Craig guesses, it is compared to the user's number and sees if it is higher or lower. If it is higher or lower than the users' number Craig will change his range to his guess plus 1. </br>
            -EX: Craig guesses 345. Users number is 543. Craig's number is lower than the users. Craig changes his range from 1-1000 to 346-1000</br>
    -His average guess is 12.5 out of 10 tries. 7-18 guesses range </br>

### Craig2.py
I took a different approach at this. I wanted to start the number guess by seeing if the users number is higher or lower than 500. by doing this i have cut the numbers range in half hoping to make it easier for Craig2

## User Guess

User Guess.py
The user makes a guess. it will count the number of guesses through recurrence.

