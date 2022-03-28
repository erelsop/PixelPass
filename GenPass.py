import numpy as np
import string
import Collection


# Initialize variables to hold password data
passAverages = ''
chunks = ''
passValues = ''
modValues = ''
gendPass = ''
desiredLength = ''


def getAverages(imageData):
    """Returns an array containing the average of RGB values within
    a separate array that holds image data"""

    averages = [sum(i) / len(i) for i in imageData]
    return averages


def getMaxPass(averages):
    """Calculates the maximum password length possible, according
    to the width of the image"""

    maxLength = len(averages)
    return maxLength


def defineChunks(averages, maxPassSize, passLength):
    """Separates RGB averages into separate arrays according to
    password length, then returns those arrays within an array"""

    return [averages[i * maxPassSize // passLength: (i + 1) * maxPassSize // passLength] for i in range(passLength)]




def genPass(maxLength, desLength, specialChars):

    global passAverages
    global chunks
    global passValues
    global gendPass
    global modValues
    global desiredLength

    
    try:
        desiredLength = int(desiredLength)
    except ValueError:
        return False

    if type(Collection.passCenterRow) == np.ndarray:
            if desiredLength <= Collection.passMaxLength:
                # Generate and update outputted password
                passAverages = getAverages(Collection.passCenterRow)
                passMaxLength = getMaxPass(passAverages)
                chunks = defineChunks(passAverages, passMaxLength, desiredLength)
                passValues = getAverages(chunks)
                modValues = [int(hash(i)) for i in passValues]
                if specialChars == 1:
                    modValues = [i % 95 for i in modValues]
                    gendPass = [string.printable[i] for i in modValues]
                    gendPass = ''.join(gendPass)
                    return gendPass
                else:
                    modValues = [i % 62 for i in modValues]
                    gendPass = [string.printable[i] for i in modValues]
                    gendPass = ''.join(gendPass)
                    return gendPass
            else:
                return "Password length exceeds the max available"