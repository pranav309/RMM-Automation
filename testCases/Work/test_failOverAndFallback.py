import time

from selenium.webdriver.common.by import By
from pageObjects.wavePage import WavePage
from pageObjects.waveOperations import WaveOperations
from pageObjects.loginPage import LoginPage
from pageObjects.waveEdit import SyncOptions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_014_FailoverAndFallback:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createAndStartWave(self, setup):
        self.logger.info("********** Test_014_FailoverAndFallback ********** ")
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

        self.logger.info("********** Creating New Wave With Host **********")
        path = "./TestData/createWaveWithHost.xlsx"
        self.crtWave = WavePage(self.driver)
        self.crtWave.createWaveWithHost(path)
        self.logger.info("********** Successful Created New Wave With Host **********")
        self.setSync = SyncOptions(self.driver)
        self.logger.info("********** Setting Autoprovision For Wave **********")
        path1 = "./TestData/setAutoprovisionAndNIC.xlsx"
        self.setSync.setAutoprovision(path1)
        self.logger.info("********** Successfully Set Autoprovision For Wave **********")
        self.logger.info("********** Setting Sync Options For The Wave **********")
        path2 = "./TestData/bulkEditOptions.xlsx"
        self.setSync.setSyncOptions(path2)
        self.logger.info("********** Successfully Set Sync Options For The Wave **********")
        self.logger.info("********** Assigning DR Policy To The Wave **********")
        self.setSync.assignDRPolicy("trial", 2, True)
        self.logger.info("********** Successfully Assigned DR Policy To The Wave **********")
        self.logger.info("********** Starting A Wave **********")
        self.driver.find_element(By.LINK_TEXT, "DR").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()
        self.startWave = WaveOperations(self.driver)
        self.startWave.startWave(["trial"])
        self.logger.info("********** Successful Started A Wave **********")
        self.waveOP = WaveOperations(self.driver)
        self.logger.info("********** Starting A Failover for Wave **********")
        self.waveOP.failoverHost("trial", True)
        self.logger.info("********** Successful Done A Failover for Wave **********")
        self.logger.info("********** Starting A Fallback for Wave **********")
        self.waveOP.fallbackHost("trial")
        self.logger.info("********** Successful Done A Fallback for Wave **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
