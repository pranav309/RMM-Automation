import time

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.loginPage import LoginPage
from pageObjects.waveOperations import WaveOperations


class Test_009_StartWave:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWaveWithHost(self, setup):
        self.logger.info("********** Test_009_StartWave ********** ")
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

        self.logger.info("********** Starting Start Wave Test **********")
        self.startWave = WaveOperations(self.driver)
        self.startWave.startWave(["linStage12", "linStage2"])
        time.sleep(5)
        self.logger.info("********** Add New Host Test Is Successful **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
