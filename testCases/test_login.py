import time

from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *************** ")
        self.logger.info("********* Verifying Home Page Title ********** ")
        self.logger.info("******* Home Page Title Test Is Passes ******* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == "RMM - v7.4.3.10":
            self.driver.close()
            self.logger.info("******* Home Page Title Test Is Passes ******* ")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****** Home Page Title Test Is Failed *******")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.logger.info("********** Opening Browser ********** ")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("********** Browser Opened Successfully **********")
        time.sleep(10)
        self.logger.info("*********** Verifying Login Test ************ ")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == "RMM - v7.4.3.10":
            self.driver.close()
            self.logger.info("************ Login Test Is Passed ************ ")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*********** Login Test Is Failed ************ ")
            assert False
