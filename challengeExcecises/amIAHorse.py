#!/usr/bin/env python3

"""
Author: Jane

This program allows a user to type in input to answer the questions posed by the flowchart "AM I A HORSE?"
"""

def printResult(n):
    if n == 1:
       print("You're not a horse!\n")
    else:
       print("Exit current flowchart!\n")

def legs():
    answer1 = input("How many legs do you walk on? (Two, Four) \n").title()
    if answer1 == "Two":
        printResult(1)
    elif answer1 == "Four":
        really()
    elif answer1 == "Q":
        printResult(0)
    else:
        legs()

def readAndWrite():
    answer3 = input("Can you read and write? (Yes, No) \n").title()
    if answer3 == "Yes":
        printResult(1)
    elif answer3 == "No":
        print("Liar, You're reading this.\n")
        printResult(1)
    elif answer3 == "Q":
        printResult(0)
    else:
        readAndWrite()

def really():
    answer2 = input("Really?(No, Yes) \n").title()
    if answer2 == "No" or answer2 == "Yes":
        readAndWrite()
    elif answer2 == "Q":
        printResult(0)
    else:
        really()

def horse():
    answer = input("Are Your A Horse?(No, Yes, Maybe) \n").title()
    if answer == "No":
        printResult(1)
    elif answer == "Yes":
        legs()
    elif answer == "Q":
        printResult(0)
    elif answer == "Maybe":
        legs()
    else:
        horse()



def main():
    horse()
main()