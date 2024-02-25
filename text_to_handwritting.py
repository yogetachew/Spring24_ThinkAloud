"""
    FileName: speed_calculator.py
    Name: Yonatan Getachew
    Date: 02/24/2024
    Purpose: 
"""

# import time and random
from time import *
import random as r

# define mistake so that it can identify the error
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput)/ time_r
    return round(speed)

# Sentence used to check your speed and error
test =["A paragraph is a self contained unit of discourse in writing dealing with a particular point or idea."]

test1 = r.choice(test)
print(" ||============== Typing Speed =========|| ")
print(test1)
print()
print()
time_1 = time()
testinput = input("  Enter : ")
time_2 = time()

print('Speed : ', speed_time(time_1,time_2,testinput), " words/sec")
print("Error : ", mistake(test1,testinput))