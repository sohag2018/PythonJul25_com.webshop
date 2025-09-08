import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")#config.ini loading

class ReadConfig:

    @staticmethod
    def getBaseUrl():
        url=config.get("sit env","base_url")
        return url
    @staticmethod
    def getUsername():
        username=config.get("sit env","username")
        return username
    @staticmethod
    def getPassword():
        password=config.get("sit env","password")
        return password

    @staticmethod
    def getTitle():
        exp_title = config.get("title", "homepage")
        return exp_title