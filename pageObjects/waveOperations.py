import time
import paramiko

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen


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

    # Pop-up Banners
    var_waveDetails_xpath = '//*[@id="rmm_lite_header"]/div/div[1]/div[2]'
    pop_successful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification/div'
    pop_deleteSuccessful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification[2]/div'

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def openWave(self, waveName):
        time.sleep(5)
        flag = 0
        if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
            if self.driver.find_element(By.LINK_TEXT, "Policies").is_displayed():
                self.driver.find_element(By.LINK_TEXT, "Replication").click()
                time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, "Waves").click()
            time.sleep(5)
            if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
                self.driver.find_element(By.LINK_TEXT, "DR").click()
                flag += 1
                time.sleep(5)
                self.driver.find_element(By.LINK_TEXT, "Waves").click()
                time.sleep(5)
                if len(self.driver.find_element(By.LINK_TEXT, waveName)) == 0:
                    flag += 1
                    self.logger.info("********** Wave : " + waveName + " Is Not Present **********")
        return flag

    def startWave(self, waveNames):
        for waveName in waveNames:
            val = self.openWave(waveName)
            if val == 2:
                return
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
                self.logger.info("********** Starting Hosts In Wave : " + waveName + " **********")
                time.sleep(10)
                totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
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
                    time.sleep(5)
                    note = self.driver.find_element(By.XPATH,'/html/body/app-root/simple-notifications/div/simple-notification/div').text
                    self.logger.info("********** Start Status of Host : " + hostName + ",")
                    self.logger.info(note, "\n")
                    WebDriverWait(self.driver, 6000).until(
                        EC.element_to_be_clickable((By.ID, self.btn_start_id))
                    )
                    time.sleep(5)
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                    if elem == 0:
                        self.logger.info("********** Host : " + hostName + ", Sync Successful **********")
                    else:
                        self.logger.info("********** Host : " + hostName + ", Sync Failed **********")
                        exit()
                    self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[1]/p-tablecheckbox/div/div[2]/span').click()

                self.logger.info("********** Successfully Synced All Hosts In Wave : " + waveName + " **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
            time.sleep(5)
            if val == 1:
                self.driver.find_element(By.LINK_TEXT, "Replication").click()
                time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def startWaveAndVerify(self, waveName):
        val = self.openWave(waveName)
        if val == 2:
            return
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            self.driver.find_element(By.ID, self.btn_start_id).click()
            time.sleep(5)
            note = self.driver.find_element(By.XPATH, '/html/body/app-root/simple-notifications/div/simple-notification/div').text
            self.logger.info("********** Start Status of Wave Name : " + waveName + ",")
            self.logger.info(note, "\n")
            time.sleep(120)
            WebDriverWait(self.driver, 18000).until(
                EC.element_to_be_clickable((By.ID, self.btn_start_id))
            )
            successCount = 0
            totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
            for hostNo in range(1, totalHosts + 1):
                if totalHosts == 1:
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/span'))
                    hostName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
                else:
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                    hostName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/span').text
                if elem == 0:
                    self.logger.info("********** Host : " + hostName + ", Sync Successful **********")
                    successCount += 1
                else:
                    self.logger.info("********** Host : " + hostName + ", Sync Failed **********")
                    self.logger.info("********** Failed Due To,\n")
                    if totalHosts == 1:
                        self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/a/i').click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/jobid-popover/span/i').click()
                        time.sleep(5)
                        details = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/jobid-popover/ngb-popover-window/div[2]/div/textarea').text
                    else:
                        self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/a/i').click()
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/jobid-popover/span/i').click()
                        time.sleep(5)
                        details = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/jobid-popover/ngb-popover-window/div[2]/div/textarea').text
                    self.logger.info(details + "\n")
                time.sleep(5)
                syncType = ""
                for r in range(1, 6):
                    if len(self.driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[5]/span/span[' + str(r) + ']/span')) != 0:
                        syncType = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[5]/span/span[' + str(r) + ']/span').text
                        break
                sourceName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/span').text
                targetName = ""
                if len(self.driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[4]/span')) != 0:
                    targetName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[4]/span').text
                if syncType == "Host Sync":
                    self.deleteSR(sourceName, targetName)
                elif syncType == "Capture" or syncType == "Stage 1":
                    self.deleteSR(sourceName, str(sourceName)+"-IMAGE")
                elif syncType == "Stage 1 & 2":
                    self.deleteSR(sourceName, str(sourceName)+"-IMAGE")
                    self.deleteSR(str(sourceName)+"-IMAGE", targetName)
                time.sleep(5)
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def setParallelCount(self, waveName, parallelCount):
        val = self.openWave(waveName)
        if val == 2:
            return
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            pc = Select(self.driver.find_element(By.ID, self.drp_parallelPolicy_id))
            pc.select_by_visible_text(parallelCount)
            time.sleep(5)
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def assignPolicy(self, waveName, policyName, startNow):
        val = self.openWave(waveName)
        if val == 2:
            return
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            self.driver.find_element(By.XPATH, self.txt_drPolicy_xpath).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.txt_verifyPolicyAss_xpath)) != 0:
                self.logger.info("********** Policy Assignment Pop-up Banner Was Opened For Wave, " + str(waveName) + " **********")
                self.driver.find_element(By.XPATH, self.drp_drPolicy_xpath).click()
                totalPolicies = len(self.driver.find_elements(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li'))
                if totalPolicies == 1:
                    self.logger.info("********** There Is No DR Policy Available **********")
                else:
                    count = 2
                    for p in range(2, totalPolicies+1):
                        tmp = self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li['+str(p)+']/span').text
                        if tmp == policyName:
                            break
                        count += 1
                    if count == totalPolicies+1:
                        self.logger.info("********** There Is No DR Policy Available With Name : "+policyName+"**********")
                        self.driver.find_element(By.ID, self.btn_cancelPolicy_id).click()
                    else:
                        self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li['+str(count)+']').click()
                        if startNow:
                            self.driver.find_element(By.ID, self.chBox_startNow_id).click()
                            time.sleep(5)
                        self.driver.find_element(By.ID, self.btn_assignPolicy_id).click()
                        time.sleep(5)
                        note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
                        self.logger.info("********** Assign DR Policy To Wave Status : " + waveName + "," + policyName + ",")
                        self.logger.info(note + "\n")
            else:
                self.logger.info("********** Policy Assignment Pop-up Banner Was Not Opened For Wave, " + str(waveName) + " **********")
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        time.sleep(5)
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def changePolicy(self, waveName, policyNumber, startNow):
        val = self.openWave(waveName)
        if val == 2:
            return
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="wave_policy_wave_policy_wave_detail_drPolicy"]/span').click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.txt_verifyPolicyAss_xpath)) != 0:
            self.logger.info("********** Policy Assignment Pop-up Banner Is Opened For Wave, " + str(waveName) + " **********")
            self.driver.find_element(By.XPATH, self.drp_drPolicy_xpath).click()
            self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li[' + str(policyNumber) + ']').click()
            if policyNumber == 1:
                self.driver.find_element(By.ID, self.btn_removePolicy_id).click()
            else:
                if startNow:
                    self.driver.find_element(By.ID, self.chBox_startNow_id).click()
                self.driver.find_element(By.ID, self.btn_assignPolicy_id).click()
        else:
            self.logger.info("********** Policy Assignment Pop-up Banner Is Not Opened For Wave, " + str(waveName) + " **********")
        time.sleep(5)

    @staticmethod
    def deleteSR(source, target):
        vm_ip = "172.29.30.127"
        vm_username = "root"
        vm_password = "rackware"

        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(vm_ip,
                    username=vm_username,
                    password=vm_password,
                    look_for_keys=False)
        ssh.exec_command("rw ic srd "+str(source)+" --target "+str(target))

    def stopWave(self, waveName):
        val = self.openWave(waveName)
        if val == 2:
            return
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            self.driver.find_element(By.XPATH, self.btn_stop_xpath).click()
            time.sleep(5)
            note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
            self.logger.info("********** Stop Wave Status : " + waveName + ",")
            self.logger.info(note + "\n")
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def pauseWave(self, waveName):
        val = self.openWave(waveName)
        if val == 2:
            return
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            self.driver.find_element(By.XPATH, self.btn_pause_xpath).click()
            time.sleep(5)
            note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
            self.logger.info("********** Pause Wave Status : " + waveName + ",")
            self.logger.info(note + "\n")
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def restartWave(self, waveName):
        val = self.openWave(waveName)
        if val == 2:
            return
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            self.driver.find_element(By.XPATH, self.btn_restart_xpath).click()
            time.sleep(5)
            note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
            self.logger.info("********** Restart Wave Status : " + waveName + ",")
            self.logger.info(note + "\n")
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def deleteHost(self, waveName, hostNames):
        val = self.openWave(waveName)
        if val == 2:
            return
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
            res = tuple(map(str, hostNames.split(', ')))
            for hostName in res:
                count = 1
                for i in range(1, totalHosts+1):
                    if totalHosts == 1:
                        tmp = self.driver.find_element(By.XPATH,'//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
                        if tmp == hostName:
                            self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[8]/span/div/i[4]').click()
                            self.hostDeleteState(hostName)
                            break
                    else:
                        tmp = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(i)+']/td[3]/span/span').text
                        if tmp == hostName:
                            self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(count)+']/td[8]/span/div/i[4]').click()
                            self.hostDeleteState(hostName)
                            break
                        else:
                            count += 1
                    if count == totalHosts+1 or totalHosts == 1:
                        self.logger.info("********** There Was No Host With Name : "+hostName+"**********")
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def hostDeleteState(self, hostName):
        time.sleep(5)
        self.driver.find_element(By.ID, self.btn_deleteHost_id).click()
        note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Delete Status For Host : " + hostName + ",")
        self.logger.info(note + "\n")
