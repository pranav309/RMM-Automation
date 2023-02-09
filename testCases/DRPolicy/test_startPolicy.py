import time

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.loginPage import LoginPage
from pageObjects.drPolicyPage import DRPolicy
from selenium.webdriver.common.by import By


class Test_007_StartDRPolicy:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWaveWithHost(self, setup):
        self.logger.info("********** Test_011_StartDRPolicy ********** ")
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
        self.logger.info("********** Starting Start DR Policy Test **********")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "DR").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Policies").click()
        self.dr = DRPolicy(self.driver)
        self.dr.startPolicy([1])
        time.sleep(5)
        self.logger.info("********** Start DR Policy Test Is Successful **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
