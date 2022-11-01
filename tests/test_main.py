import os
import sys

sys.path.append(os.path.abspath("./src/RockPaperScissorsFullGame"))
import __main__ as main #does not work
# import __main__ also does not work
# from __main__ import * also does not work
import RPS as RPS
import pytest
# For testing 'def inputToItem' in __main__.py

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
    assert main.inputToItem(player_input) is expected