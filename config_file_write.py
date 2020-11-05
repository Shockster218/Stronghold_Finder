from configparser import ConfigParser
from os import path
import config_file_read


config = ConfigParser()


DEFAULT_RESET = "g"
DEFAULT_EXIT = ';'
DEFAULT_LOCATE_FORTRESS = ","
DEFAULT_LOCATE_STRONGHOLD = "."

def WriteDefaultConfig():
    global config
    config['Program Hotkeys'] ={
        'reset coordinates' : DEFAULT_RESET,
        'exit program' : DEFAULT_EXIT
    }

    config['Ingame Commands'] ={
        'locate fortress': DEFAULT_LOCATE_FORTRESS,
        'locate stronghold': DEFAULT_LOCATE_STRONGHOLD
    }


def SaveConfig():
    global config
    config.read('config.ini')
    config.set('Program Hotkeys', 'reset coordinates', config_file_read.RESET)
    config.set('Program Hotkeys', 'exit program', config_file_read.EXIT)
    config.set('Ingame Commands', 'locate fortress', config_file_read.LOCATE_FORTRESS)
    config.set('Ingame Commands', 'locate stronghold', config_file_read.LOCATE_STRONGHOLD)

    with open('config.ini', 'w') as f:
        config.write(f)
