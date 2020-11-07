from configparser import ConfigParser
from os import path
import config_file_read as r
import config_helper as helper


config = ConfigParser()


DEFAULT_RESET = "g"
DEFAULT_EXIT = ';'
DEFAULT_LOCATE_FORTRESS = ","
DEFAULT_LOCATE_STRONGHOLD = "."
DEFAULT_WINDOW_WIDTH = 600
DEFAULT_WINDOW_HEIGHT = 250


def writeDefaultConfig():
    global config
    config['Program Hotkeys'] = {
        'reset coordinates': DEFAULT_RESET,
        'exit program': DEFAULT_EXIT,
    }

    config['Ingame Commands'] = {
        'locate fortress': DEFAULT_LOCATE_FORTRESS,
        'locate stronghold': DEFAULT_LOCATE_STRONGHOLD
    }

    config['Window Dimensions'] = {
        'window width': DEFAULT_WINDOW_WIDTH,
        'window height': DEFAULT_WINDOW_HEIGHT
    }


def SaveConfig(screen):
    global config
    config.read('config.ini')
    config.set('Program Hotkeys', 'reset coordinates', r.RESET)
    config.set('Program Hotkeys', 'exit program', r.EXIT)
    config.set('Ingame Commands', 'locate fortress', r.LOCATE_FORTRESS)
    config.set('Ingame Commands', 'locate stronghold', r.LOCATE_STRONGHOLD)
    config.set('Window Dimensions', 'window width', helper.getWindowWidth())
    config.set('Window Dimensions', 'window height', helper.getWindowHeight())

    with open('config.ini', 'w') as f:
        config.write(f)
