import configparser

def readProperitesFile():
    config = configparser.ConfigParser()
    config.read('/Users/venu/Desktop/Workspace/BackendAutomation/utils/properties.ini')
    return config