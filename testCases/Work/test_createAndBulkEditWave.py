import time

from pageObjects.wavePage import WavePage
from pageObjects.waveOperations import WaveOperations
from pageObjects.waveEdit import SyncOptions
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_012_CreateAndBulkEditWave:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createAndBulkEditWave(self, setup):
        self.logger.info("********** Test_012_CreateAndBulkEditWave ********** ")
        self.logger.info("********** Opening Browser ********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("********** Browser Opened Successfully **********")

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        time.sleep(20)
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Creating New Wave Without Host **********")
        path = "./TestData/createAndBulkEditWave.xlsx"
        self.crtWave = WavePage(self.driver)
        self.crtWave.createWaveWithoutHost(path)
        self.logger.info("********** Successful Created New Wave Without Host **********")
        path = "./TestData/bulkEditOptions.xlsx"
        self.syncOpt = SyncOptions(self.driver)
        self.syncOpt.bulkEditOption(path)
        self.logger.info("********** Starting A Wave **********")
        self.startWave = WaveOperations(self.driver)
        self.startWave.startWave(["Multiple Host"])
        self.logger.info("********** Successful Started A Wave **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
