from enum import Enum
import random
import ML

#Denotes instances of Item (plays) with values assigned to them.
class Item(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

#Denotes instances of Outcome (results) with values assigned to them.
class Outcome(Enum):
    Win = 1
    Lose = 2
    Tie = 3

#Accepts two choices (player and computer) and outputs the outcome of the round.
def getOutcome(playerItem, computerItem):
    if(playerItem.value == computerItem.value):
        ML.storeOutcome(Outcome.Tie, playerItem.name, computerItem.name)
        return Outcome.Tie
    elif((playerItem == Item.Rock and computerItem == Item.Scissors) or (playerItem.value == computerItem.value + 1)):
        ML.storeOutcome(Outcome.Win, playerItem.name, computerItem.name)
        return Outcome.Win
    else:
        ML.storeOutcome(Outcome.Lose, playerItem.name, computerItem.name)
        return Outcome.Lose

#Randomizes a number between 1 and 3, and returns the Item (rock, paper, scissors)
#associated with the random number.
def getComputerItem():
    index = random.randint(1,3)
    return Item(index)

#Checks if the input is in the beginning of rock, paper, or scissors.
#Returns appropriate instance associated with the input.
def inputToItem(str):
    if ("rock").startswith(str.lower()):
        return Item.Rock
    elif ("paper").startswith(str.lower()):
        return Item.Paper
    elif ("scissors").startswith(str.lower()):
        return Item.Scissors
    else:
        return None