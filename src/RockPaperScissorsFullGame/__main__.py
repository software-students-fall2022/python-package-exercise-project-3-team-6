# import RockPaperScissorsFullGame.RPS as RPS
import RPS
import ML

def main():
    #first ask user if they want to see ascii art
    asciiVisibility = RPS.setAsciiVisibility()
    
    #Prompting game difficulty
    difficulty = ML.chooseDifficulty()
    if (difficulty.value == 1) :
        print("You chose difficulty! Computer will be on random mode.") 
    elif (difficulty.value == 2) :
        print("You chose medium difficulty! Computer will be using history matching.")
    elif (difficulty.value == 3) :
        print("You chose hard difficulty! Computer will be using history matching.")

    # game
    play = True
    round = 1
    while (play):
        #Initialize computer choice (computerItem) to None during the start of every round.
        computerItem = None

        #Easy mode: randomizes and returns an rps item for the computer choice.
        if (difficulty.value == 1) :
            computerItem = RPS.getComputerItem()

        #Medium mode: calls ML_historyMatching() to make the computer choice.
        elif (difficulty.value == 2) :
            #Current round has to be at least 3 since minimum past rounds checked is 2.
            if round >= 3 :
                #If there is a successful prediction, the computer choice will be chosen to counter the predicted player item.
                predictedPlayerItem = (ML.ML_callHistoryMatching("computer"))
                if (predictedPlayerItem  != None) :
                    print("predicted move: ", predictedPlayerItem) #
                    if (predictedPlayerItem['player'] == 'Scissors') :
                        computerItem = RPS.Item.Rock
                    elif (predictedPlayerItem['player'] == 'Paper') :
                        computerItem = RPS.Item.Scissors
                    elif (predictedPlayerItem['player'] == 'Rock') :
                        computerItem = RPS.Item.Paper
            
            #If there are no successful predictions, the computer choice will default to random.
            if (computerItem == None) :
                computerItem = RPS.getComputerItem()

        #Prompts player input.
        playerInput = input("Enter your item: (rock, paper, scissors) ")

        #Allows the player to end the program with "quit" as the input.
        if(playerInput.lower() == "quit"):
            print("Thank you for playing!\n")
            break

        else:
            #Assigns an rps item corresponding to the user input.
            playerItem = RPS.inputToItem(playerInput)

            #If user input doesn't correspond to any rps item, prompts user input
            #and restarts the program.
            if (playerItem == None):
                print("Invalid Input\n")
                continue

            else:
                playerMove = RPS.getPlayerAsciiArt(playerItem)
                computerMove = RPS.getComputerAsciiArt(computerItem)
                if(not asciiVisibility):
                    print("You choose " + playerItem.name + ". Computer chooses " + computerItem.name + ".")
                else:
                    print("Player Move: " + playerItem.name + playerMove)
                    print("Computer Move: " + computerItem.name + computerMove)
                result = RPS.getOutcome(playerItem,computerItem)
                print("You " + result.name + ".\n")

                #Offering history matching
                # print(ML.ML_callHistoryMatching("player"))

                #Print rpsStorage
                ML.printRps()
        
        #Tracking the round
        round += 1


if __name__ == '__main__':
    main()