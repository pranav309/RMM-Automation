import time
import py

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.loginPage import LoginPage
from pageObjects.retentionPolicyPage import RetentionPolicy
from selenium.webdriver.common.by import By


class Test_008_CreateRetentionPolicy:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWaveWithHost(self, setup):
        self.logger.info("********** Test_008_CreateRetentionPolicy ********** ")
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

        self.logger.info("********** Starting Create New Retention Policy Test **********")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Backup & Restore").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Retention Policies").click()
        path = "./TestData/createRetentionPolicy.xlsx"
        self.rtp = RetentionPolicy(self.driver)
        self.rtp.createRetentionPolicy(path)
        time.sleep(5)
        self.logger.info("********** Create New Retention Policy Test Is Successful **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
