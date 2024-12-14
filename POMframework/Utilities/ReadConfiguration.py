from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("C:\\Users\\roshj\\PycharmProjects\\Test\\POMframework\\configuration\\config.ini")
    return config.get(category, key)