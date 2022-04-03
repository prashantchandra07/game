import string
import random

letters = string.ascii_lowercase
rnd = random.choice(letters)
flag = 0

def take_input():
    guess_letter = input('Only 1st letter will be considered for matching : ')[0]
    if guess_letter.lower() not in letters:
        flag = 1
        print("Error...!!! It's not an alphabet")
        exit()
        
    return(guess_letter)

guess_letter = take_input()

def check_user_input(guess_letter,flag):
    if flag == 1:
        exit()
        
    if guess_letter == rnd:
        print("\t\tHurray...!!\n\tYou Guessed it correctly.")
    else:
        print("\t\tOppssss....!!\n\tYou Missed it. The Letter was {}".format(rnd))

check_user_input(guess_letter,flag)