# import RockPaperScissorsFullGame.RPS as RPS
import RPS
import ML

def main():
    #first ask user if they want to see ascii art
    asciiVisibility = RPS.setAsciiVisibility()
    
    # game
    play = True
    while (play):
        #Randomizes and returns an rps item for the computer choice.
        computerItem = RPS.getComputerItem()

        #Prompts player input.
        playerInput = input("Enter your item: (rock, paper, scissors)\n")

        #Allows the player to end the program with "quit" as the input.
        if(playerInput.lower() == "quit"):
            print("Thank you for playing!\n")
            break

        else:
            #Assigns an rps item corresponding to the user input.
            playerItem = RPS.inputToItem(playerInput)

            #If user input doesn't correspond to any rps item, prompts user input
            #and restarts the program.
            if(playerItem == None):
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

                #Print rpsStorage
                ML.printRps()


if __name__ == '__main__':
    main()