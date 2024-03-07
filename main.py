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
lowercase = "abcdefghijklmnopqrstuvwxyzåäö"
numbers = "0123456789"
symbols = "!\"#¤%&/()=?`´^*+-_.:,;<>§"

# Password minimun and maximun legth
minLength = 15
maxLength = 30

# Other variables
userInput = ""
password = ""

###########################################################################
# Variables that are involved with testing

isCorrect = "Correct, it contains only numbers"
notCorrect = "Incorrect, it contains characters other than numbers"

###########################################################################
# Checking if input only contains numbers
# Keeps asking, until input contains only numbers


def isOnlyNumbers(userInput):
  return userInput.isdigit()


def getNumericInput():
  userInput = input("Enter number of characters: ")
  while not isOnlyNumbers(userInput):
    userInput = input("Enter numbers only. Please try again: ")
  return userInput


###########################################################################
# Welcome to the program!!

print("Welcome to the password generator!", "", "", sep="\n")

userInput = getNumericInput()

print("User's input was:",
      userInput)  # TODO: remove, For checking purposes only
print("We're here!!")  # TODO: remove, For checking purposes only

###########################################################################
#

###########################################################################
# eof
