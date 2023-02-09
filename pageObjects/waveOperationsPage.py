import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaveOperations:
    btn_start_id = "wave_policy_wave_policy_wave_detail_start_replications"
    btn_startConfirm_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[3]/div/div/div[3]/div/button[2]"
    btn_restart_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_restart_replications']/span/i"
    btn_stop_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_stop_replications']/span/i"
    btn_pause_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_pause_replications']/span/i"
    btn_add_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_add_machine']/span/i"
    btn_failOver_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_drPolicyFailover']/span/i"
    btn_fallBack_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_drPolicyFallback']/span/i"
    btn_bulkEdit_xpath = "//*[@id='content']/article/div/div[2]/p-table/div/div[1]/div[1]/button[8]/span/i"

    btn_delete_xpath = "//*[@id='content']/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[8]/span/div/i[4]"
    txt_drPolicy_xpath = "//*[@id='content']/article/div/div[2]/div[2]/div[3]/div[2]/div"
    drp_drPolicy_xpath = "//*[@id='wave_detail_wave_policy_dr_policy']/div/label"
    drp_parallelPolicy_id = "wave_policy_wave_policy_wave_detail_parallelSyncCount"
    chBox_startNow_id = "wave_detail_wave_policy_start_now"
    btn_assignPolicy_id = "wave_detail_wave_policy_assign_policy_btn"
    btn_removePolicy_id = "wave_detail_wave_policy_remove_policy_btn"

    def __init__(self, driver):
        self.driver = driver

    def startWave(self, waveNames):
        for i in waveNames:
            self.driver.find_element(By.XPATH, '//*[@id="waves_'+i+'_wave_name"]').click()
            start = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.ID, self.btn_start_id))
            )
            start.click()
            confirm = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.btn_startConfirm_xpath))
            )
            confirm.click()
            time.sleep(3)
            self.driver.find_element(By.LINK_TEXT, "Waves").click()
            time.sleep(5)

    def restartHost(self, val):
        self.driver.find_element(By.CSS_SELECTOR, "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[" + str(val) + "]/td[1]/p-tablecheckbox/div/div[2]").click()
        self.driver.find_element(By.XPATH, self.btn_restart_xpath).click()

    def stopHost(self, val):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[" + str(val) + "]/td[1]/p-tablecheckbox/div/div[2]").click()
        self.driver.find_element(By.XPATH, self.btn_stop_xpath).click()

    def pauseHost(self, val):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[" + str(val) + "]/td[1]/p-tablecheckbox/div/div[2]").click()
        self.driver.find_element(By.XPATH, self.btn_pause_xpath).click()

    def failoverHost(self, val):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[" + str(val) + "]/td[1]/p-tablecheckbox/div/div[2]").click()
        self.driver.find_element(By.XPATH, self.btn_failOver_xpath).click()

    def fallbackHost(self, val):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[" + str(val) + "]/td[1]/p-tablecheckbox/div/div[2]").click()
        self.driver.find_element(By.XPATH, self.btn_fallBack_xpath).click()

    def bulkEditHosts(self, val):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[" + str(val) + "]/td[1]/p-tablecheckbox/div/div[2]").click()
        self.driver.find_element(By.XPATH, self.btn_bulkEdit_xpath).click()

    def deleteHost(self, val):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[" + str(val) + "]/td[1]/p-tablecheckbox/div/div[2]").click()
        self.driver.find_element(By.XPATH, self.btn_delete_xpath).click()

    def setParallelCount(self, waveName, val):
        self.driver.find_element(By.XPATH, '//*[@id="waves_' + waveName + '_wave_name"]').click()
        time.sleep(5)
        pc = Select(self.driver.find_element(By.ID, self.drp_parallelPolicy_id))
        pc.select_by_visible_text(val)
        time.sleep(5)

    def assignPolicy(self, waveName, policyNumber, val):
        self.driver.find_element(By.XPATH, '//*[@id="waves_' + waveName + '_wave_name"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_drPolicy_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.drp_drPolicy_xpath).click()
        self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li['+str(policyNumber)+']').click()
        if val:
            self.driver.find_element(By.ID, self.chBox_startNow_id).click()
        self.driver.find_element(By.ID, self.btn_assignPolicy_id).click()
        time.sleep(5)

    def changePolicy(self, waveName, policyNumber, val):
        self.driver.find_element(By.LINK_TEXT, "DR").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="waves_' + waveName + '_wave_name"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="wave_policy_wave_policy_wave_detail_drPolicy"]/span').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.drp_drPolicy_xpath).click()
        self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li[' + str(policyNumber) + ']').click()
        if policyNumber == 1:
            self.driver.find_element(By.ID, self.btn_removePolicy_id).click()
        else:
            if val:
                self.driver.find_element(By.ID, self.chBox_startNow_id).click()
            self.driver.find_element(By.ID, self.btn_assignPolicy_id).click()
        time.sleep(5)
