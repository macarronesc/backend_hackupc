# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess
from asyncore import poll
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listWorkers = []

    numWorkers = 8005 + len(listWorkers)
    print(len(listWorkers))

    print("Creating Party: ")
    print("Party: http://localhost:" + str(numWorkers))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def existentWordInDictionary(word):
    exist = False
    file = open("0_palabras_todas.txt")
    for line in file.readlines():

        if (line.lower() == word.lower()):
            exist = True
    file.close()
    return exist



def getPosition(lenght):
    possi = lenght / 2
    rand = random.randint(0, possi)
    return rand

oldWord = "pato"


def correctWord(word):
    correct = False
    part = getPosition(len(word))
    print(existentWordInDictionary(word))
    if existentWordInDictionary(word) and oldWord[part:part + 2].lower() == word[0:2].lower():
        correct = True
        return correct

    return correct

print(correctWord("todo"))