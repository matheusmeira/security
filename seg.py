from secrets import randbelow
from hashlib import md5

class BreakPassword:
    passwordFound = 0
    listOfProbability = []
    numberSelected = 0

    def __init__(self):
        self.dictionary = self.readFile()

    def getPassword(self):
        password = ''
        while self.passwordFound < 6:
            self.numberSelected = self.selectNumber(self.listOfProbability)
            word = self.dictionary[self.numberSelected]
            password = password + word
            self.passwordFound += 1
        print(md5(password.encode('utf-8')).hexdigest())

    def generateListOfProbability(self, listOfNumber):
        for prob in listOfNumber:
            if len(self.listOfProbability) == 0:
                self.listOfProbability.append(round(prob * 100))
            else:
                if prob != 0:
                    sum = self.listOfProbability[len(self.listOfProbability) - 1] + round(prob * 100)
                    self.listOfProbability.append(sum)
                else:
                    self.listOfProbability.append(0)

    def selectNumber(self, listOfNumber):
        s = ''
        numberForWord = []
        while(len(numberForWord) < 5):
            numberRange = randbelow(100)
            for i in range(6):
                if numberRange < listOfNumber[i]:
                    numberForWord.append(str(i + 1))
                    break
        s = s.join(numberForWord)
        print(int(s))
        return int(s)
            
    def readFile(self):
        dictionary = dict()
        with open('diceware.wordlist.asc') as f:
            for line in f:
                (key, value) = line.split()
                dictionary[int(key)] = value
        return dictionary


if __name__ == '__main__':
    defaultProbabilities = [0.027777777777777776, 0.027777777777777776, 0.5833333333333334,
    0.027777777777777776, 0.3055555555555556, 0.027777777777777776]
    objBreakPassword = BreakPassword()
    objBreakPassword.generateListOfProbability(defaultProbabilities)
    objBreakPassword.getPassword()