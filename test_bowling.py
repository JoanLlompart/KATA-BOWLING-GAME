from venv import create
import pytest
import Bowling

class test_Bowling():
    def test_createbowling(self):
        game = Bowling.Bowling
    
    def testGutterGame(self):
        game = Bowling.Bowling
        for i in range(20):
            game.rolls(0)
        assert game.score() == 0
def testAllOnes(self):
    game = Bowling.Bowling()
    for i in range(20):
        game.roll(1)
    assert game.score(20) == 0