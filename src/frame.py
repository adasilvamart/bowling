class BaseToken:
    def __init__(self, data):
        self.data = data  # iterable/list

    def get_score(self):
        pass

    def is_correct(self):
        pass

    def add_data(self, data):  # dato suelto
        if self.is_correct(self.data.copy().append(data)):
            self.data.append(data)
            return True
        return False


class NumericToken(BaseToken):
    pass


class SpareToken(BaseToken):
    pass


class StrikeToken(BaseToken):
    TOKEN = "x"

    def is_correct(self):
        return self.data.lower() == self.token


class LastFrameToken(BaseToken):
    pass


class Frame:
    ALLOWED_CHARACTERS = "123456789x-/"

    def __init__(self):
        pass

    def get_overall_score(self):
        pass  # use here classes that inherit from BaseToken

    @classmethod
    def validate(cls, card):
        return all(char in cls.ALLOWED_CHARACTERS for char in card.lower())
