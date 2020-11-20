from configparser import ConfigParser
from os import path
from config import config_file_write as w


parser = ConfigParser()


RESET = None
EXIT = None
LOCATE_FORTRESS = None
LOCATE_STRONGHOLD = None
WINDOW_WIDTH = 0
WINDOW_HEIGHT = 0


def init():
    parseConfig()


def parseConfig():
    global RESET, EXIT, LOCATE_FORTRESS, LOCATE_STRONGHOLD
    if path.exists("config.ini"):
        parser.read('config.ini')
        # Program config
        configKey = parser.get('Program Hotkeys', 'reset coordinates')
        RESET = handleHotkey(configKey, w.DEFAULT_RESET)
        configKey = parser.get('Program Hotkeys', 'exit program')
        EXIT = handleHotkey(configKey, w.DEFAULT_EXIT)
        # Ingame commands config
        configKey = parser.get('Ingame Commands', 'locate fortress')
        LOCATE_FORTRESS = handleHotkey(configKey, w.DEFAULT_LOCATE_FORTRESS)
        configKey = parser.get('Ingame Commands', 'locate stronghold')
        LOCATE_STRONGHOLD = handleHotkey(configKey, w.DEFAULT_LOCATE_STRONGHOLD)
        # Window dimensions
        winWidth = parser.get('Window Dimensions', 'window width')
        winHeight = parser.get('Window Dimensions', 'window height')
        handleWindowDimensions(winWidth, winHeight)
    else:
        w.writeDefaultConfig()
        setDefaultHotkeys()


def handleHotkey(configKey, defaultKey):
    if len(configKey) == 1:
        hotkey = configKey
    else:
        hotkey = defaultKey
    return hotkey


def handleWindowDimensions(width, height):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    intW = int(width)
    if intW > 650 and intW <= 1920:
        WINDOW_WIDTH = intW
    else:
        WINDOW_WIDTH = w.DEFAULT_WINDOW_WIDTH
    intH = int(height)
    if intH > 250 and intH <= 1080:
        WINDOW_HEIGHT = intH
    else:
        WINDOW_HEIGHT = w.DEFAULT_WINDOW_HEIGHT


def setDefaultHotkeys():
    global RESET, EXIT, LOCATE_FORTRESS, LOCATE_STRONGHOLD, WINDOW_HEIGHT, WINDOW_WIDTH
    RESET = w.DEFAULT_RESET
    EXIT = w.DEFAULT_EXIT
    WINDOW_WIDTH = w.DEFAULT_WINDOW_WIDTH
    WINDOW_HEIGHT = w.DEFAULT_WINDOW_HEIGHT
    LOCATE_FORTRESS = w.DEFAULT_LOCATE_FORTRESS
    LOCATE_STRONGHOLD = w.DEFAULT_LOCATE_STRONGHOLD
