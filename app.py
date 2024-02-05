from src.scorecard import ScoreCard

if __name__ == "__main__":
    games = [
        "" "xxxxxxxxxxxx",
        "8/549-XX5/53639/9/X",
        "9-3561368153258-7181",
        "9-9-9-9-9-9-9-9-9-9-",
        "X5/X5/XX5/--5/X5/",
        "9-9-9-9-9-9-9-9-9-XXX",
        "XXX9-9-9-9-9-9-9-",
        "5/5/5/5/5/5/5/5/5/5/5",
        "9-3/613/815/-/8-7/8/8",
    ]

    for game in games:
        scorecard = ScoreCard(game)
        print(scorecard)
        print(f'\n{"-" * 110 }\n')
