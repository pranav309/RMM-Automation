import time
import unittest
import paramiko

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen
from utilities.commonObjects import CommonObjects


class WaveDetails(unittest.TestCase):

    txt_systemsDetails_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[2]/td/item-details/div/div/p-tabview/div/ul/li[2]/a/span"
    txt_waveStatus_xpath = '//*[@id="content"]/article/div/div[2]/div[1]/div[1]/div[2]'

    # Validations
    val_sourceData_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[2]/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/label'
    val_systemData_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[2]/td/item-details/div/div/p-tabview/div/div/p-tabpanel[2]/div/div[1]/label'

    # pop-up banners
    var_waveDetails_xpath = '//*[@id="rmm_lite_header"]/div/div[1]/div[2]'

    txt_waveName_xpath = '//*[@id="content"]/article/div/div[1]/div/h3/strong'
    txt_totalHosts_id = "wave_policy_wave_policy_wave_detail_elapsed_time_info"

    logger = LogGen.loggen()

    def verifySyncDetails(self, driver, waveName):
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
        self.logger.info("********** Total Available Hosts : " + str(totalHosts) + " ,")
        if totalHosts == 1:
            self.verifySyncDetailsOne(driver)
        else:
            self.verifySyncDetailsTwo(driver, totalHosts)

    def verifySyncDetailsOne(self, driver):
        driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/a/i').click()
        hostName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
        self.logger.info("********** Sync Details For Host: "+hostName+" ,")
        tmp = 1
        while tmp < 3:
            time.sleep(5)
            if tmp == 1:
                self.logger.info("********** Summary Details : ")
                if len(driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/label')) != 0:
                    self.logger.info("********** Summary Details Was Opened **********")
                else:
                    self.logger.info("********** Summary Details Was Not Opened **********")
                    tmp += 1
                    continue
            elif tmp == 2:
                self.logger.info("********** Systems Details : ")
                driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/ul/li[2]/a/span').click()
                time.sleep(5)
                systems_class = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/ul/li[2]').get_attribute("class")
                if systems_class == "ui-state-default ui-corner-top ui-tabview-selected ui-state-active ng-star-inserted":
                    self.logger.info("********** System Details Was Opened **********")
                else:
                    self.logger.info("********** System Details Was Not Opened **********")
                    tmp += 1
                    continue
            time.sleep(5)
            Name = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[1]/div[2]').text
            IP = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[2]/div[2]').text
            OS = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[3]/div[2]').text
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[4]/div[2]'))
            )
            OSV = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[4]/div[2]').text
            self.logger.info("********** Name: "+Name+" **********")
            self.logger.info("********** IP Address: "+IP+" **********")
            self.logger.info("********** OS: "+OS+" **********")
            self.logger.info("********** OS Version: "+OSV+" **********")
            if tmp == 1:
                if len(driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]')) != 0:
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]'))
                    )
                    TNGVersion1 = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]').text
                    self.logger.info("********** TNG Version From RMM GUI : "+TNGVersion1+" **********")
                    TNGVersion2 = self.tngDetails()
                    if TNGVersion1 == TNGVersion2:
                        self.logger.info("********** Both TNG Versions From RMM GUI And Command Prompt Are Same **********")
                    else:
                        self.logger.info("********** Both TNG Versions From RMM GUI And Command Prompt Are Not Same **********")
            tmp += 1
        driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/a/i').click()

    def verifySyncDetailsTwo(self, driver, totalHosts):
        for h in range(1, totalHosts+1):
            driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h)+']/td[3]/span/a/i').click()
            hostName = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h)+']/td[3]/span/span').text
            self.logger.info("********** Sync Details For Host No. "+str(h)+" : "+hostName+" ,")
            tmp = 1
            while tmp < 3:
                time.sleep(5)
                if tmp == 1:
                    self.logger.info("********** Summary Details : ")
                    if len(driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/label')) != 0:
                        self.logger.info("********** Summary Details Was Opened **********")
                    else:
                        self.logger.info("********** Summary Details Was Not Opened **********")
                        tmp += 1
                        continue
                    time.sleep(5)
                elif tmp == 2:
                    self.logger.info("********** Systems Details : ")
                    driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/ul/li[2]/a/span').click()
                    time.sleep(5)
                    systems_class = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/ul/li[2]').get_attribute("class")
                    if systems_class == "ui-state-default ui-corner-top ui-tabview-selected ui-state-active ng-star-inserted":
                        self.logger.info("********** System Details Was Opened **********")
                    else:
                        self.logger.info("********** System Details Was Not Opened **********")
                        tmp += 1
                        continue
                time.sleep(5)
                Name = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[1]/div[2]').text
                IP = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[2]/div[2]').text
                OS = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[3]/div[2]').text
                WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[4]/div[2]'))
                )
                OSV = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[4]/div[2]').text
                self.logger.info("********** Name: "+Name+" **********")
                self.logger.info("********** IP Address: "+IP+" **********")
                self.logger.info("********** OS: "+OS+" **********")
                self.logger.info("********** OS Version: "+OSV+" **********")
                if tmp == 1:
                    if len(driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]')) != 0:
                        WebDriverWait(driver, 30).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]'))
                        )
                        TNGVersion1 = driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]').text
                        self.logger.info("********** TNG Version From RMM GUI : "+TNGVersion1+" **********")
                        TNGVersion2 = self.tngDetails()
                        if TNGVersion1 == TNGVersion2:
                            self.logger.info("********** Both TNG Versions From RMM GUI And Command Prompt Are Same **********")
                        else:
                            self.logger.info("********** Both TNG Versions From RMM GUI And Command Prompt Are Not Same **********")
                tmp += 1
            driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h)+']/td[3]/span/a/i').click()

    def tngDetails(self):
        vm_ip = "172.29.31.111"
        vm_username = "root"
        vm_password = "rackware"

        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(vm_ip,
                    username=vm_username,
                    password=vm_password,
                    look_for_keys=False)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("rpm -qa | grep rwfs")
        output = ssh_stdout.readlines()
        TNGVersion2 = ""
        tmp = str(output)
        for i in range(12, 21):
            TNGVersion2 += tmp[i]
        self.logger.info("********** TNG Version From SSH : " + TNGVersion2 + " **********")
        return TNGVersion2

    def checkWaveStatus(self, driver, waveName):
        co = CommonObjects(driver)
        val = co.findWave(waveName)
        if val == 2:
            return
        status = 'None'
        if val == 1:
            status = driver.find_element(By.XPATH, '//*[@id="waves_'+waveName+'_wave_state"]/span').text
        if val == 0:
            if len(driver.find_elements(By.XPATH, self.txt_waveName_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Was Already Open **********")
                status = driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/div[1]/div[1]/div[2]').text
        self.logger.info("********** The Wave Status For The Wave : " + waveName + ", Is " + status + " **********")

    def totalSuccessfulSyncs(self, driver, waveName):
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
        totalHosts = len(driver.find_elements(By.ID, self.txt_totalHosts_id))
        for hostNo in range(1, totalHosts + 1):
            if totalHosts == 1:
                elem = len(driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/span'))
            else:
                elem = len(driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
            if elem == 0:
                successCount += 1
        self.logger.info("********** The Wave : " + waveName + ", Has " + str(totalHosts) + " Hosts Out Of Which " + str(successCount) + " Are Successful **********")

    def checkHosts(self, driver, waveName, hostNames):
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
        totalHosts = len(driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
        res = tuple(map(str, hostNames.split(', ')))
        for hostName in res:
            for hostNo in range(1, totalHosts + 1):
                if totalHosts == 1:
                    tmp = driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
                else:
                    tmp = driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[3]/span/span').text
                if hostName == tmp:
                    self.logger.info("********** The Host "+hostName+" Is Present In The Wave : "+waveName+" **********")
                    break
                if hostNo == totalHosts:
                    self.logger.info("********** The Host " + hostName + " Is Not Present In The Wave : " + waveName + " **********")
