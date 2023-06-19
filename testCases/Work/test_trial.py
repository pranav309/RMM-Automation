import time

from pageObjects.testWavePage import Test_WavePage
from pageObjects.testConfigurationPage import Test_Configuration
from pageObjects.testWaveOperations import Test_WaveOperations
from pageObjects.testLoginPage import loginPage
from pageObjects.testWaveEdit import Test_WaveEdit
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.testDrPolicyPage import Test_DRPolicy
from pageObjects.testWaveDetails import Test_WaveDetails

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
        self.lp = loginPage(self.driver)
        self.wp = Test_WavePage(self.driver)
        self.conf = Test_Configuration(self.driver)
        self.wo = Test_WaveOperations(self.driver)
        self.dr = Test_DRPolicy(self.driver)
        self.we = Test_WaveEdit(self.driver)
        self.wd = Test_WaveDetails(self.driver)

        self.logger.info("********** Test_019_SecondFlow **********")
        self.logger.info("********** Opening Browser ********** ")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("********** Browser Opened Successfully **********\n")

        self.logger.info("********** Logging In **********")
        self.lp.test_setUserName(self.username)
        self.lp.test_setPassword(self.password)
        self.lp.test_clickOnLogin()
        self.logger.info("********** Login Successful **********\n")

        time.sleep(10)
        print(len(self.driver.find_elements(By.LINK_TEXT, "tp")))
        self.driver.find_element(By.LINK_TEXT, "DR").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Policies").click()
        time.sleep(5)
        print(len(self.driver.find_elements(By.LINK_TEXT, "tp")))

        self.lp.test_clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        self.logger.info("\n \n \n")
