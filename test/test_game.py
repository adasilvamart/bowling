from src.scorecard import ScoreCard


def test_NumericPins():
    game = ScoreCard('12345123451234512345')
    total = 60
    assert game.score, total


def test_spareInGame():
    game = ScoreCard('9-3/613/815/-/8-7/8/8')
    total = 131
    assert game.score, total


def test_concatenateSpares():
    game = ScoreCard('5/5/5/5/5/5/5/5/5/5/5')
    total = 150
    assert game.score, total


def test_perfectGame():
    game = ScoreCard('xxxxxxxxxxxx')
    total = 300
    assert game.score, total


def test_tripleStrike():
    game = ScoreCard('XXX9-9-9-9-9-9-9-')
    total = 141
    assert game.score, total


def test_spareInLastRoll():
    game = ScoreCard('8/549-XX5/53639/9/X')
    total = 149
    assert game.score, total
