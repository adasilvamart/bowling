from src.frame import Frame, LastFrame, group_elements
import re


class ScoreCard:
    def __init__(self, pins):
        self.score = 0
        self.pins = pins
        self.frames = self.generate_frames()

    def get_frame_pins(self):
        return [frame.pins for frame in self.get_frames()]

    def get_frames(self):
        return self.frames

    def padded_pins(self):
        # utiliza una regex para colocar un guión antes de una x exceptuando la ultima, ojo con el ultimo frame, que esto no se cumple
        pattern = re.compile(r"(?<!x)(x)(?!$)")
        return pattern.sub(r"-\1", self.pins)

    def generate_frames(self):
        padded_reversed_pins = self.padded_pins()
        last_frame_ending_index = len(padded_reversed_pins) - 2
        last_frame = LastFrame(padded_reversed_pins[last_frame_ending_index:])
        if last_frame.has_three_rolls():
            last_frame_ending_index = len(padded_reversed_pins) - 3
            last_frame = LastFrame(padded_reversed_pins[last_frame_ending_index:])
        return tuple(
            Frame(pins)
            for pins in group_elements(
                padded_reversed_pins[:last_frame_ending_index],
                2,  # agrupar de 2 en 2 desde el último frame, este no incluido
            )
        ) + tuple(group_elements(last_frame.pins, 3))
