from src.frame import Frame, LastFrame
import re


def group_elements(input_list, n):
    result = []
    for i in range(0, len(input_list), n):
        if i + 1 < len(input_list):
            result.append((input_list[i], input_list[i + 1]))
        else:
            result.append((input_list[i],))
    return result


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
        padded_reversed_pins = self.padded_pins()[::-1]
        last_frame_ending_index = 1
        last_frame = LastFrame(padded_reversed_pins[:last_frame_ending_index])
        if last_frame.has_three_rolls():
            last_frame_ending_index = 2
            last_frame = LastFrame(padded_reversed_pins[:last_frame_ending_index])
        return (
            last_frame,
        ) + tuple(  # TODO: por algun motivo, last frame no es una tupla como el resto
            Frame(pins)
            for pins in group_elements(
                padded_reversed_pins[last_frame_ending_index:], 2
            )
        )  # agrupar de 2 en 2 desde el último frame, este no incluido
