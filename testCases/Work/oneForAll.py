import time
import openpyxl

from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

from pageObjects.loginPage import LoginPage
from pageObjects.wavePage import WavePage
from pageObjects.waveOperations import WaveOperations
from pageObjects.waveEdit import WaveEdit
from pageObjects.waveDetails import WaveDetails
from pageObjects.retentionPolicyPage import RetentionPolicy
from pageObjects.drPolicyPage import DRPolicy
from pageObjects.configurationPage import Configuration


class Test_000_OneForAll:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_allInOne(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.wp = WavePage(self.driver)
        self.wo = WaveOperations(self.driver)
        self.we = WaveEdit(self.driver)
        self.wd = WaveDetails(self.driver)
        self.rp = RetentionPolicy(self.driver)
        self.dr = DRPolicy(self.driver)
        self.conf = Configuration(self.driver)

        self.logger.info("********** Test_019_SecondFlow ********** ")
        self.logger.info("********** Opening Browser ********** ")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("********** Browser Opened Successfully **********\n")

        self.logger.info("********** Logging In **********")
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        self.logger.info("********** Login Successful **********\n")

        path = "./TestData/OneForAll/oneForAll.xlsx"
        workBook = openpyxl.load_workbook(path)
        sheet = workBook.active
        rows = sheet.max_row

        count = 1
        for r in range(2, rows+1):
            operation = sheet.cell(row=r, column=1).value.lower()
            if operation.find("add") != -1 and operation.find("wave") != -1 and operation.find("without") != -1:
                waveName = sheet.cell(row=r, column=3).value
                passthrough = sheet.cell(row=r, column=4).value
                self.logger.info("********** Starting TestCase "+str(count)+": Create New Wave With Upload .csv File Method **********")
                self.wp.createWaveWithoutHost(waveName, passthrough)
                self.logger.info("********** Successfully Executed TestCase: Create New Wave With Upload .csv File Method **********\n")
                count += 1

            elif operation.find("add") != -1 and operation.find("wave") != -1 and operation.find("file") != -1:
                filePath = sheet.cell(row=r, column=2).value
                self.logger.info("********** Starting TestCase " + str(count) + ": Create New Wave With Upload .csv File Method **********")
                self.wp.createWaveWithFile(filePath)
                self.logger.info("********** Successfully Executed TestCase: Create New Wave With Upload .csv File Method **********\n")
                count += 1

            elif operation.find("add") != -1 and operation.find("wave") != -1:
                filePath = sheet.cell(row=r, column=2).value
                self.logger.info("********** Starting TestCase " + str(count) + ": Create New Wave With Upload .csv File Method **********")
                self.wp.createWaveWithHost(filePath)
                self.logger.info("********** Successfully Executed TestCase: Create New Wave With Upload .csv File Method **********\n")
                count += 1

        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")