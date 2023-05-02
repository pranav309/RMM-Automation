import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        userName = config.get('common info', 'username')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
