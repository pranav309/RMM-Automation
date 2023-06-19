import time

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.testLoginPage import loginPage
from pageObjects.testWavePage import Test_WavePage


class Test_005_AddHost:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWaveWithHost(self, setup):
        self.logger.info("********** Test_005_AddHost ********** ")
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

        self.logger.info("********** Starting Add New Host Test **********")
        path = "./TestData/addNewHost.xlsx"
        self.addHost = Test_WavePage(self.driver)
        self.addHost.addHostToWaves(path)
        time.sleep(5)
        self.logger.info("********** Add New Host Test Is Successful **********")
        self.lp.test_clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
