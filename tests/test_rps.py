# import RockPaperScissorsFullGame.RPS as RPS
import os
import sys
import pytest
sys.path.append(os.path.abspath("./src/RockPaperScissorsFullGame"))
import RPS as RPS

"""
For testing RPS.py
    def getComputerItem
    def getOutcome
    def inputToItem
"""

# test that RPS.getComputerItem will return an item that is either a rock, paper or scissor enum
def test_getComputerItem():
    computerItem = RPS.getComputerItem()
    rock = RPS.Item(1)
    paper = RPS.Item(2)
    scissors = RPS.Item(3)
    assert computerItem == rock or computerItem == paper or computerItem == scissors

# test multiple outcomes
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

def test_multipleOutcomes(player_item, computer_item, outcome):
    assert RPS.getOutcome(player_item, computer_item) is outcome
    
# test def inputToItem with multiple parameters 
@pytest.mark.parametrize("player_input, expected", [
    ('r', RPS.Item.Rock),
    ('R', RPS.Item.Rock),
    ('ROCK', RPS.Item.Rock),
    ('rOcK',RPS.Item.Rock),
    ('rock', RPS.Item.Rock),
    ('rat',  None),
    ('racket', None),
    ('p', RPS.Item.Paper),
    ('P', RPS.Item.Paper),
    ('PAPER', RPS.Item.Paper),
    ('pApER', RPS.Item.Paper),
    ('paper', RPS.Item.Paper),
    ('pistol', None),
    ('panther', None),
    ('s', RPS.Item.Scissors),
    ('S', RPS.Item.Scissors),
    ('scissor', RPS.Item.Scissors),
    ('scissors', RPS.Item.Scissors),
    ('SCISSORS', RPS.Item.Scissors),
    ('sciSSORS', RPS.Item.Scissors),
    ('scorch', None),
    ('scanner', None),
    ('scjdkods', None),
    ('pdsadsd', None),
    ('rodsjdsod', None),
    ('dunce', None),
    ('lagoon', None),
    ('monastery', None),
    ('937932', None),
    ('1.3932', None),
    ('#93jf', None),
    ('flavorful-93932-#', None)
])

def test_inputToItem(player_input, expected):
    assert RPS.inputToItem(player_input) is expected