import unittest

from utilities.customLogger import LogGen


from pageObjects.testLogin import LoginPage
from pageObjects.testWavePage import WavePage
from pageObjects.testWaveOperations import WaveOperations
from pageObjects.testWaveEdit import WaveEdit
from pageObjects.testWaveDetails import WaveDetails
from pageObjects.testRetentionPolicy import RetentionPolicy
from pageObjects.testDrPolicy import DRPolicy
from pageObjects.testConfiguration import Configuration
from pageObjects.testTearDown import TearDown

lp = LoginPage()
wp = WavePage()
wo = WaveOperations()
we = WaveEdit()
wd = WaveDetails()
rp = RetentionPolicy()
dr = DRPolicy()
conf = Configuration()
td = TearDown()


class CustomTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', driver=None, count=None, path=None, start=None, end=None, waveName=None, policyName=None, val=None, hostName=None, uName=None, password=None, trueFalse=None):
        super().__init__(methodName)
        self.driver = driver
        self.count = count
        self.path = path
        self.start = start
        self.end = end
        self.waveName = waveName
        self.trueFalse = trueFalse
        self.hostName = hostName
        self.val = val
        self.policyName = policyName
        self.uName = uName
        self.password = password


class Test_AllInOne(CustomTestCase):

    logger = LogGen.loggen()

    # login
    def test_setUserName(self):
        lp.setUserName(self.driver, self.uName)

    def test_setPassword(self):
        lp.setPassword(self.driver, self.password)

    def test_clickOnLogin(self):
        lp.clickOnLogin(self.driver, self.uName, self.password)

    def test_clickOnLogout(self):
        lp.clickOnLogout(self.driver)

    # Wave Page
    def test_createWaveWithoutHost(self):
        self.logger.info("********** Starting TestCase "+str(self.count)+": Create New Wave Without Hosts **********")
        wp.createWaveWithoutHost(self.driver, self.waveName, self.trueFalse)
        self.logger.info("********** Successfully Executed TestCase: Create New Wave Without Hosts **********\n \n")

    def test_createWaveWithFile(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Create New Wave With Upload .csv File Method **********")
        wp.createWaveWithFile(self.driver, self.path)
        self.logger.info("********** Successfully Executed TestCase: Create New Wave With Upload .csv File Method **********\n \n")

    def test_createWaveWithHost(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Create New Wave With Host **********")
        wp.createWaveWithHost(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Create New Wave With Host **********\n \n")

    def test_addHostToWave(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Add New Hosts To Wave **********")
        wp.addHostToWave(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Add New Hosts To Wave **********\n \n")

    def test_searchWave(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Search A Wave **********")
        wp.searchWave(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Search A Wave **********\n \n")

    def test_searchHost(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Search A Host **********")
        wp.searchHost(self.driver, self.waveName, self.hostName)
        self.logger.info("********** Successfully Executed TestCase: Search A Host **********\n \n")

    # Wave Operations
    def test_startWaveOneByOne(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Start Wave One By One And Verify **********")
        wo.startWaveOneByOne(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Start Wave One By One And Verify **********\n \n")

    def test_startWave(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Start Wave And Verify **********")
        wo.startWave(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Start Wave And Verify **********\n \n")

    def test_deleteSRDetails(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Delete Sync Relation Data From RMM SSH Of Wave **********")
        wo.deleteSRDetails(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Delete Sync Relation Data From RMM SSH Of Wave **********\n \n")

    def test_verifySyncSuccess(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Verify Sync Success Or Fail Details **********")
        wo.verifySyncSuccess(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Verify Sync Success Or Fail Details **********\n \n")

    def test_setParallelCount(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Set Parallel Count **********")
        wo.setParallelCount(self.driver, self.waveName, self.val)
        self.logger.info("********** Successfully Executed TestCase: Set Parallel Count **********\n \n")

    def test_changePolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Change/Remove DR Policy Of Wave **********")
        wo.changePolicy(self.driver, self.waveName, self.policyName, self.trueFalse)
        self.logger.info("********** Successfully Executed TestCase: Remove DR Policy Of Wave **********\n \n")

    def test_stopWave(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Stop Wave **********")
        wo.stopWave(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Stop Wave **********\n \n")

    def test_pauseWave(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Pause Wave **********")
        wo.pauseWave(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Pause Wave **********\n \n")

    def test_restartWave(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Restart Wave **********")
        wo.restartWave(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Pause Wave **********\n \n")

    # Wave Edits
    def test_setAutoprovision(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Set Autoprovision **********")
        we.setAutoprovision(self.driver, self.path)
        self.logger.info("********** Successfully Executed TestCase: Set Autoprovision **********\n \n")

    def test_setSyncOptions(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Set Sync Options **********")
        we.setSyncOptions(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Set Sync Options **********\n \n")

    def test_bulkEditSyncOption(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Bulk Edit Sync Options **********")
        we.bulkEditSyncOption(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Bulk Edit Sync Options **********\n \n")

    def test_changeTargetType(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Change Target Type **********")
        we.changeTargetType(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Change Target Type **********\n \n")

    def test_moveHosts(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Move Host Between Waves **********")
        we.moveHosts(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Move Host Between Waves **********\n \n")

    def test_changeVcenterData(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Change vCenter Details **********")
        we.changeVcenterData(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Change vCenter Details **********\n \n")

    # Wave Details
    def test_verifySyncDetails(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Verify Sync System And Summary Details **********")
        wd.verifySyncDetails(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Verify Sync System And Summary Details **********\n \n")

    def test_tngDetails(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Verify TNG Details **********")
        wd.tngDetails()
        self.logger.info("********** Successfully Executed TestCase: Verify TNG Details **********\n \n")

    def test_checkWaveStatus(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Check Wave Status **********")
        wd.checkWaveStatus(self.driver,  self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Check Wave Status **********\n \n")

    def test_totalSuccessfulSyncs(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Total Successful Syncs **********")
        wd.totalSuccessfulSyncs(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Total Successful Syncs **********\n \n")

    def test_checkHosts(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Check Host **********")
        wd.checkHosts(self.driver, self.waveName, self.hostName)
        self.logger.info("********** Successfully Executed TestCase: Check Host **********\n \n")

    # Retention Policy
    def test_createRetentionPolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Create Retention Policy **********")
        rp.createRetentionPolicy(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Create Retention Policy **********\n \n")

    def test_startRetentionPolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Start Retention Policy **********")
        rp.startRetentionPolicy(self.driver, self.val, self.hostName)
        self.logger.info("********** Successfully Executed TestCase: Start Retention Policy **********\n \n")

    def test_editRetentionPolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Edit Retention Policy **********")
        rp.editRetentionPolicy(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Edit Retention Policy **********\n \n")

    def test_deleteRetentionPolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Delete Retention Policy **********")
        rp.deleteRetentionPolicy(self.driver, self.policyName, self.trueFalse)
        self.logger.info("********** Successfully Executed TestCase: Delete Retention Policy **********\n \n")

    # DR Policy
    def test_createDRPolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Create New DR Policy **********")
        dr.createDRPolicy(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Create New DR Policy **********\n \n")

    def test_findPolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Search DR Policy **********")
        dr.findPolicy(self.driver, self.policyName)
        self.logger.info("********** Successfully Executed TestCase: Search DR Policy **********\n \n")

    def test_addDRPolicyToWave(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Assign DR Policy To Wave **********")
        dr.addDRPolicyToWave(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Assign DR Policy To Wave **********\n \n")

    def test_checkDrPolicyState(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Check DR Policy Status **********")
        dr.checkDrPolicyState(self.driver, self.policyName)
        self.logger.info("********** Successfully Executed TestCase: Check DR Policy Status **********\n \n")

    def test_resumePolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Resume Policy **********")
        dr.resumePolicy(self.driver, self.policyName)
        self.logger.info("********** Successfully Executed TestCase: Resume Policy **********\n \n")

    def test_verifyDRHostSyncStatus(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Check DR Policy Host Sync Status **********")
        dr.verifyDRHostSyncStatus(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Check DR Policy Host Sync Status **********\n \n")

    def test_pauseDRPolicy(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Pause DR Policy **********")
        dr.pauseDRPolicy(self.driver, self.policyName)
        self.logger.info("********** Successfully Executed TestCase: Pause DR Policy **********\n \n")

    def test_failoverHost(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Failover Host **********")
        dr.failoverHost(self.driver, self.waveName, self.trueFalse)
        self.logger.info("********** Successfully Executed TestCase: Failover Host **********\n \n")

    def test_fallbackHost(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Fallback Host **********")
        dr.fallbackHost(self.driver, self.waveName)
        self.logger.info("********** Successfully Executed TestCase: Fallback Host **********\n \n")

    # Configuration
    def test_addNewCloudUser(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Create New Cloud User **********")
        conf.addNewCloudUser(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Create New Cloud User **********\n \n")

    def test_findClouduser(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Find Cloud User **********")
        conf.findClouduser(self.driver, self.uName)
        self.logger.info("********** Successfully Executed TestCase: Find Cloud User **********\n \n")

    def test_addVCenter(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Create New vCenter **********")
        conf.addVCenter(self.driver, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Create New vCenter **********\n \n")

    def test_findVCenter(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Find vCenter User **********")
        conf.findVCenter(self.driver, self.uName)
        self.logger.info("********** Successfully Executed TestCase: Find vCenter User **********\n \n")

    def test_tearDown(self):
        self.logger.info("********** Starting TestCase " + str(self.count) + ": Perform Tear Down **********")
        td.tearDown1(self.driver, self.count, self.path, self.start, self.end)
        self.logger.info("********** Successfully Executed TestCase: Perform Tear Down **********\n \n")
