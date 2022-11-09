# import RockPaperScissorsFullGame.RPS as RPS
import os
import sys
import pytest 

sys.path.append(os.path.abspath("./src/RockPaperScissorsFullGame"))
import RPS as RPS
import ML as ML

#---------------------------------------------------------------------------------
#--------------------------------Benji's ML Functions-----------------------------
#---------------------------------------------------------------------------------

#Parameters and return values for test_chooseDifficulty()
@pytest.mark.parametrize("player_input_difficulty, expected_difficulty", [
    ('easy', ML.difficulty.Easy),
    ('medium', ML.difficulty.Medium),
    ('hard', ML.difficulty.Hard),
    ('e', ML.difficulty.Easy),
    ('m', ML.difficulty.Medium),
    ('h', ML.difficulty.Hard),
    ('Easy', ML.difficulty.Easy),
    ('Medium', ML.difficulty.Medium),
    ('hArD', ML.difficulty.Hard),
    ('mEdIum', ML.difficulty.Medium),
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

@pytest.mark.parametrize("print_input, print_output", [
    ([{1 : {'player': 'Paper', 'computer': 'Rock'}}], 
    "\nOutcomes of the previous rounds: \n1  :  {'player': 'Paper', 'computer': 'Rock'}\n\n"),
    ([{1 : {'player': 'Paper', 'computer': 'Rock'}}, {2 : {'player': 'Scissors', 'computer': 'Paper'}}],
    "\nOutcomes of the previous rounds: \n1  :  {'player': 'Paper', 'computer': 'Rock'}\n2  :  {'player': 'Scissors', 'computer': 'Paper'}\n\n"),
    ([{1 : {'player': 'Paper', 'computer': 'Rock'}}, {2 : {'player': 'Scissors', 'computer': 'Paper'}}, {3 : {'player': 'Rock', 'computer': 'Scissors'}}],
    "\nOutcomes of the previous rounds: \n1  :  {'player': 'Paper', 'computer': 'Rock'}\n2  :  {'player': 'Scissors', 'computer': 'Paper'}\n3  :  {'player': 'Rock', 'computer': 'Scissors'}\n\n"),
    ([{1 : {'player': 'Paper', 'computer': 'Rock'}}, {2 : {'player': 'Scissors', 'computer': 'Paper'}}, {3 : {'player': 'Rock', 'computer': 'Scissors'}}, {4 : {'player': 'Paper', 'computer': 'Paper'}}],
    "\nOutcomes of the previous rounds: \n1  :  {'player': 'Paper', 'computer': 'Rock'}\n2  :  {'player': 'Scissors', 'computer': 'Paper'}\n3  :  {'player': 'Rock', 'computer': 'Scissors'}\n4  :  {'player': 'Paper', 'computer': 'Paper'}\n\n")
])

def test_printRps(capsys, print_input, print_output) :
    # if (len(ML.rpsStorage) != 0) :
    ML.rpsStorage = {}
    for kvp in print_input :
        ML.rpsStorage.update(kvp)
    ML.printRps()
    ML.rpsStorage = {}
    out, err = capsys.readouterr()
    assert out == print_output

# "\nOutcomes of the previous rounds: \n1  :  {'player': 'Paper', 'computer': 'Rock'}\n\n"
# "\nOutcomes of the previous rounds: \n1  :  {'player': 'Paper', 'computer': 'Rock'}\n\n"