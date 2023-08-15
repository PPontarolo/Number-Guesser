# Number-Guesser

These are fun little projects that I randomly think of and start working on. they are for me to refresh my knowledge of Python.

## Craig's 

Goal: The goal is to try to have Craig Guess the user's number with the least number of guesses. Craig uses a random number to make a guess that is between 1-1000 </br>
Average: When finding the average I am checking with only the number 345, and only doing 10 attempts in a row

> ### Craig.py
> Give Craig a number and Craig will try to guess the number that the user gives. </br>
>    -This version of Craig is all base on luck and random numbers with narrowing down his range. </br>
>>        -when Craig guesses, it is compared to the user's number and sees if it is higher or lower. If it is higher or lower than the users' number Craig will change his range to his guess plus 1. </br>
>>            -EX: Craig guesses 345. Users number is 543. Craig's number is lower than the users. Craig changes his range from 1-1000 to 346-1000</br>
>    -His average guess is 12.5 out of 10 tries. 7-18 guesses range </br>

### Craig2.py
I took a different approach to this. I wanted to start the number guess by seeing if the user's number is higher or lower than 500. by doing this I have cut the numbers range in half hoping to make it easier for Craig2 </br>
<i>Promise to change the names, but as of now, it's Craig and Craig2</i></br>
    > - Craig2 has the same guess and change range process as Craig.py, besides having the 500 higher or lower check before entering the loop </br>
    > - Craig2 average guess is 12.4 out of 10 tries. 8-19 guesses range </br>

### Craig3.py
After doing some research I discovered that the best way of finding a number with a range of 1-1000 is finding the average of the low and high range. </br>
    > -Craig3 starts with a guess of 500 and then finds if it's higher or lower than the users guess.</br>
    > -Craig3 then finds the average of the high and low to make another guess and repeats that till reaches the users guess</br>
    > -if the range is one higher and one lower than the users guess, Craig will guess that middle number

## Findings on Craig
<b>8/12</b>: As I am designing and perfecting Craig, I am starting to realize that lowering the number of guesses will be almost impossible with a random num guesser. The main component I can change is the run time. I will keep trying to get the guess attempts lowered but I will also start focusing on the run time. </br>

Though a shorter run time would be impressive, also not consistent, just like the guess attempts. </br>

<b>8/14</b>: After doing Research I have found that 10 is the highest number of guesses someone needs to make while doing the most effective way of finding that number. The process is starting at 500, like Craig2.py, but keeps changing the range in half. This will make the formula (low+high)/2 (Average) till the number is found. </br>

Craig3 works under 1-10 tries. He does the formula above and works great. I am using the library math to round the numbers up or down based on rounding rules. </br>



## User Guess

User Guess.py
The user makes a guess. it will count the number of guesses through recurrence.

