# Number-Guesser

These are fun little projects that I randomly think of and start working on. They are for me to refresh my knowledge of Python.

## Craig's 

Goal: The goal is to try to have Craig Guess the user's number with the least number of guesses. Craig uses a random number to make a guess that is between 1-1000 </br>
Average: When finding the average I am checking with only the number 345, and only doing 10 attempts in a row

>### Craig.py
>Give Craig a number and Craig will try to guess the number that the user gives. This version of Craig is all base on luck and random numbers with narrowing down his range. </br>
>    - When Craig guesses, it is compared to the user's number and sees if it is higher or lower. If it is higher or lower than the users' number Craig will change his range to his guess plus 1. </br>
>       - EX: Craig guesses 345. Users number is 543. Craig's number is lower than the users. Craig changes his range from 1-1000 to 346-1000</br>
>       - Craig average guess is 12.13 out of 100 tries. Guessing number was random </br>

>### Craig2.py
>I took a different approach to this. I wanted to start the number guess by seeing if the user's number is higher or lower than 500. by doing this I have cut the numbers range in half hoping to make it easier for Craig2 </br>
><i>Promise to change the names, but as of now, it's Craig and Craig2</i></br>
>    - Craig2 has the same guess and change range process as Craig.py, besides having the 500 higher or lower check before entering the loop </br>
>       - Craig2 average guess is 11.27 out of 100 tries. Guessing number was random </br>
>       - (1-(11.27/12.13))*100 ≈ 7.09% increase 

>### Craig3.py O(1)
>After doing some research I discovered that the best way of finding a number with a range of 1-1000 is finding the average of the low and high range. </br>
>    - Craig3 starts with a guess of 500 and then finds if it's higher or lower than the user's guess.</br>
>    - Craig3 then finds the average of the high and low to make another guess and repeats that till reaches the users guess</br>
>    - if the range is one higher and one lower than the users guess, Craig will guess the middle number
>      - Craig3 average guess is 8.84 out of 100 tries. Guessing number was random
>      - (1-(8.84/12.13))*100 ≈ 27.12% increase from Craig
>      - (1-(8.84/11.27))*100 ≈ 21.57% increase from Craig2

>### Craig4.py O(log n)
>My goal for Craig4 is to use recursions. I used a binary search instead of a while loop, like Craig3. </br>
>This is not faster or any ways better than Craig3. Since it has a Big o(log n) it is not constant and will be slower than Craig3. but not by much.</br>
>The average is the same as Craig3 so it is not any way better
>   - Binary search
>       - Craig3 average guess is 8.89 out of 100 tries. Guessing number was random

>### CraigBin.py (In the works)
>CraigBin is going to be a number guesser but is doing it with the binary numbers. the range is 1-1024.</br>
>Goal: to have CraigBin guess average be under 9.6 </br>
> 


## User Guess

User Guess.py
The user makes a guess. It will count the number of guesses through recurrence.

