import random
import math

a = random.randint(1,100)
count = 0

def take_user_input():
    try:
        guess = int(input())
        return guess
    except:
        print("\t\tERROR...!!!!\n\t\tPlease Enter a Number")
        exit()

guess = take_user_input()

def check_user_response(guess,count,a):
    try:
        flag = 0
        if guess == a:
            print("\t\tHurray !!\n\t\tYou Guessed it correctly")
            flag = 1
            exit()

        if count<2 and flag == 0:
            if guess<a:
                print("The number is higher")
            else:
                print("The number is lower")

            count = count+1
            guess = take_user_input()
            check_user_response(guess,count,a)

        else:
            if flag == 0:
                print("\t\tOPPIEESSS.....!!\n\t\tYou Missed it")
                print("\t\tThe number was",a)
            
    except:
        pass


check_user_response(guess,count,a)
