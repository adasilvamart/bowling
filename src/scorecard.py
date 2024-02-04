from src.game import Game

class ScoreCard():
    def __init__(self, pins) -> None:
        self.game = Game(pins)
        self.score = self.game.calcScore()
  

    def __repr__(self):
        return self.formatScorecard()


    def getScore(self):
        return self.score[0]
    

    def formatScorecard(self):
        frames, totalPoints = self.getFramesScore()
        formatted_frame = "|"
        formatted_result = "|"
        middle_line = "|"
        total = f" Total Points: {totalPoints}"

        for frame, result in frames:
            
            if len(frame) == 3:
                formatted_frame += f' {frame[0]} | {frame[1]} | {frame[-1]} |'
                middle_line += "   --------|"
                formatted_result += f'    {result}    |'
            else:
                if frame == self.game.STRIKE:
                    formatted_frame += f' - | {frame[0]} |'    

                formatted_frame += f' {frame[0]} | {frame[-1]} |'

                if len(str(result)) == 3:
                    formatted_result += f'  {result}  |'
                elif len(str(result)) == 1:
                    formatted_result += f'   {result}   |'
                else:
                    formatted_result += f'   {result}  |'
            
                middle_line += "   ----|"      
        
        return str(f'{formatted_frame}\n{middle_line}{total}\n{formatted_result}')


    def getFramesScore(self):

        totalScore, frameScore = self.game.calcScore()        
        frames = self.buildFrames(self.game.getPins())
        
        return list(zip(frames, frameScore)), totalScore


    def padded_pins(self, pins) -> str:
        padded_pins = ''
        if not self.hasThreeRolls():
            for i in range(0, len(pins)):
                if pins[i].lower() != 'x':
                    padded_pins += pins[i]
                else:
                    padded_pins += '-' + pins[i]
            return padded_pins
        
        else:
            for i in range(0, len(pins[:-3])):
                if pins[i].lower() != 'x':
                    padded_pins += pins[i]
                else:
                    padded_pins += '-' + pins[i]
            return padded_pins + pins[-3:]

    
    def buildFrames(self, pins):
        padded_pins = self.padded_pins(pins)
        frames = []
        if self.hasThreeRolls():
            for i in range(0, len(padded_pins[:-3]), 2):
                frames.append(padded_pins[i:i+2])
            frames.append(padded_pins[-3:])
        else:
            for i in range(0, len(padded_pins), 2):
                frames.append(padded_pins[i:i+2])
        return frames

            
    def hasThreeRolls(self):
        pins = self.game.getPins()
        frames = []

        for i in range(0, len(pins), 2):
            frames.append((pins)[i : i + 2])

        if any(len(pin) < 2 for pin in frames) or any(pin == "x" or pin == "/" for pin in pins[-3:]):
            return True
        return False