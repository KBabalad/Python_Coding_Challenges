# this program takes an input from the user to check whether the given word is a palindrome or not
import re

def evaluate_palindrome(phrase):
        forwards = ''.join(re.findall(r'[a-z]+', phrase.lower())) # refer to re import function for this info
        backwards = forwards[::-1] # to-do # understand this logic how it workS?
        if forwards == backwards: 
            print("True")
        else:
            print("False")
        return

if __name__ == '__main__':
    usr_input = input ("Enter a string \n")
    usr_input = str(usr_input)
    evaluate_palindrome(usr_input)
