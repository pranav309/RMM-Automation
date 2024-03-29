import time

from pageObjects.testWavePage import Test_WavePage
from pageObjects.testWaveOperations import Test_WaveOperations
from pageObjects.testLogin import loginPage
from pageObjects.testWaveEdit import Test_WaveEdit
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from pageObjects.testDrPolicy import Test_DRPolicy
from pageObjects.testWaveDetails import Test_WaveDetails


class Test_018_FirstFlow:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createWindowsWave(self, setup):
        self.driver = setup
        self.lp = loginPage(self.driver)
        self.crtWave = Test_WavePage(self.driver)
        self.startWave = Test_WaveOperations(self.driver)
        self.dr = Test_DRPolicy(self.driver)
        self.setSync = Test_WaveEdit(self.driver)
        self.details = Test_WaveDetails(self.driver)

        self.logger.info("********** Test_018_FirstFlow ********** ")
        self.logger.info("********** Opening Browser ********** ")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("********** Browser Opened Successfully **********")

        self.logger.info("********** Logging In **********")
        self.lp.test_setUserName(self.username)
        self.lp.test_setPassword(self.password)
        self.lp.test_clickOnLogin()
        time.sleep(20)
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Creating New Wave With Host **********")
        path1 = "./TestData/createWaveWithHost.xlsx"
        self.crtWave.test_createWaveWithHost(path1)
        self.logger.info("********** Successful Created New Wave With Host **********")

        self.logger.info("********** Adding New Host In The Wave **********")
        self.crtWave.test_addHostToWave(path1)
        self.logger.info("********** Successful Added New Host In The Wave **********")

        self.logger.info("********** Bulk Editing Sync Options For Wave **********")
        path2 = "./TestData/bulkEditOptions.xlsx"
        self.setSync.test_bulkEditSyncOption(path2)
        self.logger.info("********** Successful Bulk Edited Sync Options For Wave **********")

        self.logger.info("********** Setting Separate Sync Options For Wave **********")
        path3 = "./TestData/editSyncOptions.xlsx"
        self.setSync.test_setSyncOptions(path3)
        self.logger.info("********** Successful Set Separate Sync Options For Wave **********")

        self.logger.info("********** Setting Autoprovision For The Wave **********")
        path4 = "./TestData/setAutoprovisionAndNIC.xlsx"
        self.setSync.test_setAutoprovision(path4)
        self.logger.info("********** Successfully Set Autoprovision For The Wave **********")

        self.logger.info("********** Setting Parallel Count **********")
        self.startWave.test_setParallelCount("First Flow", "2")
        self.logger.info("********** Successfully Set Parallel Count **********")

        self.logger.info("********** Starting A Wave **********")
        self.startWave.test_startWave(["First Flow"])
        self.logger.info("********** Successful Started A Wave **********")

        self.logger.info("********** Verifying Summary & Systems Details **********")
        self.details.test_verifySyncDetails("First Flow")
        self.logger.info("********** Successfully Verified Summary & Systems Details **********")

        self.logger.info("********** Creating New DRPolicy **********")
        path5 = "./TestData/createDrPolicy.xlsx"
        self.dr.test_createDRPolicy(path5)
        time.sleep(5)
        self.logger.info("********** Successfully Created New DRPolicy **********")

        self.logger.info("********** Adding DRPolicy To Wave **********")
        self.dr.test_addDRPolicyToWave("Images", "trial", True)
        self.logger.info("********** Successfully Added DRPolicy To Wave **********")

        self.logger.info("********** Resuming DRPolicy And Verifying Sync **********")
        self.driver.find_element(By.LINK_TEXT, "DR").click()
        self.dr.resumePolicyAndVerifySyncs("trial", "First Flow")
        self.logger.info("********** Successfully Resumed DRPolicy And Verified Sync **********")

        self.logger.info("********** Changing Target Type Of Wave **********")
        path6 = "./TestData/changeTargetType.xlsx"
        self.setSync.test_changeTargetType(path6)
        self.logger.info("********** Successfully Changed Target Type Of Wave **********")

        self.logger.info("********** Starting A Wave Again **********")
        self.startWave.test_startWave("First Flow")
        self.logger.info("********** Successful Started A Wave **********")

        self.logger.info("********** Starting A Wave Again **********")
        self.startWave = Test_WaveOperations(self.driver)
        self.startWave.test_startWave("First Flow")
        self.logger.info("********** Successful Started A Wave **********")

        self.logger.info("********** Performing Failover **********")
        self.dr.test_failoverHost("First Flow", True)
        self.logger.info("********** Successful Performed Failover **********")

        self.lp.test_clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        print("\n")
