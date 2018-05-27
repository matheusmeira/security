from secrets import randbelow
from hashlib import md5
from random import choices
from collections import Counter

class BreakPassword:
    listOfProbability = []
    setOfPassword = set()

    def __init__(self, password, probability):
        self.dictionary = self.readFile()
        self.passwordToBeBroken = password
        # self.generateListOfProbability(probability)
        self.listOfProbability = probability

    def passwordBroken(self):
        found = False
        while not found:
            passwordHash = self.getPassword()
            self.passwordFound = passwordHash
            found = self.comparePassword(passwordHash)
            # print(passwordHash)
            # print(found)
        print(self.passwordFound)

    def comparePassword(self, passwordGenerate):
        return passwordGenerate == self.passwordToBeBroken

    def getPassword(self):
        password = ''
        controll = True
        while controll:
            password = ''
            for i in range(6):
                numberSelected = self.selectNumber()
                word = self.dictionary[numberSelected]
                password = password + word
            controll = self.onCheckPasswordInSet(password)
            if not controll:
                self.setOfPassword.add(password)
        return str(md5(password.encode('ascii')).hexdigest())

    def onCheckPasswordInSet(self, generatedPassword):
        return generatedPassword in self.setOfPassword

    def selectNumber(self):
        s = ''
        numberForWord = choices(range(1, 7), weights = self.listOfProbability, k = 5)
        # while(len(numberForWord) < 5):
        #     numberRange = randbelow(100)
        #     for i in range(6):
        #         if numberRange < self.listOfProbability[i]:
        #             numberForWord.append(str(i + 1))
        #             break
        s = s.join(map(str, numberForWord))
        # print(int(s))
        return int(s)

    # def generateListOfProbability(self, listOfNumber):
    #     for prob in listOfNumber:
    #         if len(self.listOfProbability) == 0:
    #             self.listOfProbability.append(round(prob * 100))
    #         else:
    #             if prob != 0:
    #                 sum = self.listOfProbability[len(self.listOfProbability) - 1] + round(prob * 100)
    #                 self.listOfProbability.append(sum)
    #             else:
    #                 self.listOfProbability.append(0)
    #     print(self.listOfProbability)
            
    def readFile(self):
        dictionary = dict()
        with open('diceware.wordlist.asc') as f:
            for line in f:
                (key, value) = line.split()
                dictionary[int(key)] = value
                # print(key, value)
        return dictionary


if __name__ == '__main__':
    password = '2dcdb9fd95e7bf58056b47506dc3ebeb'
    defaultProbabilities = [0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.0, 0.0, 0.0]
    objBreakPassword = BreakPassword(password, defaultProbabilities)
    objBreakPassword.passwordBroken()