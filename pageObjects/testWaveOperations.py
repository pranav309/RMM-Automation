import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen
from utilities.commonObjects import CommonObjects

from pageObjects.testTearDown import TearDown


class WaveOperations(unittest.TestCase):
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

    def startWaveOneByOne(self, driver, waveNames):
        for waveName in waveNames:
            co = CommonObjects(driver)
            val = co.findWave(waveName)
            if val == 2:
                continue
            if val == 1:
                driver.find_element(By.LINK_TEXT, waveName).click()
                time.sleep(5)
                if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                    self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
                else:
                    self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                    continue
            if val == 0:
                if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                    self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
            self.logger.info("********** Starting Hosts In Wave : " + waveName + " **********")
            totalHosts = len(driver.find_elements(By.ID, self.txt_totalHosts_id))
            for hostNo in range(1, totalHosts + 1):
                time.sleep(5)
                if totalHosts == 1:
                    driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[1]/p-tablecheckbox/div/div[2]').click()
                    time.sleep(5)
                    hostName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
                else:
                    driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[1]/p-tablecheckbox/div/div[2]').click()
                    time.sleep(5)
                    hostName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[3]/span/span').text
                ele = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, self.btn_start_id))
                )
                ele.click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
                )
                note = driver.find_element(By.XPATH, self.pop_successful_xpath).text
                self.logger.info("********** Start Status of Host : " + hostName + ",")
                self.logger.info(note, "\n")
                time.sleep(2)
                driver.find_element(By.XPATH, self.pop_successful_xpath).click()
                WebDriverWait(driver, 30).until(
                    EC.text_to_be_present_in_element((By.XPATH, self.txt_waveState_xpath), "Running")
                )
                WebDriverWait(driver, 7200).until(
                    EC.element_to_be_clickable((By.ID, self.btn_start_id))
                )
                time.sleep(5)
                if totalHosts == 1:
                    elem = len(driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/span'))
                    if elem != 0:
                        self.logger.info("********** Host : " + hostName + ", Sync Failed **********")
                        exit()
                    else:
                        state = driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span').text
                        self.logger.info("********** Host : " + hostName + ", Sync " + state + " **********")
                    driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[1]/p-tablecheckbox/div/div[2]/span').click()
                else:
                    elem = len(driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                    if elem != 0:
                        self.logger.info("********** Host : " + hostName + ", Sync Failed **********")
                        exit()
                    else:
                        state = driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span').text
                        self.logger.info("********** Host : " + hostName + ", Sync " + state + " **********")
                    driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[1]/p-tablecheckbox/div/div[2]/span').click()
            self.logger.info("********** Successfully Synced All Hosts In Wave : " + waveName + " **********")

    def startWave(self, driver, waveName):
        co = CommonObjects(driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        ele3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.btn_start_id))
        )
        ele3.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Start Status For Wave Name : " + waveName + ",")
        self.logger.info(note + "\n")
        time.sleep(2)
        driver.find_element(By.XPATH, self.pop_successful_xpath).click()
        time.sleep(5)
        WebDriverWait(driver, 18000).until(
            EC.element_to_be_clickable((By.ID, self.btn_start_id))
        )

    def deleteSRDetails(self, driver, waveName):
        co = CommonObjects(driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        totalHosts = len(driver.find_elements(By.ID, self.txt_totalHosts_id))
        for hostNo in range(1, totalHosts + 1):
            syncType = ""
            targetName = ""
            if totalHosts == 1:
                for r in range(1, 6):
                    if len(driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[5]/span/span[' + str(r) + ']/span')) != 0:
                        syncType = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[5]/span/span[' + str(r) + ']/span').text
                        break
                sourceName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
                if len(driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[4]/span')) != 0:
                    targetName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[4]/span').text
            else:
                for r in range(1, 6):
                    if len(driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[5]/span/span[' + str(r) + ']/span')) != 0:
                        syncType = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[5]/span/span[' + str(r) + ']/span').text
                        break
                sourceName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/span').text
                if len(driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[4]/span')) != 0:
                    targetName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[4]/span').text
            td = TearDown()
            if syncType == "Host Sync":
                td.deleteSR(sourceName, targetName)
            elif syncType == "Capture" or syncType == "Stage 1":
                td.deleteSR(sourceName, str(sourceName) + "-IMAGE")
            elif syncType == "Stage 1 & 2":
                td.deleteSR(sourceName, str(sourceName) + "-IMAGE")
                td.deleteSR(str(sourceName) + "-IMAGE", targetName)

    def verifySyncSuccess(self, driver, waveName):
        co = CommonObjects(driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        successCount = 0
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, self.txt_totalHosts_id))
        )
        totalHosts = len(driver.find_elements(By.ID, self.txt_totalHosts_id))
        for hostNo in range(1, totalHosts + 1):
            if totalHosts == 1:
                elem = len(driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/span'))
                hostName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
            else:
                elem = len(driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                hostName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/span').text
            if elem == 0:
                if totalHosts == 1:
                    state = driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span').text
                else:
                    state = driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span').text
                self.logger.info("********** Host : " + hostName + ", Sync " + state + " **********")
                successCount += 1
            else:
                self.logger.info("********** Host : " + hostName + ", Sync Failed **********")
                self.logger.info("********** Failed Due To,\n")
                if totalHosts == 1:
                    driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/jobid-popover/span/i').click()
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/jobid-popover/ngb-popover-window/h3'))
                    )
                    time.sleep(3)
                    details = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/jobid-popover/ngb-popover-window/div[2]/div/textarea').text
                else:
                    driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/jobid-popover/span/i').click()
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/jobid-popover/ngb-popover-window/h3'))
                    )
                    time.sleep(3)
                    details = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/jobid-popover/ngb-popover-window/div[2]/div/textarea').text
                driver.find_element(By.XPATH, self.txt_waveName_xpath).click()
                lines = details.split("\n")
                if len(lines) > 10:
                    last_10_lines = lines[-10:]
                    log = ""
                    for i in range(1, len(last_10_lines)):
                        log += str(last_10_lines[i])
                        log += "\n"
                    self.logger.info("\n" + log)
                else:
                    self.logger.info("\n" + details)
                self.logger.info("\n")

    def setParallelCount(self, driver, waveName, parallelCount):
        co = CommonObjects(driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        pc = Select(driver.find_element(By.ID, self.drp_parallelPolicy_id))
        pc.select_by_visible_text(str(parallelCount))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Set Parallel Count To Wave: " + waveName + ", Status : ")
        self.logger.info(note + "\n")
        time.sleep(2)
        driver.find_element(By.XPATH, self.pop_successful_xpath).click()

    def changePolicy(self, driver, waveName, policyName, startNow):
        co = CommonObjects(driver)
        val = co.findDrWave(waveName)
        if val == 2:
            return
        if val == 1:
            driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        currentPolicy = driver.find_element(By.XPATH, self.txt_drPolicyName_xpath).text
        self.logger.info("********** Current DR Policy Of The Wave: "+waveName+" Is "+currentPolicy+" **********")
        driver.find_element(By.XPATH, self.txt_drPolicyName_xpath).click()
        time.sleep(5)
        if len(driver.find_elements(By.XPATH, self.txt_verifyPolicyAss_xpath)) != 0:
            self.logger.info("********** Policy Assignment Pop-up Banner Is Opened For Wave, " + str(waveName) + " **********")
            driver.find_element(By.XPATH, self.drp_drPolicy_xpath).click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txt_drPolicyDrp_xpath))
            )
            totalPolicies = len(driver.find_elements(By.XPATH, self.txt_totalPolicies_xpath))
            if totalPolicies == 2:
                self.logger.info("********** There Is No Other DR Policy Available **********")
            else:
                for p in range(2, totalPolicies + 1):
                    tmp = driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li[' + str(p) + ']/span').text
                    if tmp == policyName:
                        driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li[' + str(p) + ']').click()
                        if len(driver.find_elements(By.ID, self.chBox_startNow_id)) != 0:
                            if startNow:
                                driver.find_element(By.ID, self.chBox_startNow_id).click()
                        WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.ID, self.btn_assignPolicy_id))
                        )
                        driver.find_element(By.ID, self.btn_assignPolicy_id).click()
                        break
                    if p == totalPolicies:
                        self.logger.info("********** There Is No DR Policy With Name : " + policyName + "**********")
                        driver.find_element(By.ID, self.btn_cancelPolicy_id).click()
                        return
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
            )
            note = driver.find_element(By.XPATH, self.pop_successful_xpath).text
            self.logger.info("********** Assign DR Policy " + policyName + " To Wave " + waveName + ", Status : ")
            self.logger.info(note + "\n")
            time.sleep(2)
            driver.find_element(By.XPATH, self.pop_successful_xpath).click()
        else:
            self.logger.info("********** Policy Assignment Pop-up Banner Is Not Opened For Wave, " + str(waveName) + " **********")

    def stopWave(self, driver, waveName):
        co = CommonObjects(driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        ele1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_stop_xpath))
        )
        ele1.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Stop Wave Status : " + waveName + ",")
        self.logger.info(note + "\n")
        time.sleep(2)
        driver.find_element(By.XPATH, self.pop_successful_xpath).click()

    def pauseWave(self, driver, waveName):
        co = CommonObjects(driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        ele1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_pause_xpath))
        )
        ele1.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Pause Wave Status : " + waveName + ",")
        self.logger.info(note + "\n")
        time.sleep(2)
        driver.find_element(By.XPATH, self.pop_successful_xpath).click()

    def restartWave(self, driver, waveName):
        co = CommonObjects(driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        if val == 1:
            driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Opened Successfully **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
                return
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
        ele1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_restart_xpath))
        )
        ele1.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.pop_successful_xpath))
        )
        note = driver.find_element(By.XPATH, self.pop_successful_xpath).text
        self.logger.info("********** Restart Wave Status : " + waveName + ",")
        self.logger.info(note + "\n")
        time.sleep(2)
        driver.find_element(By.XPATH, self.pop_successful_xpath).click()
