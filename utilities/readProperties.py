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

    @staticmethod
    def getSourceURL():
        sourceURL = config.get('common info', 'sourceURL')
        return sourceURL

    @staticmethod
    def getSourceIP():
        sourceIP = config.get('common info', 'sourceIP')
        return sourceIP

    @staticmethod
    def getSourceUserName():
        sourceUserName = config.get('common info', 'sourceUsername')
        return sourceUserName

    @staticmethod
    def getSourcePassword():
        sourcePassword = config.get('common info', 'sourcePassword')
        return sourcePassword

    @staticmethod
    def getCWHVCUserName():
        cwhvcUserName = config.get('common info', 'cwhvcUsername')
        return cwhvcUserName

    @staticmethod
    def getCWHVCPassword():
        cwhvcPassword = config.get('common info', 'cwhvcPassword')
        return cwhvcPassword
