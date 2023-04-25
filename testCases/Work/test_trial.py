import time

from pageObjects.wavePage import WavePage
from pageObjects.configurationPage import Configuration
from pageObjects.waveOperations import WaveOperations
from pageObjects.loginPage import LoginPage
from pageObjects.waveEdit import SyncOptions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.drPolicyPage import DRPolicy
from pageObjects.waveDetails import WaveDetails


class Test_019_SecondFlow:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWindowsWave(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.crtWave = WavePage(self.driver)
        self.config = Configuration(self.driver)
        self.startWave = WaveOperations(self.driver)
        self.dr = DRPolicy(self.driver)
        self.setSync = SyncOptions(self.driver)
        self.details = WaveDetails(self.driver)

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        time.sleep(20)

        self.dr.addDRPolicyToWave("z", "trial", True)

        self.lp.clickOnLogout()
        self.driver.close()
        print("\n")
