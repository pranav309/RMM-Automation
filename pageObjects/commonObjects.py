import time

from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen


class CommonObjects:

    txt_waveState_xpath = '//*[@id="content"]/article/div/div[2]/div[1]/div[1]/div[2]'
    txt_waveName_xpath = '//*[@id="content"]/article/div/div[1]/div/h3/strong'
    txt_replication_xpath = '//*[@id="nav-panel"]/nav/ul/li[1]'
    txt_dr_xpath = '//*[@id="nav-panel"]/nav/ul/li[2]'
    txt_rWave_xpath = '//*[@id="nav-panel"]/nav/ul/li[1]/ul/li[2]'
    txt_drWave_xpath = '//*[@id="nav-panel"]/nav/ul/li[2]/ul/li[3]'
    txt_hostSearch_xpath = '//*[@id="content"]/div/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[1]/p-tablecheckbox/div/div[2]'
    txt_waveSearch_xpath = '//*[@id="waves_search_input"]'
    txt_policySearch_xpath = '//*[@id="policies_dr_policy_search_text"]'

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def findWaveCommon(self, waveName, flag):
        self.driver.find_element(By.LINK_TEXT, "Replication").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).send_keys(waveName)
        time.sleep(2)
        if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
            self.driver.find_element(By.LINK_TEXT, "DR").click()
            time.sleep(2)
            self.driver.find_element(By.LINK_TEXT, "Waves").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).click()
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).clear()
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).send_keys(waveName)
            time.sleep(2)
            if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
                flag += 1
                self.logger.info("********** Wave : " + waveName + " Is Not Present **********")
        return flag

    def findWaveCommonOne(self, waveName, flag):
        wave_class = self.driver.find_element(By.XPATH, self.txt_rWave_xpath).get_attribute("class")
        if wave_class != "active":
            self.driver.find_element(By.LINK_TEXT, "Waves").click()
            time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).send_keys(waveName)
        time.sleep(2)
        if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
            self.driver.find_element(By.LINK_TEXT, "DR").click()
            time.sleep(3)
            self.driver.find_element(By.LINK_TEXT, "Waves").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).click()
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).clear()
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).send_keys(waveName)
            time.sleep(2)
            if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
                flag += 1
                self.logger.info("********** Wave : " + waveName + " Is Not Present **********")
        return flag

    def findWaveCommonTwo(self, waveName, flag):
        wave_class = self.driver.find_element(By.XPATH, self.txt_drWave_xpath).get_attribute("class")
        if wave_class == "ng-star-inserted":
            self.driver.find_element(By.LINK_TEXT, "Waves").click()
            time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).send_keys(waveName)
        time.sleep(2)
        if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(3)
            self.driver.find_element(By.LINK_TEXT, "Waves").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).click()
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).clear()
            self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).send_keys(waveName)
            time.sleep(2)
            if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
                flag += 1
                self.logger.info("********** Wave : " + waveName + " Is Not Present **********")
        return flag

    def findWave(self, waveName):
        time.sleep(5)
        flag = 0
        replication_class = self.driver.find_element(By.XPATH, self.txt_replication_xpath).get_attribute("class")
        dr_class = self.driver.find_element(By.XPATH, self.txt_dr_xpath).get_attribute("class")
        wp = len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath))
        if wp != 0:
            wn = self.driver.find_element(By.XPATH, self.txt_waveName_xpath).text
            if wn == waveName:
                return flag
        flag += 1
        if replication_class == "ng-star-inserted open":
            flag = self.findWaveCommonOne(waveName, flag)
        elif dr_class == "ng-star-inserted open":
            flag = self.findWaveCommonTwo(waveName, flag)
        else:
            flag = self.findWaveCommon(waveName, flag)
        return flag

    def findDrWave(self, waveName):
        time.sleep(5)
        flag = 0
        dr_class = self.driver.find_element(By.XPATH, self.txt_dr_xpath).get_attribute("class")
        wp = len(self.driver.find_elements(By.XPATH, self.txt_waveName_xpath))
        if wp != 0:
            wn = self.driver.find_element(By.XPATH, self.txt_waveName_xpath).text
            if wn == waveName:
                return flag
        flag += 1
        if dr_class == "ng-star-inserted":
            self.driver.find_element(By.LINK_TEXT, "DR").click()
            time.sleep(3)
        wave_class = self.driver.find_element(By.XPATH, self.txt_drWave_xpath).get_attribute("class")
        if wave_class == "ng-star-inserted":
            self.driver.find_element(By.LINK_TEXT, "Waves").click()
            time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_waveSearch_xpath).send_keys(waveName)
        time.sleep(2)
        if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
            self.logger.info("********** Wave : " + waveName + " Is Not Present Or Don't Have Any Policy Assigned To It **********")
            flag += 1
        return flag

    def hostSyncState(self):
        totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
        if totalHosts == 1:
            elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[6]/span/span/span'))
            hostName = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[3]/span/span').text
            if elem == 0:
                self.logger.info("********** For Host : " + hostName + ", Sync Successful **********")
            else:
                self.logger.info("********** For Host : " + hostName + ", Sync Failed **********")
        else:
            for hostNo in range(1, totalHosts + 1):
                elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                hostName = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/span').text
                if elem == 0:
                    self.logger.info("********** For Host : " + hostName + ", Sync Successful **********")
                else:
                    self.logger.info("********** For Host : " + hostName + ", Sync Failed **********")
