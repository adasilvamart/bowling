class Game:
    VALID_CHARS = "123456789/x-"
    STRIKE = 'x'
    SPARE = '/'
    ZERO = '-'

    def __init__(self, pins):     
        self.pins = self.validatePins(pins)
        self.numPins = self.setNumPins()


    def __repr__(self):
        return f'{self.pins}'
    

    def getPins(self):
        return self.pins


    def getNumPins(self):
        return self.numPins


    def setNumPins(self):
        """
            Translate Pins into his numeric values
        """
        pins = self.getPins()
        numPins=[]

        for i, pin in enumerate(pins):

            if pin.isdigit(): # Pin
                numPins.append(int(pin))

            elif pin in self.SPARE: # Spare 
                if pins[i - 1] in self.ZERO:
                    numPins.append(10)
                else:    
                    numPins.append(10 - int(pins[i - 1]))

            elif pin in self.ZERO: # Nill
                numPins.append(0)

            else: # Strike
                numPins.append(10)

        return numPins   


    def validatePins(self, pins):
        if all(pin.lower() in self.VALID_CHARS for pin in pins):
            return pins
        raise ValueError
 

    def calcScore(self):
        score = 0
        frameScore = []

        numPins = self.getNumPins()
        frames = self.getPins()
        
        i = 0
        for frame in range(0, 10): 
            if self.isStrike(numPins, frames, i):
                frameScore.append(score + self.calcStrike(numPins, i))
                score += self.calcStrike(numPins, i)
                i += 1

            elif self.isSpare(numPins, frames, i):
                frameScore.append(score + self.calcSpare(numPins, i))
                score += self.calcSpare(numPins, i)
                
                i += 2

            else:
                frameScore.append(score + numPins[i] + numPins[i + 1])
                score += numPins[i] + numPins[i + 1]
                i += 2

        return score, frameScore
        

    def calcSpare(self, numPins, i):
        return 10 + numPins[i + 2]


    def calcStrike(self, numPins, i):
        return 10 + numPins[i + 1] + numPins[i + 2]


    def isSpare(self, numPins, frames, i):
        return numPins[i] + numPins[i + 1] == 10 and self.SPARE in frames[i + 1]


    def isStrike(self, numPins, frames, i):
        return frames[i].lower() == self.STRIKE and numPins[i] == 10
