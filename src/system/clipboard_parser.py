import pyperclip
from system import window_management as wm
from minecraftmath import calculator
from minecraftmath import coordinate_finder

netherSet = False
firstThrowSet = False
secondThrowSet = False


def clear():
    global netherSet, firstThrowSet, secondThrowSet
    netherSet = False
    firstThrowSet = False
    secondThrowSet = False


def handleClipboard(clipboard):
    global netherSet, firstThrowSet, secondThrowSet
    if isMinecraftClipboard(clipboard):
        pyperclip.copy("")
        parseClipboard(clipboard)


def parseClipboard(clipboard):
    f3 = clipboard[42:].split()
    x = float(f3[0])
    y = float(f3[1])
    z = float(f3[2])
    angle = float(f3[3]) % 360
    if inNether(clipboard):
        if netherSet == False:
            wm.addNether(*calculator.roundNetherCoordinates(x, y ,z))
            netherSet = True
    else:
        if firstThrowSet == True:
            wm.addSuggestion(*coordinate_finder.findStronghold(x, z, angle))
            secondThrowSet = True
        else:
            wm.addStronghold(*coordinate_finder.findSecondSuggestedThrow(x, y, angle))
            firstThrowSet = True


def isMinecraftClipboard(clipboard):
    identifier = clipboard[1:21]
    if identifier == "execute in minecraft":
        return True
    else:
        return False


def inNether(clipboard):
    identifier = clipboard[22:32]
    if identifier == "the_nether":
        return True
    else:
        return False
