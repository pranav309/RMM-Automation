import time

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.testLoginPage import loginPage
from pageObjects.testDrPolicyPage import Test_DRPolicy
from selenium.webdriver.common.by import By


class Test_006_CreateDRPolicy:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWaveWithHost(self, setup):
        self.logger.info("********** Test_006_CreateDRPolicy ********** ")
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

        self.logger.info("********** Starting Create New DRPolicy Test **********")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "DR").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Policies").click()
        self.dr = Test_DRPolicy(self.driver)
        path = "./TestData/tp.xlsx"
        self.dr.test_createDRPolicy(path)
        time.sleep(5)
        self.logger.info("********** Create New DRPolicy Test Is Successful **********")
        self.lp.test_clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
