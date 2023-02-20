import time

from pageObjects.waveCreatePage import WavePage
from pageObjects.waveOperationsPage import WaveOperations
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_011_CreateAndStartWave:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createAndStartWave(self, setup):
        self.logger.info("********** Test_011_CreateAndStartWave ********** ")
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
        self.logger.info("********** Starting A Wave **********")
        self.startWave = WaveOperations(self.driver)
        self.startWave.startWave(["test"])
        self.logger.info("********** Successful Started A Wave **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
