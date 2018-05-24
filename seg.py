from secrets import randbelow
def generateNumber(listOfNumber):
    listOfProbability = []
    for prob in listOfNumber:
        if len(listOfProbability) == 0:
            listOfProbability.append(round(prob * 100))
        else:
            if prob != 0:
                sum = listOfProbability[len(listOfProbability) - 1] + round(prob * 100)
                listOfProbability.append(sum)
            else:
                listOfProbability.append(0)
    selectNumber(listOfProbability)

def selectNumber(listOfNumber):
    numberForWord = []
    while(len(numberForWord) < 6):
        numberRange = randbelow(100)
        for i in range(6):
            if numberRange < listOfNumber[i]:
                numberForWord.append(i + 1)
                break
    print(numberForWord)
        

if __name__ == '__main__':
    generateNumber([0.027777777777777776, 0.027777777777777776, 0.5833333333333334,
    0.027777777777777776, 0.3055555555555556, 0.027777777777777776])