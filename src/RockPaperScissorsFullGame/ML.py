#Machine Learning functions for higher difficulties
import RPS
from enum import Enum

#Stores the results of each round in a dictionary: 
#{round : {"player" : playerchoice, "computer" :computerchoice}}.
rpsStorage = {}

#Arrays track the rounds for which the outcome occurs.
winsArr = []
lossesArr = []
tiesArr = []

#Variables track the number of rounds and outcomes.
round = 1
wins = 0
losses = 0
ties = 0

#Difficulties
class difficulty(Enum):
    Easy = 1
    Medium = 2
    Hard = 3

#Prompt the user for choice of difficulty and returns difficulty 
#if the difficulty begins with the input.
def chooseDifficulty() :
    playerInput = input("Enter your preferred difficulty (easy, medium, hard): ")
    if ("easy").startswith(playerInput.lower()): 
        return difficulty.Easy
    elif ("medium").startswith(playerInput.lower()): 
        return difficulty.Medium
    elif ("hard").startswith(playerInput.lower()): 
        return difficulty.Hard
    else:
        return None

#Stores the outcome of a round and players' choices (player and computer)
#in the rpsStorage dictionary. Tracks wins, losses, and ties.
def storeOutcome(outcome, playerChoice, computerChoice) :
    if (outcome == "Win") :
        kvp = {round : storeChoices(playerChoice, computerChoice)}
        rpsStorage.update(kvp)
        winsArr.append(round)
        round += 1
        wins += 1
        return kvp
    elif (outcome == "Lose") :
        kvp = {round : storeChoices(playerChoice, computerChoice)}
        rpsStorage.update(kvp)
        lossesArr.append(round)
        round += 1
        losses += 1
        return kvp
    elif (outcome == "Tie") :
        kvp = {round : storeChoices(playerChoice, computerChoice)}
        rpsStorage.update(kvp)
        tiesArr.append(round)
        round += 1
        ties += 1
        return kvp
    else :
        return None

#Creates the choices dictionary for rpsStorage (auxiliary function).
def storeChoices(playerChoice, computerChoice) :
    return {"player" : playerChoice, "computer" : computerChoice}

#Prints the current outcomes in rpsStorage 
def printRps() :
    if len(rpsStorage) == 0:
        print(0)
    for kvp in rpsStorage :
        print(kvp)

#Iterates through rpsStorage to check if the outcomes from a previous number
#of rounds before the current one has been repeated before. Returns the next
#expected outcome after the repeated interval of outcomes if there is a repeated
#segment. If there isn't a repeated segment, the previous number of rounds checked
#is decremented and checked again. This repetition occurs until number of rounds
#is lower than 2 (not really a segment).
def ML_historyMatching (numRounds) :
    resultsArr = rpsStorage.values()
    fractResultsArr = []
    while numRounds != 1 :
        for index in range(len(resultsArr) - numRounds, len(resultsArr), 1) :
            fractResultsArr.append(resultsArr[index])

        startIndex = find_subarray(resultsArr, fractResultsArr)
        if startIndex == None :
            fractResultsArr.clear()
            numRounds -= 1
        elif not (startIndex + numRounds >= len(resultsArr)):
            return resultsArr[startIndex + numRounds]

    return None

#Checks if the first array contains the second array.
def find_subarray(first_arr, second_arr):
    first = 0
    second = 0

    first_len = len(first_arr)
    second_len = len(second_arr)

    while first < first_len and second < second_len:
        #From the beginning of each array, every element is matched to check
        #for an equality.
        if first_arr[first] == second_arr[second]:
            first += 1
            second += 1

            #If the second array is completed (has every element equal
            #to an element in the first array in the same order), 
            #second array is contained within the first array.
            if second == second_len:
                return first - second_len

        else:
            #If the second array's element doesn't match the first array's 
            #element, it has to be reset. Likewise, if the second array is
            #reset, the first array has to be checked again from the next 
            #element after the first element which matched the second array's 
            #first element.
            first = first - second + 1
            second = 0

    return None


        
    




    
    
    

