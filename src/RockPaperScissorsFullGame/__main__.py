#import RockPaperScissorsFullGame.RPS as RPS
import RPS

def inputToItem(str):
    if ("rock").startswith(str.lower()):
        return RPS.Item.Rock
    elif ("paper").startswith(str.lower()):
        return RPS.Item.Paper
    elif ("scissors").startswith(str.lower()):
        return RPS.Item.Scissors
    else:
        return None


def main():
    play = True
    while (play):
        computerItem = RPS.getComputerItem()
        playerInput = input("Enter your item: (rock, paper, scissors)\n")
        if(playerInput.lower() == "quit"):
            print("Thank you for playing!\n")
            break
        else:
            playerItem = inputToItem(playerInput)
            if(playerItem == None):
                print("Invalid Input\n")
                continue
            else:
                print("You choose " + playerItem.name + ". Computer chooses " + computerItem.name + ".")
                result = RPS.getOutcome(playerItem,computerItem)
                print("You " + result.name + ".\n")



if __name__ == '__main__':
    main()