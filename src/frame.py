from dataclasses import dataclass


def group_elements(input_list, n):
    result = []
    for i in range(0, len(input_list), n):
        current_group = input_list[i : i + n]
        result.append(tuple(current_group))
    return result


class BaseToken:
    def __init__(self, data, ctx):
        self.data: str = data
        self.ctx: str = ctx

    def get_score(self):
        pass

    def is_correct(self):
        pass


class NumericToken(BaseToken):
    def is_correct(self):
        return self.data.isdecimal()

    def get_score(self):
        return int(self.data)


class StrikeToken(BaseToken):
    TOKEN = "x"

    def is_correct(self):
        return self.data.lower() == self.TOKEN

    def get_score(self):
        return 10


class NilToken(BaseToken):
    TOKEN = "-"

    def is_correct(self):
        return self.data.lower() == self.TOKEN

    def get_score(self):
        return 0


class SpareToken(BaseToken):
    TOKEN = "/"
    SPECIAL_TOKENS = (StrikeToken, NilToken)

    def __init__(self, data, ctx):
        super().__init__(data, ctx)
        self.ctx = self.ctx[::-1]

    def is_correct(self):
        return self.data.lower() == self.TOKEN

    def get_score(self):
        remaining = self.ctx[self.ctx.find(self.TOKEN) + 1  :] #ese +1 hay que tenrlo en cuenta solo si estamos jugando con darle la vuelta al string, si no queremos tener que darle la vuelta ponemos -1
        if not remaining.isdecimal():
            for special_token in self.SPECIAL_TOKENS:
                token = special_token(remaining, None)
                if token.is_correct():
                    remaining = token.get_score()
                    break
        return 10 - int(remaining)


class Frame:
    VALID_CHARS = "123456789x-/"
    TOKENS = (NumericToken, SpareToken, StrikeToken, NilToken)

    def __init__(self, pins=""):
        self.__pins = pins

    def __repr__(self):
        return str(self.pins)

    @property
    def pins(self):
        return self.__pins

    @pins.setter
    def pins(self, pins):
        self.__pins = pins

    def validate_pins(self):
        return all(char.lower() in Frame.VALID_CHARS for char in self.pins)

    def calc_score(self):
        total = 0
        for pin in self.pins:
            for token in self.TOKENS:
                pin_token = token(pin, self.pins)
                if pin_token.is_correct():
                    total += pin_token.get_score()
                    break
        return total


"""    def calc_special_character_puntuation(self):
        special_char = ["X", "-", "/"]
        special_char_values = {"X": lambda: 10, "-": lambda: 0, "/": lambda: self.calc_spare()}
        for item in special_char:
            self.pins.replace(item, str(special_char_values[item]()))
        return self.pins"""


class LastFrame(Frame):
    # Last frame has 3 tokens initially, but if you don't reach 10 points in the first 2 rolls, you lose the 3rd roll
    def has_three_rolls(self):
        return any(pin == "x" or pin == "/" for pin in self.pins[0:2])


if __name__ == "__main__":
    print(LastFrame("x1/").calc_score())
    print(LastFrame("1/x").calc_score())
