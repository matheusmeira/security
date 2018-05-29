from secrets import randbelow
from hashlib import md5
from hashlib import sha256
from random import choices
from collections import Counter

class BreakPassword:
    listOfProbability = []
    setOfPassword = set()

    def __init__(self, password, probability):
        self.dictionary = self.readFile()
        self.passwordToBeBroken = password
        self.listOfProbability = probability

    def passwordBroken(self):
        found = False
        while not found:
            passwordHash = self.getPassword()
            found = self.comparePassword(passwordHash)
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
        self.passwordFound = password
        return str(md5(password.encode('ascii')).hexdigest())

    def onCheckPasswordInSet(self, generatedPassword):
        return generatedPassword in self.setOfPassword

    def selectNumber(self):
        s = ''
        numberForWord = choices(range(1, 7), weights = self.listOfProbability, k = 5)
        s = s.join(map(str, numberForWord))
        return int(s)
            
    def readFile(self):
        dictionary = dict()
        with open('diceware.wordlist.asc') as f:
            for line in f:
                (key, value) = line.split()
                dictionary[int(key)] = value
        return dictionary


if __name__ == '__main__':
    password = 'ea05adc80b65cecb6ea3a3034602831c'
    defaultProbabilities = [0.2, 0.8, 0.0, 0.0, 0.0, 0.0]
    objBreakPassword = BreakPassword(password, defaultProbabilities)
    objBreakPassword.passwordBroken()