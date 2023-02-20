import time

from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.loginPage import LoginPage
from pageObjects.configurationPage import Configuration


class Test_011_AddVCenter:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWaveWithHost(self, setup):
        self.logger.info("********** Test_011_AddVCenter ********** ")
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

        self.logger.info("********** Starting Add vCenter Test **********")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Configuration").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "vCenter").click()
        path = "./TestData/addVcenter.xlsx"
        self.addUser = Configuration(self.driver)
        self.addUser.addVCenter(path)
        time.sleep(5)
        self.logger.info("********** Add vCenter Test Is Successful **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
