from PIL import Image as Img
import platform
import numpy as np
from tkinter import filedialog
import GenPass


# Initialize variables to hold password image path and data
passImgPath = None
passImgData = None
passImgContext = None
passCenterRow = None
passMaxLength = None


def getContext():
    """Opens file dialog for master and password key image selection, opens the image,
    and then returns the RGB data in a new numpy array"""

    global passImgPath
    global passImgData
    global passImgContext
    global passCenterRow
    global passMaxLength

    # Determines system platform to decide image selection's starting directory
    plt = platform.system()
    if plt == "Windows":
        strdir = "C:/Users"
    elif plt == "Linux":
        strdir = "~/"
    elif plt == "Darwin":
        strdir = "~/"
    else:
        strdir = "/"

    imagePath = filedialog.askopenfilename(initialdir=strdir, title="Select image", filetypes=(
        ("png files", "*.png *.PNG"), ("bmp files", "*.bmp *.BMP"), ("all files", "*")))

    passImgPath = imagePath

    try:
        passImgData = getImageData(passImgPath)
    except AttributeError:
        return False

    if verifyComplexity(passImgData):
        passCenterRow = len(passImgData) // 2
        passCenterRow = passImgData[passCenterRow]
        passMaxLength = len(passCenterRow)
        return passImgPath
    else:
        passImgPath = "Image did not meet complexity requirements"
        return passImgPath


def getImageData(imagePath):
    image = Img.open(imagePath)
    return np.array(image)


def verifyComplexity(data):
    """Determines whether an image is visually complex enough for secure password
    generation. If the image deminsions are too small, or the image does not contain
    sufficient color complexity, the user must select a new image"""
    weakCount = 0
    if len(data) > 128:
        for pixelRow in range(len(data)):
            currentRow = data[pixelRow]
            comparison = currentRow == data[0]
            same = comparison.all()
            if same:
                weakCount += 1
        if weakCount > 48:
            return False
        else:
            return True
    else:
        return False