import time
import paramiko

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen


class WaveDetails:

    txt_systemsDetails_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[2]/td/item-details/div/div/p-tabview/div/ul/li[2]/a/span"
    txt_waveStatus_xpath = '//*[@id="content"]/article/div/div[2]/div[1]/div[1]/div[2]'

    # Validations
    val_sourceData_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[2]/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/img'
    val_systemData_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[2]/td/item-details/div/div/p-tabview/div/div/p-tabpanel[2]/div/div[1]/div/div[5]/div[2]/p-progressbar/div/div[2]'

    # pop-up banners
    var_waveDetails_xpath = '//*[@id="rmm_lite_header"]/div/div[1]/div[2]'

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def openWave(self, waveName):
        time.sleep(5)
        flag = 0
        if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
            if (len(self.driver.find_elements(By.LINK_TEXT, "Summary"))) == 0:
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

    def verifySyncDetails(self, waveName):
        time.sleep(5)
        val = self.openWave(waveName)
        if val == 2:
            return
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
            for h in range(1, totalHosts+1):
                time.sleep(5)
                self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h)+']/td[3]/span/a/i').click()
                hostName = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h)+']/td[3]/span/span').text
                self.logger.info("********** Sync Details For Host "+hostName+" ,")
                tmp = 1
                while tmp < 3:
                    if tmp == 1:
                        self.logger.info("********** Summary Details : ")
                        if len(self.driver.find_elements(By.XPATH, self.val_sourceData_xpath)) != 0:
                            self.logger.info("********** Summary Details Was Opened **********")
                        else:
                            self.logger.info("********** Summary Details Was Not Opened **********")
                            tmp += 1
                            continue
                        time.sleep(5)
                    elif tmp == 2:
                        self.logger.info("********** Systems Details : ")
                        self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(h + 1) + ']/td/item-details/div/div/p-tabview/div/ul/li[2]/a/span').click()
                        time.sleep(5)
                        if len(self.driver.find_elements(By.XPATH, self.val_systemData_xpath)) != 0:
                            self.logger.info("********** System Details Was Opened **********")
                        else:
                            self.logger.info("********** System Details Was Not Opened **********")
                            tmp += 1
                            continue
                    time.sleep(5)
                    Name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[1]/div[2]').text
                    IP = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[2]/div[2]').text
                    OS = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[3]/div[2]').text
                    WebDriverWait(self.driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[4]/div[2]'))
                    )
                    OSV = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel['+str(tmp)+']/div/div[1]/div/div[4]/div[2]').text
                    self.logger.info("********** Name : "+Name+" **********")
                    self.logger.info("********** IP Address : "+IP+" **********")
                    self.logger.info("********** OS : "+OS+" **********")
                    self.logger.info("********** OS Version : "+OSV+" **********")
                    if tmp == 1:
                        if len(self.driver.find_elements(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]')) != 0:
                            WebDriverWait(self.driver, 30).until(
                                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]'))
                            )
                            TNGVersion1 = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h+1)+']/td/item-details/div/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[2]/div[3]/div[2]').text
                            self.logger.info("********** TNG Version From RMM GUI : "+TNGVersion1+" **********")
                            TNGVersion2 = self.tngDetails()
                            if TNGVersion1 == TNGVersion2:
                                self.logger.info("********** Both TNG Versions From RMM GUI And Command Prompt Are Same **********")
                            else:
                                self.logger.info("********** Both TNG Versions From RMM GUI And Command Prompt Are Not Same **********")
                    tmp += 1
                self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(h)+']/td[3]/span/a/i').click()
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        time.sleep(5)
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def sourceLogin(self, userName, password):
        time.sleep(5)
        self.driver.find_element(By.ID, "username").send_keys(userName)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(5)
        self.driver.find_element(By.ID, "submit").click()

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

    def checkWaveStatus(self, waveName):
        val = self.openWave(waveName)
        if val == 2:
            return
        time.sleep(5)
        status = self.driver.find_element(By.ID, '//*[@id="waves_'+waveName+'_wave_state"]/span').text
        self.logger.info("********** The Wave Status For The Wave : " + waveName + ", Is " + status + " **********")

    def totalSuccessfulSyncs(self, waveName):
        val = self.openWave(waveName)
        if val == 2:
            return
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            successCount = 0
            totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
            for hostNo in range(1, totalHosts + 1):
                if totalHosts == 1:
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/span'))
                else:
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                if elem == 0:
                    successCount += 1
            self.logger.info("********** The Successful Host Sync Count For The Wave : " + waveName + ", Is " + str(successCount) + " **********")
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def checkHosts(self, waveName, hostNames):
        val = self.openWave(waveName)
        if val == 2:
            return
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
            res = tuple(map(str, hostNames.split(', ')))
            for hostName in res:
                for hostNo in range(1, totalHosts + 1):
                    if totalHosts == 1:
                        tmp = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
                    else:
                        tmp = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[3]/span/span').text
                    if hostName == tmp:
                        self.logger.info("********** The Host "+hostName+" Is Present In The Wave : "+waveName+" **********")
                        break
                    elif hostNo == totalHosts:
                        self.logger.info("********** The Host " + hostName + " Is Not Present In The Wave : " + waveName + " **********")
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if val == 1:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()
