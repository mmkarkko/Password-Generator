###########################################################################
# PASSWORD GENERATOR
# @mmkarkko
# Version 1.0
# A program that generates a random password based on user input

# 7.3.2024  Start of the project

###########################################################################
# imports

import random
import secrets

###########################################################################
# Possible characters of the password

#Characters that are allowed in the password
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
scands  = "ÅÄÖ"
numbers = "0123456789"
symbols = "!\"#%&/(){}[]=?^*+-_.:,;<>§@£$€"

# Password minimun and maximun legth
minLength = 8
maxLength = 30

userInput = ""  # User input variable
password = ""  # Password variable

scandsOrNot    = False  # Variable to check if the password should contain scands
programRunning = True

###########################################################################
# Variables that are involved with testing

isCorrect = "Correct, it contains only numbers"
notCorrect = "Incorrect, it contains characters other than numbers"

###########################################################################
# Checks the given input
# Checks if the input is a number and between the min and max lengths
# Keeps asking the input until it is correct
# Returns the input if it is correct
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
# Generates a random password. Length is defined by arguments
# Returns the generated password
#
# length = the length of the password based of user input given earlier
# letrs  = the available letters for the password
# nums   = the available numbers for the password
# symbs  = the available symbols for the password

def createPassword(length, letrs, nums, symbs):
  lowercase = letrs.lower()  # Lowercase letters
  availableChars = letrs + lowercase + nums + symbs  # All available characters

  # Generates a random password
  password = ''.join(secrets.choice(availableChars) for i in range(length))

  return password


###########################################################################
# Welcome to the program!!

print("Welcome to the password generator!", "", "", sep="\n")

# Calls for a function that asks for an input
# Sends in the parameters that are needed for the function
# After creating a password, asks if user wants to create another one
#while programRunning:

def main():
  userInput = checkUserInput(minLength, maxLength)
  password = createPassword(userInput, letters, numbers, symbols)
  print("Here is the generated password:", password)

###########################################################################
## Asks the user if the user wants to generate a password

while programRunning:
  answer = input("Would you like to generate a password? ")
  if answer.lower() == "yes" or answer.lower() == "y" and :
    main()
  else:
    programRunning = False

###########################################################################
# End of the program