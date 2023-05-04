import time

from pageObjects.wavePage import WavePage
from pageObjects.configurationPage import Configuration
from pageObjects.waveOperations import WaveOperations
from pageObjects.loginPage import LoginPage
from pageObjects.waveEdit import WaveEdit
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.drPolicyPage import DRPolicy
from pageObjects.waveDetails import WaveDetails

from selenium.webdriver.common.by import By


class Test_019_SecondFlow:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    btn_addNew_xpath = "//*[@id='policies_dr_policy_create_policy_btn']/span/i"
    rd_schedule_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[1]/div/div/input"
    rd_frequency_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[2]/div/div/input"
    rd_once_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[3]/div/div/input"
    rd_continuous_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[4]/div/div/input"

    def test_createWindowsWave(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.wp = WavePage(self.driver)
        self.conf = Configuration(self.driver)
        self.wo = WaveOperations(self.driver)
        self.dr = DRPolicy(self.driver)
        self.we = WaveEdit(self.driver)
        self.wd = WaveDetails(self.driver)

        self.logger.info("********** Test_019_SecondFlow **********")
        self.logger.info("********** Opening Browser ********** ")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("********** Browser Opened Successfully **********\n")

        self.logger.info("********** Logging In **********")
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        self.logger.info("********** Login Successful **********\n")

        time.sleep(10)
        print(len(self.driver.find_elements(By.LINK_TEXT, "tp")))
        self.driver.find_element(By.LINK_TEXT, "DR").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Policies").click()
        time.sleep(5)
        print(len(self.driver.find_elements(By.LINK_TEXT, "tp")))

        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        self.logger.info("\n \n \n")
