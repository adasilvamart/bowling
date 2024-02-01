if __name__ == "__main__":
    from src.score_card import ScoreCard
    pins = "81-92/x637-52x-62/x"
    scoreCard = ScoreCard(pins)
    print(scoreCard.generate_frames())
    # total3 = 122

    pins2 = "1-x1232x123-x"
    scoreCard2 = ScoreCard(pins2)
    print(scoreCard2.generate_frames())
    # print(scoreCard2.get_frame_pins())

    pins3 = "12345123451234512345"
    scoreCard3 = ScoreCard(pins3)

    # print(scoreCard3.get_frame_pins())
    print(scoreCard3.generate_frames())
