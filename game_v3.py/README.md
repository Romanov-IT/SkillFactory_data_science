# Project 01. game_v3.py
## Task description
The computer generates a random integer between 1 and 100. Needs to create a program for guess the random number.
## Task conditions
* no more 20 attempts for guess the random number.
* the program takes into account: more or less number than random number.
## Qwality evaluation
The result evaluated for mean value of 10000 attempts.
## Objectives of task
* Phython code practic.
* IDE practic.
* GitHub practic.
## Task solve
The task is solved by dividing the list in half. If the random number is greater than the middle value of the list, then the list divided in half from middle value to end, or from middle to start, if random number is less then middle value. Middel value is mean middel by index, not by value.
## Сonclusion
The mean value for the 10000 attempts is 5.32. The task is   solved successfully. 
In conclusion, I can add that this method helps you guess a random number in 7 attempts from 1 to 128,  or 8 attempts from 1 to 256 etc. Becouse 2^7 = 128, it's mean, that value '128' I can divide in half 7 times.