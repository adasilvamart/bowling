from src.game import Game


class ScoreCard:
    def __init__(self, pins) -> None:
        self.game = Game(pins)
        self.score = self.game.calculate_score()

    def __repr__(self):
        return self.format_scorecard()

    def get_score(self):
        return self.score[0]

    def format_scorecard(self):
        frames, totalPoints = self.get_frames_score()
        formatted_frame = "|"
        formatted_result = "|"
        middle_line = "|"
        total = f" Total Points: {totalPoints}"

        for frame, result in frames:

            if len(frame) == 3:
                formatted_frame += f" {frame[0]} | {frame[1]} | {frame[-1]} |"
                middle_line += "   --------|"
                formatted_result += f"    {result}    |"
            else:
                if frame == self.game.STRIKE:
                    formatted_frame += f" - | {frame[0]} |"

                formatted_frame += f" {frame[0]} | {frame[-1]} |"

                if len(str(result)) == 3:
                    formatted_result += f"  {result}  |"
                elif len(str(result)) == 1:
                    formatted_result += f"   {result}   |"
                else:
                    formatted_result += f"   {result}  |"

                middle_line += "   ----|"

        return str(f"{formatted_frame}\n{middle_line}{total}\n{formatted_result}")

    def get_frames_score(self):
        total_score, frame_score = self.game.calculate_score()
        frames = self.build_frames(self.game.get_pins())
        return list(zip(frames, frame_score)), total_score

    def padded_pins(self, pins) -> str:
        padded_pins = ""
        if not self.has_three_rolls():
            for i in range(0, len(pins)):
                if pins[i].lower() != "x":
                    padded_pins += pins[i]
                else:
                    padded_pins += "-" + pins[i]
            return padded_pins

        else:
            for i in range(0, len(pins[:-3])):
                if pins[i].lower() != "x":
                    padded_pins += pins[i]
                else:
                    padded_pins += "-" + pins[i]
            return padded_pins + pins[-3:]

    def build_frames(self, pins):
        padded_pins = self.padded_pins(pins)
        frames = []
        if self.has_three_rolls():
            for i in range(0, len(padded_pins[:-3]), 2):
                frames.append(padded_pins[i : i + 2])
            frames.append(padded_pins[-3:])
        else:
            for i in range(0, len(padded_pins), 2):
                frames.append(padded_pins[i : i + 2])
        return frames

    def has_three_rolls(self):
        pins = self.game.get_pins()
        if any(pin.lower() == "x" or pin == "/" for pin in pins[-3:]):
            return True
        return False
