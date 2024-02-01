from dataclasses import dataclass


class BaseToken:
    def __init__(self, data):
        self.data: str = data

    def get_score(self):
        pass

    def is_correct(self):
        pass

    def add_data(self, data):  # dato suelto
        appended_data = self.data + data
        if self.is_correct(appended_data):
            self.data = appended_data
            return True
        return False


class NumericToken(BaseToken):
    def get_score(self):
        return int(self.data)

    def is_correct(self):
        return self.data.isdecimal()


class SpareToken(BaseToken):
    TOKEN = "/"

    def is_correct(self):
        return self.data.lower() == self.TOKEN


class StrikeToken(BaseToken):
    TOKEN = "x"

    def is_correct(self):
        return self.data.lower() == self.TOKEN


class Frame:
    @dataclass
    class InternalFrameState:
        pass

    VALID_CHARS = "123456789x-/"

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


    def calc_spare (self):
        spare_index = self.pins.find('/')
        spare_value = 10 - int(self.pins[spare_index + 1]) 
        return spare_value 

    def calc_special_character_puntuation(self):
        #sustituir los caracteres especiales por su valor, directamente pues ya hemos separado de 2 en 2
        special_char = {"x": lambda: 10, "-": lambda: 0, "/": lambda: self.calc_spare()}

        pass

    def calc_score(self):
        pass


class LastFrame(Frame):
    # Last frame has 3 tokens initially, but if you don't reach 10 points in the first 2 rolls, you lose the 3rd roll
    def has_three_rolls(self):
        return any(pin == "x" or pin == "/" for pin in self.pins[0:2])


if __name__ == "__main__":
    print(LastFrame("12").has_three_rolls())
    frame = Frame('/1')
    print(frame.calc_spare())

