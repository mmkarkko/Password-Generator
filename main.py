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
scands = "ÅÄÖ"
numbers = "0123456789"
symbols = "!\"#%&/(){}[]=?^*+-_.:,;<>§@£$€"

# Password minimun and maximun legth
minLength = 8
maxLength = 30

userInput = ""  # User input variable
password = ""  # Password variable

scandsOrNo = False  # Variable to check if the password should contain scands
amountOfPws = 1  # How many passwords should be generated, default is 1
programRunning = True  # Variable to check if the program is running


###########################################################################
# This function asks the user if using scandic letter is allowed
#
# If the user answers yes, the program will add the scandic letters to the password
# Default is no
# @param rTheyOK = are scandic letters allowed in password or not
# @return True if the user wants to use scandic letters in the password
def areScandsOK(rTheyOK):

  # Loop until the user answers y/yes or n/no
  while not rTheyOK:
    answer = input(
        "Do you want to use scandic letters in your password? (y/n): ")
    if answer.lower() == "y" or answer.lower() == "yes":
      return True
    if answer.lower() == "n" or answer.lower() == "no":
      return False
    else:
      print("Please answer with y or n. Try again.")
  return rTheyOK


###########################################################################
# Checks if the input is a number and between the min and max lengths
#
# Keeps asking the input until it is correct
# @param minLength is the minimum length of the password
# @param maxLength is the maximum length of the password
# @return the input when it is correct
def checkUserInput(minLength, maxLength):

  # Loop until an input in a correct form is given
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
# Generates a random password. Length is defined by parameters
#
# @param length = the length of the password based of user input given earlier
# @param letrs  = the available letters for the password
# @param nums   = the available numbers for the password
# @param symbs  = the available symbols for the password
# @param scands = the available scandic letters for the password
# @param scandsOrNo = True if the password should contain scandic letters
# @return the generated password
def createPassword(length, letrs, nums, symbs, scands, scandsOrNo):
  lowercase = letrs.lower()  # Lowercase letters
  availableChars = letrs + lowercase + nums + symbs  # All available characters
  if scandsOrNo:
    availableChars += scands  # Add scandic letters if allowed, else not included

  # Generates a random password and returns it
  password = ''.join(secrets.choice(availableChars) for i in range(length))
  return password


###########################################################################
# Welcome to the program!!

print("Welcome to the password generator!", "", "", sep="\n")


# Calls for a function that asks for an input
# Sends in the parameters that are needed for the function
# After creating a password, asks if user wants to create another one
# @param howManyPws = how many passwords should be generated
# @param scandsOrNo = True if the password should contain scandic letters
def main(howManyPws, scandsOrNo):
  scandsOrNo = areScandsOK(scandsOrNo)
  userInput = checkUserInput(minLength, maxLength)
  password = createPassword(userInput, letters, numbers, symbols, scands,
                            scandsOrNo)
  print("Here is the generated password:", password)
  print()


###########################################################################
## Asks the user if the user wants to generate a password
# while programRunning is true, the program will keep asking the user
# If user wants to quit, programRunning is set to false

# Loops until the user answers y/yes or n/no
while programRunning:
  answer = input("Would you like to generate a password? ")
  if answer.lower() == "yes" or answer.lower() == 'y':
    main(amountOfPws, scandsOrNo)
  if answer.lower() == "no" or answer.lower() == 'n':
    programRunning = False
  else:
    print("Write y/yes to generate a password or n/no to exit the program.")

###########################################################################
# End of the program
