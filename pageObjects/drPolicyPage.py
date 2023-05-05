import time
import openpyxl

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.customLogger import LogGen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DRPolicy:
    btn_addNew_xpath = "//*[@id='policies_dr_policy_create_policy_btn']/span/i"

    txt_name_id = "policyName"
    rd_schedule_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[1]/div/div/input"
    rd_frequency_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[2]/div/div/input"
    rd_once_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[3]/div/div/input"
    rd_continuous_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[4]/div/div/input"
    txt_start_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[3]/div/p-calendar/span/input"
    txt_email_xpath = "//*[@id='email']"
    btn_add_xpath = "//*[@id='policies_create_dr_policy_sbf_addEmail_btn']/i"
    chBox_failNote_xpath = "//*[@id='notifyfailonly']"
    chBox_completeNote_xpath = "//*[@id='notifyonwavecomplete']"
    btn_create_id = "policies_create_dr_policy_sbf_create_btn"
    btn_clear_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[3]/div/p-calendar/span/div/div[3]/div/div[2]/button/span"
    btn_resume_xpath = "//*[@id='policies_dr_policy_resume_dr_policy']/div/div/div/form/div/div[3]/div/button[2]"
    txt_policyName_id = "policies_dr_policy_policyname"

    # By Schedule
    drp_dw_xpath = "//*[@id='select_daily_weekly']"
    drp_hr_xpath = "//*[@id='policies_create_dr_policy_sbs_select_hour']"
    drp_min_xpath = "//*[@id='policies_create_dr_policy_sbs_select_minute']"
    drp_wkDay_xpath = "//*[@id='select_week']"

    # By Frequency
    drp_durationMin_id = "policies_create_dr_policy_sbf_select_minute"
    drp_durationHr_id = "policies_create_dr_policy_sbf_select_hour"
    drp_minHr_xpath = "//*[@id='select_hours_minutes']"
    drp_fromHr_id = "policies_create_dr_policy_sbf_exclude_from_hr"
    drp_fromMin_id = "policies_create_dr_policy_sbf_exclude_from_min"
    drp_toHr_id = "policies_create_dr_policy_sbf_exclude_to_hr"
    drp_toMin_id = "policies_create_dr_policy_sbf_exclude_to_min"

    # Once
    btn_startDate_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[3]/div/p-calendar/span/button/span[1]"

    # Add DR Policy To Wave
    txt_drPolicy_xpath = "//*[@id='content']/article/div/div[2]/div[2]/div[3]/div[2]/div"
    drp_selectDrPolicy_xpath = "//*[@id='wave_detail_wave_policy_dr_policy']/div/div[3]/span"
    ch_startPolicyNow_id = "wave_detail_wave_policy_start_now"
    btn_assignPolicy_id = "wave_detail_wave_policy_assign_policy_btn"
    btn_start_id = "wave_policy_wave_policy_wave_detail_start_replications"
    btn_pause_id = "wave_policy_wave_policy_wave_detail_pause_replications"
    txt_assPolicyName_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_drPolicy"]/span'
    txt_noPolicy_xpath = '//*[@id="content"]/article/div/div[2]/div[2]/div[3]/div[2]/div'
    btn_cancel_id = "wave_detail_wave_policy_close_btn"

    # Failover
    btn_failOver_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_drPolicyFailover']/span/i"
    btn_failOver_id = "wave_policy_wave_policy_wave_detail_drPolicyFailover"
    ch_testMode_id = "wave_detail_failover_testmode"
    btn_failoverYes_id = "wave_detail_failover_yes_btn"
    btn_endDRFailoverOK_xpath = "//*[@id='policies_dr_policy_stop_failover_test']/div/div/div/div/div[3]/div/button[2]"
    txt_policyName_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_drPolicy']/span"

    # Fallback
    btn_fallBack_id = "wave_policy_wave_policy_wave_detail_drPolicyFallback"
    btn_fallBackYes_id = "wave_detail_dr_fallback_yes_btn"

    # Validations
    var_waveDetails_xpath = '//*[@id="rmm_lite_header"]/div/div[1]/div[2]'

    # Pop-up Banners
    pop_failOver_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_failover"]/div/div/div/div[1]/h4'
    pop_createDrPolicy_xpath = '//*[@id="policies_dr_policy_create_dr_policy"]/div/div/div/form/div[1]/h4'
    pop_policyAssignment_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_wave_policy_info"]/div[1]/div/div/div[1]/h4'
    pop_resumePolicy_xpath = '//*[@id="policies_dr_policy_resume_dr_policy"]/div/div/div/form/div/div[1]/h4'
    pop_successful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification/div'

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def findWave(self, waveName):
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
                if len(self.driver.find_elements(By.LINK_TEXT, waveName)) == 0:
                    flag += 1
                    self.logger.info("********** Wave : " + waveName + " Is Not Present **********")
        return flag

    def createDRPolicy(self, path):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        rows = sheet.max_row

        time.sleep(5)
        if(len(self.driver.find_elements(By.LINK_TEXT, "Policies"))) == 0:
            self.driver.find_element(By.LINK_TEXT, "DR").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Policies").click()
        for r in range(2, rows+1):
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.btn_addNew_xpath).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.pop_createDrPolicy_xpath)) != 0:
                self.logger.info("********** Create New DR Policy Pop-up Banner Is Opened **********")
                name = sheet.cell(row=r, column=1).value
                startTime = sheet.cell(row=r, column=2).value
                email = sheet.cell(row=r, column=3).value
                note1 = sheet.cell(row=r, column=4).value
                note2 = sheet.cell(row=r, column=5).value
                periodicity = sheet.cell(row=r, column=6).value

                self.driver.find_element(By.ID, self.txt_name_id).send_keys(name)

                if periodicity == "By Schedule":
                    text = sheet.cell(row=r, column=7).value
                    hrs = sheet.cell(row=r, column=8).value
                    mins = sheet.cell(row=r, column=9).value
                    day = sheet.cell(row=r, column=10).value

                    self.driver.find_element(By.XPATH, self.rd_schedule_xpath).click()
                    if self.driver.find_element(By.XPATH, self.rd_schedule_xpath).is_selected():
                        self.logger.info("********** Selected Periodicity Type: By Schedule **********")
                    else:
                        self.logger.info("********** Failed To Select Periodicity Type: By Schedule **********")
                        self.logger.info("********** Failed To Create A DR Policy "+name+" **********")
                        continue
                    dailyWeekly = Select(self.driver.find_element(By.XPATH, self.drp_dw_xpath))
                    hour = Select(self.driver.find_element(By.XPATH, self.drp_hr_xpath))
                    minute = Select(self.driver.find_element(By.XPATH, self.drp_min_xpath))

                    dailyWeekly.select_by_visible_text(text)
                    if text == "Weekly":
                        weekDay = Select(self.driver.find_element(By.XPATH, self.drp_wkDay_xpath))
                        weekDay.select_by_visible_text(day)
                    hour.select_by_index(hrs)
                    minute.select_by_index(mins)

                elif periodicity == "By Frequency":
                    mh = sheet.cell(row=r, column=11).value
                    due = sheet.cell(row=r, column=12).value
                    fhr = sheet.cell(row=r, column=13).value
                    fmn = sheet.cell(row=r, column=14).value
                    thr = sheet.cell(row=r, column=15).value
                    tmn = sheet.cell(row=r, column=16).value

                    self.driver.find_element(By.XPATH, self.rd_frequency_xpath).click()
                    if self.driver.find_element(By.XPATH, self.rd_schedule_xpath).is_selected():
                        self.logger.info("********** Selected Periodicity Type: By Frequency **********")
                    else:
                        self.logger.info("********** Failed To Select Periodicity Type: By Frequency **********")
                        self.logger.info("********** Failed To Create A DR Policy " + name + " **********")
                        continue
                    minHr = Select(self.driver.find_element(By.XPATH, self.drp_minHr_xpath))
                    minHr.select_by_visible_text(mh)
                    time.sleep(5)
                    if mh == "Minutes":
                        duration = Select(self.driver.find_element(By.ID, self.drp_durationMin_id))
                    else:
                        duration = Select(self.driver.find_element(By.ID, self.drp_durationHr_id))
                    if mh == "Hours":
                        duration.select_by_index(due-1)
                        time.sleep(5)
                    elif mh == "Minutes" and due == 5:
                        duration.select_by_index(0)
                    elif mh == "Minutes" and due > 5:
                        duration.select_by_visible_text(str(due))
                    if fhr != "NA":
                        fromHr = Select(self.driver.find_element(By.ID, self.drp_fromHr_id))
                        fromHr.select_by_index(fhr+1)
                    if fmn != "NA":
                        fromMin = Select(self.driver.find_element(By.ID, self.drp_fromMin_id))
                        fromMin.select_by_index(fmn+1)
                    if thr != "NA":
                        toHr = Select(self.driver.find_element(By.ID, self.drp_toHr_id))
                        toHr.select_by_index(thr+1)
                    if tmn != "NA":
                        toMin = Select(self.driver.find_element(By.ID, self.drp_toMin_id))
                        toMin.select_by_index(tmn+1)

                elif periodicity == "Once":
                    self.driver.find_element(By.XPATH, self.rd_once_xpath).click()
                    if self.driver.find_element(By.XPATH, self.rd_schedule_xpath).is_selected():
                        self.logger.info("********** Selected Periodicity Type: Once **********")
                    else:
                        self.logger.info("********** Failed To Select Periodicity Type: Once **********")
                        self.logger.info("********** Failed To Create A DR Policy " + name + " **********")
                        continue
                    self.driver.find_element(By.XPATH, self.txt_start_xpath).click()
                    self.driver.find_element(By.XPATH, self.btn_clear_xpath).click()
                    self.driver.find_element(By.XPATH, self.txt_start_xpath).send_keys(startTime)
                    time.sleep(5)
                    self.driver.find_element(By.XPATH, self.btn_startDate_xpath).click()

                elif periodicity == "Continuous":
                    self.driver.find_element(By.XPATH, self.rd_continuous_xpath).click()
                    if self.driver.find_element(By.XPATH, self.rd_schedule_xpath).is_selected():
                        self.logger.info("********** Selected Periodicity Type: Continuous **********")
                    else:
                        self.logger.info("********** Failed To Select Periodicity Type: Continuous **********")
                        self.logger.info("********** Failed To Create A DR Policy " + name + " **********")
                        continue

                self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)
                self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

                if note1:
                    self.driver.find_element(By.XPATH, self.chBox_failNote_xpath).click()
                    if self.driver.find_element(By.XPATH, self.chBox_failNote_xpath).is_selected():
                        self.logger.info("********** Email Notification For Fail Cases Only Was Selected **********")
                    else:
                        self.logger.info("********** Failed To Select Email Notification For Fail Cases Only **********")
                if note2:
                    self.driver.find_element(By.XPATH, self.chBox_completeNote_xpath).click()
                    if self.driver.find_element(By.XPATH, self.chBox_completeNote_xpath).is_selected():
                        self.logger.info("********** Email Notification When Complete Was Selected **********")
                    else:
                        self.logger.info("********** Failed To Select Email Notification When Complete **********")
                time.sleep(5)
                self.driver.find_element(By.ID, self.btn_create_id).click()
                time.sleep(5)
                totalDrPolicies = len(self.driver.find_elements(By.ID, self.txt_policyName_id))
                count = 1
                for i in range(1, totalDrPolicies + 1):
                    tmp = self.driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr[' + str(i) + ']/td[1]/span').text
                    if tmp == name:
                        break
                    count += 1
                if count == totalDrPolicies+1:
                    self.logger.info("********** Failed To Create no. " + str(r - 1) + " DR Policy with name " + name + " **********")
                else:
                    self.logger.info("********** Created no. " + str(r - 1) + " DR Policy with name " + name + " **********")
            else:
                self.logger.info("********** Create New DR Policy Pop-up Banner Is Not Opened **********")
        # time.sleep(5)
        # self.driver.find_element(By.LINK_TEXT, "Replication").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def addDRPolicyToWave(self, path):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        rows = sheet.max_row

        for r in range(2, rows+1):
            waveName = sheet.cell(row=r, column=5).value
            drPolicyName = sheet.cell(row=r, column=9).value
            startNow = sheet.cell(row=r, column=10).value
            val = self.findWave(waveName)
            if val == 2:
                return
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
                if len(self.driver.find_elements(By.XPATH, self.txt_assPolicyName_xpath)) == 0:
                    self.logger.info("********** Currently The Wave : " + waveName + ", Don't Have Any Policy **********")
                else:
                    currentPolicy = self.driver.find_element(By.XPATH, self.txt_assPolicyName_xpath).text
                    self.logger.info("********** Currently The Wave : " + waveName + ", Has Policy : " + currentPolicy + " **********")
                self.driver.find_element(By.XPATH, self.txt_drPolicy_xpath).click()
                time.sleep(5)
                if len(self.driver.find_elements(By.XPATH, self.pop_policyAssignment_xpath)) != 0:
                    self.logger.info("********** Policy Assignment Pop-up Banner Is Opened For Wave, " + str(waveName) + " **********")

                    self.driver.find_element(By.XPATH, self.drp_selectDrPolicy_xpath).click()
                    time.sleep(5)
                    # self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li['+str(policyNumber)+']/span').click()
                    if len(self.driver.find_elements(By.CSS_SELECTOR, "li[aria-label="+drPolicyName+"]")) == 0:
                        self.logger.info("********** There Was No Such Policy With Name, " + str(drPolicyName) + " **********")
                        self.driver.find_element(By.ID, self.btn_cancel_id).click()
                    else:
                        self.driver.find_element(By.CSS_SELECTOR, "li[aria-label="+drPolicyName+"]").click()
                        time.sleep(5)
                        if startNow:
                            self.driver.find_element(By.ID, self.ch_startPolicyNow_id).click()
                        time.sleep(3)
                        self.driver.find_element(By.ID, self.btn_assignPolicy_id).click()
                        time.sleep(5)
                        note = self.driver.find_element(By.XPATH, self.pop_successful_xpath).text
                        self.logger.info("********** Assign DR Policy " + drPolicyName + " To Wave " + waveName + ", Status : ")
                        self.logger.info(note + "\n")
                        currentPolicy = self.driver.find_element(By.XPATH, self.txt_assPolicyName_xpath).text
                        if drPolicyName == currentPolicy:
                            self.logger.info("********** Policy : " + drPolicyName + ", Added To The Wave : " + waveName + " **********")
                            time.sleep(60)
                            self.checkDrPolicyState(drPolicyName)
                        else:
                            self.logger.info("********** Failed To Add Policy : " + drPolicyName + ", To The Wave : " + waveName + ", Because The Wave Has " + currentPolicy + " Policy Assign **********")
                else:
                    self.logger.info("********** Policy Assignment Pop-up Banner Is Not Opened For Wave, " + str(waveName) + " **********")
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if len(self.driver.find_elements(By.LINK_TEXT, "Policies")) != 0:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def checkDrPolicyState(self, policyName):
        if len(self.driver.find_elements(By.LINK_TEXT, "Policies")) == 0:
            self.driver.find_element(By.LINK_TEXT, "DR").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Policies").click()
        time.sleep(5)
        totalDrPolicies = len(self.driver.find_elements(By.ID, self.txt_policyName_id))
        count = 1
        for i in range(1, totalDrPolicies+1):
            tmp = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr['+str(i)+']/td[1]/span').text
            if tmp == policyName:
                break
            count += 1
        if count == totalDrPolicies+1:
            self.logger.info("********** There Is No Such Policy With Name: "+policyName+" **********")
        else:
            waveState = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr['+str(count)+']/td[2]/span/span').text
            self.logger.info("********** Policy : " + policyName + ", Is In " + waveState + " State **********")
        if len(self.driver.find_elements(By.LINK_TEXT, "Policies")) != 0:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def resumePolicyAndVerifySyncs(self, waveName, policyName):
        time.sleep(5)
        if len(self.driver.find_elements(By.LINK_TEXT, "Policies")) == 0:
            self.driver.find_element(By.LINK_TEXT, "DR").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Policies").click()
        time.sleep(5)
        totalDrPolicies = len(self.driver.find_elements(By.ID,  self.txt_policyName_id))
        count = 1
        for i in range(1, totalDrPolicies + 1):
            tmp = self.driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr[' + str(i) + ']/td[1]/span').text
            if tmp == policyName:
                break
            count += 1
        if count == totalDrPolicies+1:
            self.logger.info("********** There Is No Such Policy With Name: " + policyName + " **********")
            return
        self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr['+str(count)+']/td[9]/span/i[1]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_resume_xpath).click()
        time.sleep(5)
        if self.driver.find_element(By.XPATH, self.pop_resumePolicy_xpath).is_displayed():
            self.logger.info("********** Pop-up Banner For Resume Policy Was Opened For Policy: "+policyName+" **********")
            val = self.findWave(waveName)
            if val == 2:
                return
            time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            if len(self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath)) != 0:
                self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
                time.sleep(300)
                self.logger.info("********** Pausing DR Policy **********")
                self.pauseDRPolicy(str(policyName))
                self.logger.info("********** Successfully Paused DR Policy **********")
                if not self.driver.find_element(By.LINK_TEXT, "Policies").is_displayed():
                    self.driver.find_element(By.LINK_TEXT, "Policies").click()
                    time.sleep(5)
                self.driver.find_element(By.LINK_TEXT, "Waves").click()
                time.sleep(5)
                self.driver.find_element(By.LINK_TEXT, waveName).click()
                time.sleep(5)
                WebDriverWait(self.driver, 18000).until(
                    EC.element_to_be_clickable((By.ID, self.btn_start_id))
                )
                totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
                for hostNo in range(1, totalHosts+1):
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[6]/span/span/span'))
                    hostName = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNo)+']/td[3]/span/span').text
                    if elem == 0:
                        self.logger.info("********** For Host : "+hostName+", Sync Successful **********")
                    else:
                        self.logger.info("********** For Host : "+hostName+", Sync Failed **********")
                    time.sleep(5)
            else:
                self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        else:
            self.logger.info("********** Pop-up Banner For Resume Policy Was Not Opened For Policy: "+policyName+" **********")
        if self.driver.find_element(By.LINK_TEXT, "Policies").is_displayed():
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()
        time.sleep(5)

    def failoverHost(self, waveName, testMode):
        val = self.findWave(waveName)
        if val == 2:
            return
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        if self.driver.find_elements(By.XPATH, self.var_waveDetails_xpath).is_displayed():
            self.logger.info("********** Wave : " + waveName + " Opened Successfully **********")
            time.sleep(5)
            self.driver.find_element(By.ID, self.btn_failOver_id).click()
            time.sleep(5)
            if self.driver.find_element(By.XPATH, self.pop_failOver_xpath).is_displayed():
                self.logger.info("********** Pop-up Banner Of Failover Was Opened **********")
                if testMode:
                    self.driver.find_element(By.ID, self.ch_testMode_id).click()
                self.driver.find_element(By.ID, self.btn_failoverYes_id).click()
                time.sleep(10)
                WebDriverWait(self.driver, 18000).until(
                    EC.text_to_be_present_in_element((By.XPATH, "//*[@id='content']/article/div/div[2]/div[1]/div[1]/div[2]"), "Failed Over")
                )
                time.sleep(5)
                totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
                for hostNo in range(1, totalHosts + 1):
                    elem = len(self.driver.find_elements(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[6]/span/span/span'))
                    hostName = self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[' + str(hostNo) + ']/td[3]/span/span').text
                    if elem == 0:
                        self.logger.info("********** For Host : " + hostName + ", Sync Successful **********")
                    else:
                        self.logger.info("********** For Host : " + hostName + ", Sync Failed **********")
                    time.sleep(5)
                self.logger.info("********** Pausing DR Policy **********")
                tmp = self.driver.find_element(By.XPATH, self.txt_policyName_xpath).text
                res = tuple(map(str, tmp.split(' (')))
                self.pauseDRPolicy(str(res[0]))
            else:
                self.logger.info("********** Pop-up Banner Of Failover Was Not Opened **********")
        else:
            self.logger.info("********** Failed To Open Wave : " + waveName + " **********")
        if self.driver.find_element(By.LINK_TEXT, "Policies").is_displayed:
            self.driver.find_element(By.LINK_TEXT, "Replication").click()
            time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def fallbackHost(self, waveName):
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.btn_fallBack_id).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.btn_fallBackYes_id).click()
        time.sleep(5)
        WebDriverWait(self.driver, 18000).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_failOver_xpath))
        )
        self.driver.find_element(By.LINK_TEXT, "Waves")

    def pauseDRPolicy(self, policyNames):
        res = tuple(map(str, policyNames.split(', ')))
        for policyName in res:
            time.sleep(5)
            if len(self.driver.find_elements(By.LINK_TEXT, "Policies")) == 0:
                self.driver.find_element(By.LINK_TEXT, "DR").click()
                time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, "Policies").click()
            time.sleep(5)
            totalDrPolicies = len(self.driver.find_elements(By.ID,  self.txt_policyName_id))
            count = 1
            for i in range(1, totalDrPolicies + 1):
                tmp = self.driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr[' + str(i) + ']/td[1]/span').text
                if tmp == policyName:
                    break
                count += 1
            if count == totalDrPolicies+1:
                self.logger.info("********** There Is No Such Policy With Name: " + policyName + " **********")
                return
            waveState = self.driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr[' + str(count) + ']/td[2]/span/span').text
            self.logger.info("********** Policy : " + policyName + ", Is In " + waveState + " State **********")
            self.logger.info("********** Pausing The DR Policy **********")
            self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr['+str(count)+']/td[9]/span/i[1]').click()
            time.sleep(5)
            # if len(self.driver.find_elements(By.XPATH, self.btn_endDRFailoverOK_xpath)) != 0:
            #     time.sleep(5)
            #     self.driver.find_element(By.XPATH, self.btn_endDRFailoverOK_xpath).click()
            # time.sleep(10)
            WebDriverWait(self.driver, 18000).until(
                EC.text_to_be_present_in_element((By.XPATH, '/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr['+str(count)+']/td[2]/span/span'), "Paused")
            )
            time.sleep(5)
            waveState = self.driver.find_element(By.XPATH,'/html/body/app-root/app-main-layout/div/dr-policy/div/div/article/div/div[3]/p-table/div/div[2]/table/tbody/tr[' + str(count) + ']/td[2]/span/span').text
            self.logger.info("********** Policy : " + policyName + ", Is In " + waveState + " State **********")
            if waveState == "Paused":
                self.logger.info("********** Successfully Paused The Policy : " + policyName + " **********")
