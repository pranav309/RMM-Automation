import time

from pageObjects.waveCreate import WavePage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_CreateWaveWithHost:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWaveWithHost(self, setup):
        self.logger.info("********** Test_004_CreateWaveWithHost ********** ")
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

        self.logger.info("********** Starting Create New Wave With Host Test **********")
        path = "./TestData/createWaveWithHost.xlsx"
        self.crtWave = WavePage(self.driver)
        self.crtWave.createWaveWithHost(path)
        self.logger.info("********** Create New Wave With Host Test Is Successful **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")