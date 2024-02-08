class Game:
    VALID_CHARS = "123456789/x-"
    STRIKE = "x"
    SPARE = "/"
    ZERO = "-"

    def __init__(self, pins):
        self.pins = self.is_pin_valid(pins)
        self.num_pins = self.calc_pin_values()
        self.score = self.calculate_score()[0]

    def get_score(self):
        return self.score

    def __repr__(self):
        return f"{self.pins}"

    def get_pins(self):
        return self.pins

    def get_num_pins(self):
        return self.num_pins

    def calc_pin_values(self):
        """
        Translate Pins into their numeric values
        """
        pins = self.get_pins()
        num_pins = []

        for i, pin in enumerate(pins):

            if pin.isdigit():  # Pin
                num_pins.append(int(pin))

            elif pin in self.SPARE:  # Spare
                if pins[i - 1] in self.ZERO:
                    num_pins.append(10)
                else:
                    num_pins.append(10 - int(pins[i - 1]))

            elif pin in self.ZERO:  # Null
                num_pins.append(0)

            else:  # Strike
                num_pins.append(10)

        return num_pins

    def is_pin_valid(self, pins):
        if all(pin.lower() in self.VALID_CHARS for pin in pins):
            return pins
        return None

    def calculate_score(self):
        score = 0
        frame_score = []

        num_pins = self.get_num_pins()
        frames = self.get_pins()

        i = 0
        for frame in range(0, 10):
            if self.is_strike(num_pins, frames, i):
                frame_score.append(score + self.calculate_strike(num_pins, i))
                score += self.calculate_strike(num_pins, i)
                i += 1

            elif self.is_spare(num_pins, frames, i):
                frame_score.append(score + self.calculate_spare(num_pins, i))
                score += self.calculate_spare(num_pins, i)

                i += 2

            else:
                frame_score.append(score + num_pins[i] + num_pins[i + 1])
                score += num_pins[i] + num_pins[i + 1]
                i += 2

        return score, frame_score

    def calculate_spare(self, num_pins, i):
        return 10 + num_pins[i + 2]

    def calculate_strike(self, num_pins, i):
        return 10 + num_pins[i + 1] + num_pins[i + 2]

    def is_spare(self, num_pins, frames, i):
        return num_pins[i] + num_pins[i + 1] == 10 and self.SPARE in frames[i + 1]

    def is_strike(self, num_pins, frames, i):
        return frames[i].lower() == self.STRIKE and num_pins[i] == 10
