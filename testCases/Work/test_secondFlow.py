from pageObjects.wavePage import WavePage
from pageObjects.configurationPage import Configuration
from pageObjects.waveOperations import WaveOperations
from pageObjects.loginPage import LoginPage
from pageObjects.waveEdit import WaveEdit
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
        self.wp = WavePage(self.driver)
        self.conf = Configuration(self.driver)
        self.wo = WaveOperations(self.driver)
        self.dr = DRPolicy(self.driver)
        self.we = WaveEdit(self.driver)
        self.wd = WaveDetails(self.driver)

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

        self.logger.info("********** Starting TestCase 1: Create New Wave With Upload .csv File Method **********")
        path1 = r"C:\Users\Pranav Pawar\PycharmProjects\RMM_DataDriven\TestData\secondFlow\Second Flow.csv"
        self.wp.createWaveWithFile(path1)
        self.logger.info("********** Successfully Executed TestCase: Create New Wave With Upload .csv File Method **********\n")

        self.logger.info("********** Starting TestCase 2: Add New vCenter **********")
        path2 = "./TestData/secondFlow/addVcenter.xlsx"
        self.conf.addVCenter(path2)
        self.logger.info("********** Successfully Executed TestCase: Add New vCenter **********\n")

        self.logger.info("********** Starting TestCase 3: Set Autoprovision For The Wave **********")
        path3 = "./TestData/secondFlow/setAutoprovisionAndNIC.xlsx"
        self.we.setAutoprovision(path3)
        self.logger.info("********** Successfully Executed TestCase: Set Autoprovision For The Wave **********\n")

        self.logger.info("********** Starting TestCase 4: Bulk Edit Sync Options For Wave **********")
        path4 = "./TestData/secondFlow/bulkEditOptions.xlsx"
        self.we.bulkEditSyncOption(path4)
        self.logger.info("********** Successfully Executed TestCase: Bulk Edit Sync Options For Wave **********\n")

        self.logger.info("********** Starting TestCase 5 & 6: Edit Sync Options For Linux Wave **********")
        path5 = "./TestData/secondFlow/editSyncOptions.xlsx"
        self.we.setSyncOptions(path5)
        self.logger.info("********** Successfully Executed TestCase: Edit Sync Options For Linux Wave **********\n")

        self.logger.info("********** Starting TestCase 7: Change Datastore For All Waves **********")
        self.we.changeDatastore("Second Flow", "esx09-datastore2")
        self.logger.info("********** Successfully Executed TestCase: Change Datastore For All Waves **********\n")

        self.logger.info("********** Starting TestCase 8: Bulk Edit Sync Options For Windows Hosts **********")
        path6 = "./TestData/secondFlow/bulkEditOptionsWindows.xlsx"
        self.we.bulkEditSyncOption(path6)
        self.logger.info("********** Successfully Executed TestCase: Bulk Edit Sync Options For Windows Hosts **********\n")

        self.logger.info("********** Starting TestCase 9.1: Set Parallel Count **********")
        self.wo.setParallelCount("Second Flow", "4")
        self.logger.info("********** Successfully Executed TestCase: Set Parallel Count **********\n")

        self.logger.info("********** Starting TestCase 9.2: Start & Verify A Wave **********")
        # Wave name i.e. to be started
        self.wo.startWave("Second Flow")
        self.logger.info("********** Successfully Executed TestCase: Start & Verify A Wave **********\n")

        self.logger.info("********** Starting TestCase 9.3: Check Wave Status **********")
        # Wave name i.e. to be started
        self.wd.checkWaveStatus("Second Flow")
        self.wd.totalSuccessfulSyncs("Second Flow")
        self.logger.info("********** Successfully Executed TestCase: Check Wave Status **********\n")

        self.logger.info("********** Starting TestCase 10: Changing Sync Options for A Wave **********")
        # Wave name, Sync option i.e. to be changed, Yes or No
        # Sync Options : TNG, Verbose, Passwordless, Allow Direct Fscopy, Allow FS Deletion, No Transfer, Transfer Compress, No Transfer Compress, Ignore Missing, No In Place, No Reboot, Include SAN, Exclude SAN, Override RMM Storage Check, Delete All Target FS, Keep Target Layout, Cloud Init
        self.we.changeBulkEditOption("Second Flow", "No Transfer", "No")
        self.logger.info("********** Successfully Executed TestCase: Changed Sync Options for A Wave **********\n")

        self.logger.info("********** Starting TestCase 11.1: Start & Verify A Wave Again **********")
        # Wave name i.e. to be started
        self.wo.startWave("Second Flow")
        self.logger.info("********** Successfully Executed TestCase: Start & Verify A Wave Again **********\n")

        self.logger.info("********** Starting TestCase 11.2: Check Wave Status **********")
        # Wave name i.e. to be started
        self.wd.checkWaveStatus("Second Flow")
        self.wd.totalSuccessfulSyncs("Second Flow")
        self.logger.info("********** Successfully Executed TestCase: Check Wave Status **********\n")

        self.logger.info("********** Starting TestCase 12: Create Another Wave Without Hosts **********")
        # Wave name i.e. to be created, passthrough option check
        self.wp.createWaveWithoutHost("Second Flow 1", True)
        self.logger.info("********** Successfully Executed TestCase: Create Another Wave Without Hosts **********\n")

        self.logger.info("********** Starting TestCase 13.1: Move Hosts From One Wave To Another Wave **********")
        # Source wave name, Host Numbers which are to be moved, Target wave name
        # Please enter host numbers in decreasing order...
        self.we.moveHosts("Second Flow", "2, 1", "Second Flow 1")
        self.logger.info("********** Successfully Executed TestCase: Move Hosts From One Wave To Another Wave **********\n")

        self.logger.info("********** Starting TestCase 13.2: Check Available Hosts **********")
        # Source wave name, Host Numbers which are to be moved, Target wave name
        # Please enter host numbers in decreasing order...
        self.wd.checkHosts("Second Flow 1", "psp-MyLinSecondFlow-src1, psp-MyLinSecondFlow-src2")
        self.logger.info("********** Successfully Executed TestCase: Move Hosts From One Wave To Another Wave **********\n")

        self.logger.info("********** Starting TestCase 14.1: Changing Target Type Of Linux Hosts Wave **********")
        path7 = "./TestData/secondFlow/changeTargetType.xlsx"
        self.we.changeTargetType(path7, 2, 3)
        self.logger.info("********** Successfully Executed TestCase: Changed Target Type Of Linux Hosts Wave **********\n")

        self.logger.info("********** Starting TestCase 14.2: Set Parallel Count **********")
        self.wo.setParallelCount("Second Flow 1", "2")
        self.logger.info("********** Successfully Executed TestCase: Set Parallel Count **********\n")

        self.logger.info("********** Starting TestCase 14.3: Start & Verify A Wave Again **********")
        # Wave name i.e. to be started
        self.wo.startWave("Second Flow 1")
        self.logger.info("********** Successfully Executed TestCase: Start & Verify A Wave Again **********\n")

        self.logger.info("********** Starting TestCase 15.1: Change Target Type Of Windows Hosts Wave **********")
        self.we.changeTargetType(path7, 4, 5)
        self.logger.info("********** Successfully Executed TestCase: Change Target Type Of Windows Hosts Wave **********\n")

        self.logger.info("********** Starting TestCase 15.2: Start & Verify A Wave Again **********")
        # Wave name i.e. to be started
        self.wo.startWave("Second Flow")
        self.logger.info("********** Successfully Executed TestCase: Start & Verify A Wave Again **********\n")

        self.logger.info("********** Starting TestCase 16.1: Create New DRPolicy **********")
        path8 = "./TestData/secondFlow/createDrPolicy.xlsx"
        self.dr.createDRPolicy(path8)
        self.logger.info("********** Successfully Executed TestCase: Create New DRPolicy **********\n")

        self.logger.info("********** Starting TestCase 16.2, 17 & 18: Add DRPolicy To Wave **********")
        self.dr.addDRPolicyToWave("Second Flow", "SecondFlowWin", True)
        self.dr.addDRPolicyToWave("Second Flow 1", "SecondFlowLin", True)
        self.logger.info("********** Successfully Executed TestCase: Add DRPolicy To Wave **********\n")

        self.logger.info("********** Starting TestCase 19.1: Pause DR Policy For Windows **********")
        self.dr.pauseDRPolicy("SecondFlowWin")
        self.logger.info("********** Successfully Executed TestCase: Pause DR Policy For Windows **********\n")

        self.logger.info("********** Starting TestCase 19.2: Perform Failover Windows Hosts **********")
        self.dr.failoverHost("Second Flow", False)
        self.logger.info("********** Successfully Executed TestCase: Perform Failover Windows Hosts **********\n")

        self.logger.info("********** Starting TestCase 20.1: Pause DR Policy For Linux **********")
        self.dr.pauseDRPolicy("SecondFlowLin")
        self.logger.info("********** Successfully Executed TestCase: Pause DR Policy For Linux **********\n")

        self.logger.info("********** Starting TestCase 20.2: Change Target Type Of Wave **********")
        self.we.changeTargetType(path7, 6, 7)
        self.logger.info("********** Successfully Executed TestCase: Change Target Type Of Wave **********\n")

        self.logger.info("********** Starting TestCase 20.3: Resume DRPolicy And Verify Sync **********")
        self.dr.resumePolicyAndVerifySyncs("SecondFlowLin", "Second Flow 1")
        self.logger.info("********** Successfully Executed TestCase: Resume DRPolicy And Verify Sync **********\n")

        self.lp.clickOnLogout()
        self.logger.info("********** Logout Successful **********")
        self.driver.close()
        self.logger.info("********** Browser Closed Successfully **********")
        self.logger.info("\n \n \n")
