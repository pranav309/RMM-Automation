import time

from pageObjects.testWavePage import Test_WavePage
from pageObjects.testWaveOperations import Test_WaveOperations
from pageObjects.testWaveEdit import Test_WaveEdit
from pageObjects.testLoginPage import loginPage
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

        self.lp = loginPage(self.driver)
        self.lp.test_setUserName(self.username)
        self.lp.test_setPassword(self.password)
        self.lp.test_clickOnLogin()
        time.sleep(20)
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Creating New Wave Without Host **********")
        path = "./TestData/createAndBulkEditWave.xlsx"
        self.crtWave = Test_WavePage(self.driver)
        self.crtWave.test_createWaveWithoutHost(path)
        self.logger.info("********** Successful Created New Wave Without Host **********")
        path = "./TestData/bulkEditOptions.xlsx"
        self.syncOpt = Test_WaveEdit(self.driver)
        self.syncOpt.bulkEditOption(path)
        self.logger.info("********** Starting A Wave **********")
        self.startWave = Test_WaveOperations(self.driver)
        self.startWave.test_startWave(["Multiple Host"])
        self.logger.info("********** Successful Started A Wave **********")
        self.lp.test_clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
