import time
import paramiko

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen
from pageObjects.commonObjects import CommonObjects
from pageObjects.tearDown import TearDown


class WaveOperations:
    btn_start_id = "wave_policy_wave_policy_wave_detail_start_replications"
    btn_startConfirm_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[3]/div/div/div[3]/div/button[2]"
    btn_restart_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_restart_replications']/span/i"
    btn_stop_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_stop_replications']/span/i"
    btn_pause_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_pause_replications']/span/i"
    btn_add_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_add_machine']/span/i"
    btn_fallBack_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_drPolicyFallback']/span/i"
    btn_bulkEdit_xpath = "//*[@id='content']/article/div/div[2]/p-table/div/div[1]/div[1]/button[8]/span/i"

    btn_delete_xpath = "//*[@id='content']/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[8]/span/div/i[4]"
    txt_drPolicy_xpath = "//*[@id='content']/article/div/div[2]/div[2]/div[3]/div[2]/div"
    drp_drPolicy_xpath = "//*[@id='wave_detail_wave_policy_dr_policy']/div/label"
    drp_parallelPolicy_id = "wave_policy_wave_policy_wave_detail_parallelSyncCount"
    chBox_startNow_id = "wave_detail_wave_policy_start_now"
    btn_assignPolicy_id = "wave_detail_wave_policy_assign_policy_btn"
    btn_cancelPolicy_id = "wave_detail_wave_policy_cancel_btn"
    btn_removePolicy_id = "wave_detail_wave_policy_remove_policy_btn"
    btn_deleteHost_id = "wave_detail_delete_item_delete_btn"

    txt_verifyPolicyAss_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_wave_policy_info"]/div[1]/div/div/div[1]/h4'
    txt_waveName_xpath = '//*[@id="content"]/article/div/div[1]/div/h3/strong'
    txt_waveState_xpath = '//*[@id="content"]/article/div/div[2]/div[1]/div[1]/div[2]'
    txt_totalHosts_id = "wave_policy_wave_policy_wave_detail_elapsed_time_info"
    txt_drPolicyName_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_drPolicy"]/span'
    txt_drPolicyDrp_xpath = '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul'
    txt_totalPolicies_xpath = '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li'

    # Pop-up Banners
    var_waveDetails_xpath = '//*[@id="rmm_lite_header"]/div/div[1]/div[2]'
    pop_successful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification/div'
    pop_deleteSuccessful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification[2]/div'

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def startWaveOneByOne(self, waveNames):
        for waveName in waveNames:
            co = CommonObjects(self.driver)
            val = co.findWave(waveName)
            if val == 2:
                continue
            if val == 1:
                self.driver.find_element(By.LINK_TEXT, waveName).click()
                time.sleep(5)
                if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                    self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
                else:
                    self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                    continue
            if val == 0:
                if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                    self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
            self.logger.info("********** Starting Hosts In Wave : " + waveName + " **********")
            totalHosts = len(self.driver.find_elements(By.ID, self.txt_totalHosts_id))
            for hostNo in range(1, totalHosts + 1):
                time.sleep(5)
                if totalHosts == 1:
                    self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[1]/p-tablecheckbox/div/div[2]').click()
                    time.sleep(5)
                    hostName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
                else:
                    self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[1]/p-tablecheckbox/div/div[2]').click()
                    time.sleep(5)
                    hostName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[3]/span/span').text
                self.driver.find_element(By.ID, self.btn_start_id).click()
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
                )
                note = self.driver.find_element(By.XPATH,'/html/body/app-root/simple-notifications/div/simple-notification/div').text
                self.logger.info("********** Start Status of Host : " + hostName + ",")
                self.logger.info(note, "\n")
                WebDriverWait(self.driver, 30).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.txt_waveState_xpath), "Running")
                )
                WebDriverWait(self.driver, 7200).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.txt_waveState_xpath), "Idle" or "Paused" or "Stopped")
                )
                time.sleep(5)
                if totalHosts == 1:
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/span'))
                    if elem != 0:
                        self.logger.info("********** Host : " + hostName + ", Sync Failed **********")
                        exit()
                    else:
                        state = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span').text
                        self.logger.info("********** Host : " + hostName + ", Sync " + state + " **********")
                    self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[1]/p-tablecheckbox/div/div[2]/span').click()
                else:
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                    if elem != 0:
                        self.logger.info("********** Host : " + hostName + ", Sync Failed **********")
                        exit()
                    else:
                        state = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span').text
                        self.logger.info("********** Host : " + hostName + ", Sync " + state + " **********")
                    self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[1]/p-tablecheckbox/div/div[2]/span').click()
            self.logger.info("********** Successfully Synced All Hosts In Wave : " + waveName + " **********")
            # if val == 1:
            #     self.driver.find_element(By.LINK_TEXT, "Replication").click()
            #     time.sleep(5)
            # self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def startWave(self, waveName):
        co = CommonObjects(self.driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        self.driver.find_element(By.ID, self.btn_start_id).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Start Status For Wave Name : " + waveName + ",")
        self.logger.info(note + "\n")
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element((By.XPATH, self.txt_waveState_xpath), "Running")
        )
        WebDriverWait(self.driver, 7200).until(
            EC.text_to_be_present_in_element((By.XPATH, self.txt_waveState_xpath), "Idle" or "Paused" or "Stopped")
        )
        # if val == 1:
        #     self.driver.find_element(By.LINK_TEXT, "Replication").click()
        #     time.sleep(5)
        # self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def deleteSRDetails(self, waveName):
        co = CommonObjects(self.driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        totalHosts = len(self.driver.find_elements(By.ID, self.txt_totalHosts_id))
        for hostNo in range(1, totalHosts + 1):
            syncType = ""
            targetName = ""
            if totalHosts == 1:
                for r in range(1, 6):
                    if len(self.driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[5]/span/span[' + str(r) + ']/span')) != 0:
                        syncType = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[5]/span/span[' + str(r) + ']/span').text
                        break
                sourceName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
                if len(self.driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[4]/span')) != 0:
                    targetName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[4]/span').text
            else:
                for r in range(1, 6):
                    if len(self.driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[5]/span/span[' + str(r) + ']/span')) != 0:
                        syncType = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[5]/span/span[' + str(r) + ']/span').text
                        break
                sourceName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/span').text
                if len(self.driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[4]/span')) != 0:
                    targetName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[4]/span').text
            td = TearDown(self.driver)
            if syncType == "Host Sync":
                td.deleteSR(sourceName, targetName)
            elif syncType == "Capture" or syncType == "Stage 1":
                td.deleteSR(sourceName, str(sourceName) + "-IMAGE")
            elif syncType == "Stage 1 & 2":
                td.deleteSR(sourceName, str(sourceName) + "-IMAGE")
                td.deleteSR(str(sourceName) + "-IMAGE", targetName)
            time.sleep(5)

    def verifySyncDetails(self, waveName):
        co = CommonObjects(self.driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        successCount = 0
        totalHosts = len(self.driver.find_elements(By.ID, self.txt_totalHosts_id))
        for hostNo in range(1, totalHosts + 1):
            if totalHosts == 1:
                elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/span'))
                hostName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
            else:
                elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                hostName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/span').text
            if elem == 0:
                if totalHosts == 1:
                    state = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span').text
                else:
                    state = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span').text
                self.logger.info("********** Host : " + hostName + ", Sync " + state + " **********")
                successCount += 1
            else:
                self.logger.info("********** Host : " + hostName + ", Sync Failed **********")
                self.logger.info("********** Failed Due To,\n")
                if totalHosts == 1:
                    self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/jobid-popover/span/i').click()
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/jobid-popover/ngb-popover-window/h3'))
                    )
                    details = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/jobid-popover/ngb-popover-window/div[2]/div/textarea').text
                else:
                    self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/jobid-popover/span/i').click()
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/jobid-popover/ngb-popover-window/h3'))
                    )
                    details = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/jobid-popover/ngb-popover-window/div[2]/div/textarea').text
                self.driver.find_element(By.XPATH, self.txt_waveName_xpath).click()
                lines = details.split("\n")
                last_10_lines = lines[-10:]
                self.logger.info(last_10_lines + "\n")

    def setParallelCount(self, waveName, parallelCount):
        co = CommonObjects(self.driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        pc = Select(self.driver.find_element(By.ID, self.drp_parallelPolicy_id))
        pc.select_by_visible_text(str(parallelCount))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Set Parallel Count To Wave: " + waveName + ", Status : ")
        self.logger.info(note + "\n")
        # if val == 1:
        #     self.driver.find_element(By.LINK_TEXT, "Replication").click()
        #     time.sleep(5)
        # self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def changePolicy(self, waveName, policyName, startNow):
        co = CommonObjects(self.driver)
        val = co.findDrWave(waveName)
        if val == 2:
            return
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        currentPolicy = self.driver.find_element(By.XPATH, self.txt_drPolicyName_xpath).text
        self.logger.info("********** Current DR Policy Of The Wave: "+waveName+" Is "+currentPolicy+" **********")
        self.driver.find_element(By.XPATH, self.txt_drPolicyName_xpath).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.txt_verifyPolicyAss_xpath)) != 0:
            self.logger.info("********** Policy Assignment Pop-up Banner Is Opened For Wave, " + str(waveName) + " **********")
            self.driver.find_element(By.XPATH, self.drp_drPolicy_xpath).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txt_drPolicyDrp_xpath))
            )
            totalPolicies = len(self.driver.find_elements(By.XPATH, self.txt_totalPolicies_xpath))
            if totalPolicies == 2:
                self.logger.info("********** There Is No Other DR Policy Available **********")
            else:
                for p in range(2, totalPolicies + 1):
                    tmp = self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li[' + str(p) + ']/span').text
                    if tmp == policyName:
                        self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li[' + str(p) + ']').click()
                        if startNow:
                            self.driver.find_element(By.ID, self.chBox_startNow_id).click()
                            time.sleep(5)
                        self.driver.find_element(By.ID, self.btn_assignPolicy_id).click()
                        break
                    if p == totalPolicies:
                        self.logger.info("********** There Is No DR Policy With Name : " + policyName + "**********")
                        self.driver.find_element(By.ID, self.btn_cancelPolicy_id).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
            )
            note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
            self.logger.info("********** Assign DR Policy " + policyName + " To Wave " + waveName + ", Status : ")
            self.logger.info(note + "\n")
        else:
            self.logger.info("********** Policy Assignment Pop-up Banner Is Not Opened For Wave, " + str(waveName) + " **********")
        time.sleep(5)

    def stopWave(self, waveName):
        co = CommonObjects(self.driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        self.driver.find_element(By.XPATH, self.btn_stop_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Stop Wave Status : " + waveName + ",")
        self.logger.info(note + "\n")
        # if val == 1:
        #     self.driver.find_element(By.LINK_TEXT, "Replication").click()
        #     time.sleep(5)
        # self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def pauseWave(self, waveName):
        co = CommonObjects(self.driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        self.driver.find_element(By.XPATH, self.btn_pause_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Pause Wave Status : " + waveName + ",")
        self.logger.info(note + "\n")
        # if val == 1:
        #     self.driver.find_element(By.LINK_TEXT, "Replication").click()
        #     time.sleep(5)
        # self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def restartWave(self, waveName):
        co = CommonObjects(self.driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        self.driver.find_element(By.XPATH, self.btn_restart_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Restart Wave Status : " + waveName + ",")
        self.logger.info(note + "\n")
        # if val == 1:
        #     self.driver.find_element(By.LINK_TEXT, "Replication").click()
        #     time.sleep(5)
        # self.driver.find_element(By.LINK_TEXT, "Waves").click()
