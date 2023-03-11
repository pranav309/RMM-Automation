import time

from pageObjects.waveCreatePage import WavePage
from pageObjects.waveOperationsPage import WaveOperations
from pageObjects.loginPage import LoginPage
from pageObjects.waveEdit import SyncOptions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_013_CreateAndStartWave:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWindowsWave(self, setup):
        self.logger.info("********** Test_013_CreateAndStartWave ********** ")
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
        path1 = "./TestData/createWaveWithHost.xlsx"
        self.crtWave = WavePage(self.driver)
        self.crtWave.createWaveWithoutHost(path1)
        self.logger.info("********** Successful Created New Wave With Host **********")
        self.setSync = SyncOptions(self.driver)
        path2 = "./TestData/setAutoprovisionAndNIC.xlsx"
        self.setSync.setAutoprovision(path2)
        path3 = "./TestData/bulkEditOptions.xlsx"
        self.setSync.bulkEditOption(path3)
        self.logger.info("********** Starting A Wave **********")
        self.startWave = WaveOperations(self.driver)
        self.startWave.startWave(["Windows AP Automation"])
        self.logger.info("********** Successful Started A Wave **********")
        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
