#import RockPaperScissorsFullGame.RPS as RPS
import RPS
import ML

def main():
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
                #Printing out player choice and computer choice.
                print("You choose " + playerItem.name + ". Computer chooses " + computerItem.name + ".")
                
                #Gets the outcome of the round and prints it.
                result = RPS.getOutcome(playerItem,computerItem)
                print("You " + result.name + ".\n")

if __name__ == '__main__':
    main()