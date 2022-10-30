import RockPaperScissorsFullGame.RPS as RPS
import pytest

"""
For testing RPS.py
    def getComputerItem
    def getOutcome
"""

# test that RPS.getComputerItem will return an item that is either a rock, paper or scissor enum
def test_getComputerItem():
    computerItem = RPS.getComputerItem()
    rock = RPS.Item(1)
    paper = RPS.Item(2)
    scissors = RPS.Item(3)
    assert computerItem == rock or computerItem == paper or computerItem == scissors


@pytest.mark.parametrize("player_item, computer_item, outcome", [
    (RPS.Item.Rock, RPS.Item.Rock, RPS.Outcome.Tie),
    (RPS.Item.Rock, RPS.Item.Paper, RPS.Outcome.Lose),
    (RPS.Item.Rock, RPS.Item.Scissors, RPS.Outcome.Win),
    (RPS.Item.Paper, RPS.Item.Paper, RPS.Outcome.Tie),
    (RPS.Item.Paper, RPS.Item.Rock, RPS.Outcome.Win),
    (RPS.Item.Paper, RPS.Item.Scissors, RPS.Outcome.Lose),
    (RPS.Item.Scissors, RPS.Item.Rock, RPS.Outcome.Lose),
    (RPS.Item.Scissors, RPS.Item.Paper, RPS.Outcome.Win),
    (RPS.Item.Scissors, RPS.Item.Scissors, RPS.Outcome.Tie),
])

# test that 
    
def test_multipleOutcomes(player_item, computer_item, outcome):
    assert RPS.getOutcome(player_item, computer_item) is outcome
    