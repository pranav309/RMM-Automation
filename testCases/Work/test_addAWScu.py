import time

from selenium.webdriver.common.by import By
from pageObjects.testWavePage import Test_WavePage
from pageObjects.testWaveOperations import Test_WaveOperations
from pageObjects.testLoginPage import loginPage
from pageObjects.testWaveEdit import Test_WaveEdit
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_016_addAWScu:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createAndStartWave(self, setup):
        self.logger.info("********** Test_016_addAWScu ********** ")
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

        self.logger.info("********** Creating New Wave With Host **********")
        path = "./TestData/createWaveWithHost.xlsx"
        self.crtWave = Test_WavePage(self.driver)
        self.crtWave.test_createWaveWithHost(path)
        self.logger.info("********** Successful Created New Wave With Host **********")

        self.setSync = Test_WaveEdit(self.driver)
        self.logger.info("********** Setting AWS Autoprovision For Wave **********")
        self.setSync.setAWS("AWS Trial", "AWSuser", "vpc-1608d373", "subnet-45a15a32")
        self.logger.info("********** Successfully Set AWS Autoprovision For Wave **********")

        self.logger.info("********** Setting Sync Options For The Wave **********")
        path2 = "./TestData/editSyncOptions.xlsx"
        self.setSync.test_setSyncOptions(path2,,
        self.logger.info("********** Successfully Set Sync Options For The Wave **********")

        self.logger.info("********** Starting A Wave **********")
        self.driver.find_element(By.LINK_TEXT, "Waves").click()
        self.startWave = Test_WaveOperations(self.driver)
        self.startWave.test_startWave(["AWS Trial"])
        self.logger.info("********** Successful Started A Wave **********")

        self.lp.test_clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
