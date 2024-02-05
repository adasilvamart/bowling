from src.scorecard import ScoreCard
import pytest


@pytest.mark.parametrize(
    "pins, final_score",
    [
        ("xxxxxxxxxxxx", 300),
        ("8/549-XX5/53639/9/X", 149),
        ("9-3561368153258-7181", 82),
        ("9-9-9-9-9-9-9-9-9-9-", 90),
        ("X5/X5/XX5/--5/X5/", 175),
        ("9-9-9-9-9-9-9-9-9-XXX", 111),
        ("XXX9-9-9-9-9-9-9-", 141),
        ("5/5/5/5/5/5/5/5/5/5/5", 150),
        ("9-3/613/815/-/8-7/8/8", 131),
    ],
)
def test_calculate_scores(pins, final_score):
    assert ScoreCard(pins).get_score() == final_score
