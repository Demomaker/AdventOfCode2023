numberMap = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def getNextNumber(line):
    numberWord = ""
    numberWords = numberMap.keys()
    for character in line:
        if str(character).isnumeric():
            return character
        else:
            numberWord = numberWord + character
            for possibleNumberWord in numberWords:
                if possibleNumberWord in numberWord:
                    return possibleNumberWord
    return ""

def getElfCalibrations(array):
    elfCalibrations = []
    for line in array:
        lineNumbers = []
        currentAmount = 0
        subline = line
        nextNumber = getNextNumber(subline)
        while nextNumber != "":
            if nextNumber.isnumeric():
                lineNumbers.append(nextNumber)
            else:
                lineNumbers.append(numberMap[nextNumber])
            sublineIndex = subline.find(nextNumber) + 1
            subline = subline[sublineIndex:]
            nextNumber = getNextNumber(subline)
        if len(lineNumbers) > 0:
            if len(lineNumbers) > 1:
                currentAmount = int(str(lineNumbers[0]) + str(lineNumbers[-1]))
            else :
                currentAmount = int(str(lineNumbers[0]) + str(lineNumbers[0]))
        elfCalibrations.append(currentAmount)
    print(elfCalibrations)
    return elfCalibrations

def getTotalCalibration():
    elfCalibrations = getElfCalibrations(getCalibrationArray())
    elfCalibrations.sort(reverse=True)
    return sum(elfCalibrations)

def getCalibrationArray():
    file = open("input.txt", "r")
    array = []
    for index, line in enumerate(file):
        array.append(line[:-1])
    file.close()
    return array

print(getTotalCalibration())
