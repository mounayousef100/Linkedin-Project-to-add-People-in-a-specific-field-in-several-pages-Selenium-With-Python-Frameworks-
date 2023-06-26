from configparser import ConfigParser


def read_config(category,key):
    config = ConfigParser()
    config.read("utilities/config.ini")
    return config.get(category,key)

