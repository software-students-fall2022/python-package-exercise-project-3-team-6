import RockPaperScissorsFullGame.__main__ as main
import RockPaperScissorsFullGame.RPS as RPS
import pytest

# For testing 'def inputToItem' in __main__.py

#Rather than testing if the input contains the correct first letter, check if the input is a substring of rock, paper, or scissor
@pytest.mark.parametrize("player_input, expected", [
    ('r', RPS.Item.Rock),
    ('R', RPS.Item.Rock),
    ('ROCK', RPS.Item.Rock),
    ('rOcK',RPS.Item.Rock),
    ('rock', RPS.Item.Rock),
    ('rat', None),
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