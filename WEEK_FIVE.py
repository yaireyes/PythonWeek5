################################################################

                        #Yaisiel Reyes

################################################################

import random
import time
import os
import config
import numpy as np


# Time needed 2 hours

retry = True
while retry:
    print("1. Press 1 to play 'Let the computer guess the Number': ")
    print("2. Press 2 for Naive/Binary Index Search of given target Number from List: ")
    print("3. Press 3 to send a text to your Given number: ")
    print("4. Exit")

    menu = input("Please Choose from the menu (1, 2, 3, 4)   ")

    if menu == "1":
            def guess(x):
                random_number = random.randint(1, x)
                guess = 0
                while guess != random_number:
                    guess = int(input(f'Guess a number between 1 and {x}: '))
                    if guess < random_number:
                        print('Sorry, guess again. Too low.')
                    elif guess > random_number:
                        print('Sorry. guess again. Too high.')
                print(f'Yay, Congrats. You have guessed the number {random_number} correctly!')

            def computer_guess(x):
                low = 1
                high = x
                feedback = ''
                while feedback != 'c':
                    if low != high:
                        guess = random.randint(low, high)
                    else:
                        guess = low # could also be high b/c low = high
                    feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
                    if feedback == 'h':
                        high = guess - 1
                    elif feedback == 'l':
                        low = guess + 1
                print(f'Yay, The Computer guessed the number {guess} correctly!')
            computer_guess(20)

    elif menu == "2":
        #Implementation of binary search!
        #We will prove that binary search is faster than naive search
        #Naive Search: Scan entire list and ask if its equal to the target.
        #if Yes, return the index
        #If No, then return -1
            def naive_search(l, target):
                #Example l = [1, 3, 10, 12]
                for i in range(len(l)):
                    if l[i] == target:
                        return i
                return -1

        #binary search uses divide and conquer!
        #I will leverage the fact that our list is SORTED
            def binary_search(l, target, low=None, high=None):
                if low is None:
                    low = 0
                if high is None:
                    high = len(l) -1

                if high < low:
                    return -1

                #Example l [1, 3, 5, 10, 12] #should return 3
                midpoint = (low + high) // 2 #2
                if l[midpoint]  == target:
                    return midpoint
                elif target < l[midpoint]:
                    return binary_search(l, target, low, midpoint-1)
                else:
                    target > l[midpoint]
                    return binary_search(l, target, midpoint+1, high)
            if __name__=='__main__':
                l = [1, 3, 5, 10, 12, 16, 22]
                target = 12 # should return 4
                print(l)
                print("The Index for the Target Number using Naive Search is: ")
                print(naive_search(l, target))
                print("The Index for the Target Number using Binary Search is: ")
                print(binary_search(l, target))

    elif menu == "3":
        def get_words(file_path):
            with open(file_path, 'r') as f:
                text = f.readlines()[0]
                words = text.split()
            return words


        def get_lines(file_path):
            with open(file_path, 'r') as f:
                text = f.readlines()
            return text


        def send_message(phone_number, message):
            os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

        def phone_number():
            # put your phone number into the string!
            phone_number = input("Enter your phone number: ")
            print(f'Sending text to: ' + f' {phone_number}')
            print('{}-{}-{}'.format(phone_number[:3],phone_number[3:6],phone_number[6:]))

        if __name__ == '__main__':
            # if your number is 123456789, the next line should look like this: phone_number = '123-456-7890'
            phone_number = phone_number()
            words = get_words('miracle.txt')
            for word in words:
                send_message(phone_number, word)

    elif menu == "4":
        retry = False
        print("Sorry to See You Go")
    else:
        print("Invalid selection, Please try 1, 2, 3, or 4")

# Time spent 5 hours and 38 minutes
