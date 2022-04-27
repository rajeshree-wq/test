import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        baseURL= config.get("common info","baseURL")
        return baseURL

    @staticmethod
    def getUsername():
        username = config.get("credentials", "username")
        return username

    @staticmethod
    def getPassword():
        passowrd = config.get("credentials", "passowrd")
        return passowrd