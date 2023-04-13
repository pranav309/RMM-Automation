import time

from selenium.webdriver.common.by import By
from pageObjects.wavePage import WavePage
from pageObjects.waveOperations import WaveOperations
from pageObjects.loginPage import LoginPage
from pageObjects.waveEdit import SyncOptions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_015_addOCIcu:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createAndStartWave(self, setup):
        self.logger.info("********** Test_015_addOCIcu ********** ")
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
        self.logger.info("********** Setting OCI Autoprovision For Wave **********")
        self.setSync.setOCI("OCI Trial", "OCIuser", "Network2", "Public Subnet hjme:PHX-AD-1", "hjme:PHX-AD-1")
        self.logger.info("********** Successfully Set OCI Autoprovision For Wave **********")

        self.logger.info("********** Setting Sync Options For The Wave **********")
        path2 = "./TestData/editSyncOptions.xlsx"
        self.setSync.setSyncOptions(path2)
        self.logger.info("********** Successfully Set Sync Options For The Wave **********")

        self.logger.info("********** Starting A Wave **********")
        self.driver.find_element(By.LINK_TEXT, "Waves").click()
        self.startWave = WaveOperations(self.driver)
        self.startWave.startWave(["OCI Trial"])
        self.logger.info("********** Successful Started A Wave **********")

        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
