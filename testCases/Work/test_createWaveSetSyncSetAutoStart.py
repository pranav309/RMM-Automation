import time

from pageObjects.testWavePage import Test_WavePage
from pageObjects.testWaveOperations import Test_WaveOperations
from pageObjects.testLoginPage import loginPage
from pageObjects.testWaveEdit import Test_WaveEdit
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_013_CreateAndStartWave:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWindowsWave(self, setup):
        self.logger.info("********** Test_017_CreateAndStartWave ********** ")
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
        path1 = "./TestData/createWaveWithHost.xlsx"
        self.crtWave = Test_WavePage(self.driver)
        self.crtWave.test_createWaveWithoutHost(path1)
        self.logger.info("********** Successful Created New Wave With Host **********")
        self.setSync = Test_WaveEdit(self.driver)
        path3 = "./TestData/editSyncOptions.xlsx"
        self.setSync.test_setSyncOptions(path3,,
        path2 = "./TestData/setAutoprovisionAndNIC.xlsx"
        self.setSync.test_setAutoprovision(path2)
        self.logger.info("********** Starting A Wave **********")
        self.startWave = Test_WaveOperations(self.driver)
        self.startWave.test_startWave(["Event Script Trial 1"])
        self.logger.info("********** Successful Started A Wave **********")
        self.lp.test_clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
