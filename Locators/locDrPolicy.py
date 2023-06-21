txt_policies_xpath = '//*[@id="nav-panel"]/nav/ul/li[2]/ul/li[2]'
txt_dr_xpath = '//*[@id="nav-panel"]/nav/ul/li[2]'
txt_waveState_xpath = '//*[@id="content"]/article/div/div[2]/div[1]/div[1]/div[2]'
txt_waveName_xpath = '//*[@id="content"]/article/div/div[1]/div/h3/strong'
txt_start_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[3]/div/p-calendar/span/input"
txt_email_xpath = "//*[@id='email']"
txt_policyName_id = "policies_dr_policy_policyname"
txt_name_id = "policyName"


btn_addNew_xpath = "//*[@id='policies_dr_policy_create_policy_btn']/span/i"
btn_add_xpath = "//*[@id='policies_create_dr_policy_sbf_addEmail_btn']/i"
btn_clear_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[3]/div/p-calendar/span/div/div[3]/div/div[2]/button/span"
btn_resume_xpath = "//*[@id='policies_dr_policy_resume_dr_policy']/div/div/div/form/div/div[3]/div/button[2]"
btn_cancel_xpath = "policies_create_dr_policy_sbf_cancel_btn"
btn_create_id = "policies_create_dr_policy_sbf_create_btn"

rd_schedule_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[1]/div/div/input"
rd_frequency_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[2]/div/div/input"
rd_once_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[3]/div/div/input"
rd_continuous_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[2]/div[1]/div[4]/div/div/input"

chBox_failNote_xpath = "//*[@id='notifyfailonly']"
chBox_completeNote_xpath = "//*[@id='notifyonwavecomplete']"


# By Schedule
drp_dw_xpath = "//*[@id='select_daily_weekly']"
drp_hr_xpath = "//*[@id='policies_create_dr_policy_sbs_select_hour']"
drp_min_xpath = "//*[@id='policies_create_dr_policy_sbs_select_minute']"
drp_wkDay_xpath = "//*[@id='select_week']"


# By Frequency
drp_minHr_xpath = "//*[@id='select_hours_minutes']"
drp_durationMin_id = "policies_create_dr_policy_sbf_select_minute"
drp_durationHr_id = "policies_create_dr_policy_sbf_select_hour"
drp_fromHr_id = "policies_create_dr_policy_sbf_exclude_from_hr"
drp_fromMin_id = "policies_create_dr_policy_sbf_exclude_from_min"
drp_toHr_id = "policies_create_dr_policy_sbf_exclude_to_hr"
drp_toMin_id = "policies_create_dr_policy_sbf_exclude_to_min"


# Once
btn_startDate_xpath = "//*[@id='policies_dr_policy_create_dr_policy']/div/div/div/form/div[2]/div[3]/div/p-calendar/span/button/span[1]"


# Add DR Policy To Wave
txt_drPolicy_xpath = "//*[@id='content']/article/div/div[2]/div[2]/div[3]/div[2]/div"
txt_assPolicyName_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_drPolicy"]/span'
txt_noPolicy_xpath = '//*[@id="content"]/article/div/div[2]/div[2]/div[3]/div[2]/div'

btn_assignPolicy_id = "wave_detail_wave_policy_assign_policy_btn"
btn_start_id = "wave_policy_wave_policy_wave_detail_start_replications"
btn_pause_id = "wave_policy_wave_policy_wave_detail_pause_replications"
btn_cancel_id = "wave_detail_wave_policy_cancel_btn"

drp_selectDrPolicy_xpath = "//*[@id='wave_detail_wave_policy_dr_policy']/div/div[3]/span"
ch_startPolicyNow_id = "wave_detail_wave_policy_start_now"


# Failover
txt_failoverCheck_xpath = '//*[@id="content"]/article/div/div[2]/div[2]/div[3]/div[2]/div'
txt_policyName_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_drPolicy']/span"

btn_failOver_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_drPolicyFailover']/span/i"
btn_endDRFailoverOK_xpath = "//*[@id='policies_dr_policy_stop_failover_test']/div/div/div/div/div[3]/div/button[2]"
btn_failOver_id = "wave_policy_wave_policy_wave_detail_drPolicyFailover"
btn_failoverYes_id = "wave_detail_failover_yes_btn"

ch_testMode_id = "wave_detail_failover_testmode"


# Fallback
btn_fallBack_id = "wave_policy_wave_policy_wave_detail_drPolicyFallback"
btn_fallBackYes_id = "wave_detail_dr_fallback_yes_btn"


# Validations
val_waveOpen_xpath = '//*[@id="content"]/article/div/div[1]/div/h3/strong'


# Pop-up Banners
pop_failOver_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_failover"]/div/div/div/div[1]/h4'
pop_createDrPolicy_xpath = '//*[@id="policies_dr_policy_create_dr_policy"]/div/div/div/form/div[1]/h4'
pop_policyAssignment_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_wave_policy_info"]/div[1]/div/div/div[1]/h4'
pop_resumePolicy_xpath = '//*[@id="policies_dr_policy_resume_dr_policy"]/div/div/div/form/div/div[1]/h4'
pop_successful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification/div'

