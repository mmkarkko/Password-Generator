###########################################################################
# PASSWORD GENERATOR
# @mmkarkko
# Version 1.0
# A program that generates a random password based on user input

# 7.3.2024  Start of the project

###########################################################################
# imports

import random

###########################################################################
# Possible characters of the password

#Characters that are allowed in the password
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
lowercase = uppercase.lower()
numbers = "0123456789"
symbols = "!\"#¤%&/(){}[]=?`´^*+-_.:,;<>§@£$€"

# Password minimun and maximun legth
minLength = 10
maxLength = 30

userInput = ""  # User input variable
password = ""  # Password variable
#programRunning = True  # Program running variable

###########################################################################
# Variables that are involved with testing

isCorrect = "Correct, it contains only numbers"
notCorrect = "Incorrect, it contains characters other than numbers"

###########################################################################
# checks the given input


def checkUserInput(minLength, maxLength):
  while True:
    userInputtoCheck = input("Enter a number between {} and {}: ".format(
        minLength, maxLength))
    if userInputtoCheck.isdigit():
      userInputtoCheck = int(userInputtoCheck)
      if minLength <= userInputtoCheck <= maxLength:
        break
      else:
        print("The input was not between {} and {}. Please try again.".format(
            minLength, maxLength))
    else:
      print("The input was not a number. Please try again.")
  return userInputtoCheck


###########################################################################
# Welcome to the program!!

print("Welcome to the password generator!", "", "", sep="\n")

userInput = checkUserInput(minLength, maxLength)

print("We're here!! It's the end of it!"
      )  # TODO: remove, For checking purposes only

###########################################################################
# Making random password based on user input

###########################################################################
# eof
