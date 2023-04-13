import time

from pageObjects.wavePage import WavePage
from pageObjects.waveOperations import WaveOperations
from pageObjects.loginPage import LoginPage
from pageObjects.waveEdit import SyncOptions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from pageObjects.drPolicyPage import DRPolicy


class Test_014_FirstFlow:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWindowsWave(self, setup):

        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.crtWave = WavePage(self.driver)
        self.startWave = WaveOperations(self.driver)
        self.dr = DRPolicy(self.driver)
        self.setSync = SyncOptions(self.driver)

        self.logger.info("********** Test_014_FirstFlow ********** ")
        self.logger.info("********** Opening Browser ********** ")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("********** Browser Opened Successfully **********")

        self.logger.info("********** Logging In **********")
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        time.sleep(20)
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Setting Separate Sync Options For Wave **********")
        path3 = "./TestData/editSyncOptions.xlsx"
        self.setSync.setSyncOptions(path3)
        self.logger.info("********** Successful Set Separate Sync Options For Wave **********")

        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
