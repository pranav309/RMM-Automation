import time

from pageObjects.waveCreate import WavePage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_CreateWaveWithoutHost:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWaveWithoutHost(self, setup):
        self.logger.info("********** Test_003_CreateWaveWithoutHost ********** ")
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

        self.logger.info("********** Starting Create New Wave Without Host Test **********")
        path = "./TestData/createWaveWithoutHost.xlsx"
        self.crtWave = WavePage(self.driver)
        self.crtWave.createWaveWithoutHost(path)
        self.logger.info("********** Create New Wave Without Host Test Is Successful **********")

        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully ********** ")
