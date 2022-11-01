#Machine Learning functions for higher difficulties
import RPS

rpsStorage = {}
winsArr = []
lossesArr = []
tiesArr = []
round = 1
wins = 0
losses = 0
ties = 0

class difficulty(Enum):
    Easy = 1
    Medium = 2
    Hard = 3

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

def storeChoices(playerChoice, computerChoice) :
    return {"player" : playerChoice, "computer" : computerChoice}

def machineLearning_
    




    
    
    

