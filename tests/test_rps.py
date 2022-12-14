# import RockPaperScissorsFullGame.RPS as RPS
import os
import sys
import pytest 

sys.path.append(os.path.abspath("./src/RockPaperScissorsFullGame"))
import RPS as RPS
import ML as ML

"""
For testing RPS.py
    def getComputerItem
    def getOutcome
    def inputToItem
    def getPlayerAsciiArt
    def getComputerAsciiArt
    def setAsciiVisibility
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

# test def getPlayerAsciiArt with multiple parameters 
@pytest.mark.parametrize("item, player_art", [
    (RPS.Item.Rock, """
            _____
        ---'  ____)  
             (_____)  
             (_____)  
             (____)
        ---.(___)
        """),

    (RPS.Item.Paper, """
            ______
        ---'   ____)____  
                   ______)  
                   _______)  
                  _______)
        ---._________) 
        """),

    (RPS.Item.Scissors, """
            ______
        ---'   ____)_____ 
                    ______)  
                __________)  
              (____)
        ---.__(___)
        """),

    (None, "Invalid Option"),
    (RPS.Outcome.Tie, "Invalid Option")
])

# test that RPS.getPlayerAsciiArt will return an art that is either a rock, paper or scissor if given the correct item
def test_getPlayerAsciiArt(item,player_art):
    assert RPS.getPlayerAsciiArt(item) == player_art

# test def getComputerAsciiArt with multiple parameters 
@pytest.mark.parametrize("item, computer_art", [
    (RPS.Item.Rock, """
           _____
         (____  '---
        (_____)  
        (_____)  
         (____)
           (___).---

        """),

    (RPS.Item.Paper, """
             _____
       ____(____  '---
     (_____ 
    (_______  
     (_______
       (_________.---
        """),

    (RPS.Item.Scissors, """
                _____
         ______(____ '--- 
       (______  
       (__________  
            (____)
             (___)__.---
        """),

    (None, "Invalid Option"),
    (RPS.Outcome.Tie, "Invalid Option")
])

# test that RPS.getComputerAsciiArt will return an art that is either a rock, paper or scissor if given the correct item
def test_getComputerAsciiArt(item,computer_art):
    assert RPS.getComputerAsciiArt(item) == computer_art


# test def inputToItem with multiple parameters 
@pytest.mark.parametrize("player_set_input, expected", [
    ('Yes', True),
    ('No', False),
    ('no', False),
    ('yes', True),
    ('1', True),
    ('2', False),
    ('3', True),
    ('0', True),
    ('kjndsfa', True),
    ("sdjfn;l", True),
    ('y', True),
    ('n', True)
])

def test_setAsciiVisibility(monkeypatch,player_set_input, expected):
    monkeypatch.setattr('builtins.input', lambda _: player_set_input)
    assert RPS.setAsciiVisibility() is expected

#---------------------------------------------------------------------------------
#--------------------------------Benji's Functions--------------------------------
#---------------------------------------------------------------------------------

#Parameters and return values for test_chooseDifficulty()
@pytest.mark.parametrize("player_input_difficulty, expected_difficulty", [
    ('easy', ML.difficulty.Easy),
    ('hard', ML.difficulty.Hard),
    ('e', ML.difficulty.Easy),
    ('h', ML.difficulty.Hard),
    ('Easy', ML.difficulty.Easy),
    ('hArD', ML.difficulty.Hard),
    ('NONE', None),
    ('adasdasdas', None)
])

#Testing ML.chooseDifficulty() to return a correct difficulty.
def test_chooseDifficulty(monkeypatch, player_input_difficulty, expected_difficulty) :
    monkeypatch.setattr('builtins.input', lambda _: player_input_difficulty)
    assert ML.chooseDifficulty() is expected_difficulty

@pytest.mark.parametrize("store_outcome, store_player, store_computer, store_kvp", [
    ('Win', 'Paper', 'Rock', {1 : {'player': 'Paper', 'computer': 'Rock'}}),
    ('Win', 'Scissors', 'Paper', {1 : {'player': 'Scissors', 'computer': 'Paper'}}),
    ('Win', 'Rock', 'Scissors', {1 : {'player': 'Rock', 'computer': 'Scissors'}}),
    ('Tie', 'Paper', 'Paper', {1 : {'player': 'Paper', 'computer': 'Paper'}}),
    ('Tie', 'Scissors', 'Scissors', {1 : {'player': 'Scissors', 'computer': 'Scissors'}}),
    ('Tie', 'Rock', 'Rock', {1 : {'player': 'Rock', 'computer': 'Rock'}}),
    ('Lose', 'Paper', 'Scissors', {1 : {'player': 'Paper', 'computer': 'Scissors'}}),
    ('Lose', 'Scissors', 'Rock', {1 : {'player': 'Scissors', 'computer': 'Rock'}}),
    ('Lose', 'Rock', 'Paper', {1 : {'player': 'Rock', 'computer': 'Paper'}}),
    ('asdasda', None, None, None)
])

#Testing ML.storeOutcome() to store accurate outcomes in the rpsStorage dictionary.
def test_storeOutcome(store_outcome, store_player, store_computer, store_kvp) :
    ML.round = 1
    assert ML.storeOutcome(store_outcome, store_player, store_computer) == store_kvp

# @pytest.mark.parametrize("print_input", [
#     ({1 : {'player': 'Paper', 'computer': 'Rock'}}),
#     ({1 : {'player': 'Paper', 'computer': 'Rock'}}, {2 : {'player': 'Scissors', 'computer': 'Paper'}}),
#     ({1 : {'player': 'Paper', 'computer': 'Rock'}}, {2 : {'player': 'Scissors', 'computer': 'Paper'}}, {3 : {'player': 'Rock', 'computer': 'Scissors'}}),
#     ({1 : {'player': 'Paper', 'computer': 'Rock'}}, {2 : {'player': 'Scissors', 'computer': 'Paper'}}, {3 : {'player': 'Rock', 'computer': 'Scissors'}}, {4 : {'player': 'Paper', 'computer': 'Paper'}})
# ])

# def test_printRps(capsys, print_input) :
#     ML.rpsStorage.update(print_input)
#     ML.printRps()
#     out, err = capsys.readouterr()
#     ML.rpsStorage.clear()
#     assert out is print_input
