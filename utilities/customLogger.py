import logging


class LogGen:
    @staticmethod
    def loggen():

        logging.basicConfig(filename=r'C:\Users\Pranav Pawar\PycharmProjects\RMM_DataDriven\Logs\automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s:',
                            datefmt='%m/%d/%y %I:/%M:/%S %p', force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
