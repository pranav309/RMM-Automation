import time
import openpyxl

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utilities.customLogger import LogGen


class SyncOptions:
    # Autoprovision
    txt_autoprovision_id = "wave_policy_wave_policy_wave_detail_autoprovision"
    txt_environment_xpath = "//*[@id='clouduser']"
    txt_clusterName_xpath = "//*[@id='wave_detail_cu_edit_vc_clustername']/div/input"
    txt_ESXHost_xpath = "//*[@id='wave_detail_cu_edit_vc_esx_host']/div/input"
    txt_Datastore_xpath = "//*[@id='wave_detail_cu_edit_vc_dc']/div/input"
    btn_applyChanges_id = "wave_detail_cu_edit_apply_changes_btn"

    # Single Edit Set NIC
    btn_NICAdd_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div/div[4]/div[2]/a"
    txt_deviceName_id = "wave_detail_edit_item_nic_device_name"
    txt_type_id = "wave_detail_edit_item_nic_type"
    txt_networkName_id = "wave_detail_edit_item_nic_networkName"
    rd_DHCP_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/edit-item-nic/div/div/div/form/div[2]/div[1]/div[4]/div/div[1]/div/div/input"
    rd_staticIP_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/edit-item-nic/div/div/div/form/div[2]/div[1]/div[4]/div/div[2]/div/div/input"
    txt_CIDR_id = "wave_detail_edit_item_nic_cidr"
    txt_gateway_id = "wave_detail_edit_item_nic_gateway"
    txt_DNS1_id = "wave_detail_edit_item_nic_dns1"
    txt_DNS2_id = "wave_detail_edit_item_nic_dns2"
    btn_save_id = "wave_detail_edit_item_nic_save_btn"

    # Bulk Edit Set NIC
    btn_NICAddBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[4]/div/p-tabview/div/div/p-tabpanel[2]/div/div/div[5]/div[3]/a/i"
    txt_deviceNameBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[1]/span/input"
    txt_typeBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[2]/span/input"
    txt_networkNameBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[3]/span/input"
    rd_DHCPBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[4]/div/div[1]/div/div/input"
    rd_staticIPBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[4]/div/div[2]/div/div/input"
    txt_CIDRBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[2]/div[1]/span/input"
    txt_gatewayBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[2]/div[2]/span/input"
    txt_DNS1BulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[2]/div[3]/span/input"
    txt_DNS2BulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[2]/div[4]/span/input"
    btn_save_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[3]/div/button[2]"

    # Sync Options
    btn_syncOptions_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/ul/li[2]/a/span"
    btn_modify_id = "wave_detail_edit_item_modify_btn"
    rd_tng_id = "wave_detail_edit_item_options_tng"
    rd_verbose_id = "wave_detail_edit_item_options_verbose"
    rd_directFScopy_id = "wave_detail_edit_item_options_allowdirectfscopy"
    rd_FSDeletion_id = "wave_detail_edit_item_options_allowFsDeletion"
    rd_NoTransfer_id = "wave_detail_edit_item_options_no_xfer"
    rd_transferCompress_id = "wave_detail_edit_item_options_xfer_compress"
    rd_noTransferCompress_id = "wave_detail_edit_item_options_no_xfer_compress"
    rd_ignoreMissing_id = "wave_detail_edit_item_options_ignore_missing"
    rd_noInPlace_id = "wave_detail_edit_item_options_noInPlace"
    rd_noReboot_id = "wave_detail_edit_item_options_noReboot"
    rd_includeSAN_id = "wave_detail_edit_item_options_include_san"
    rd_excludeSAN_id = "wave_detail_edit_item_options_exclude_san"
    rd_overrideRMMStorageCheck_id = "wave_detail_edit_item_options_storage_override"
    rd_deleteAllTargetFS_id = "wave_detail_edit_item_options_delete_all_target_fs"
    rd_keepTargetLayout_id = "wave_detail_edit_item_options_keep_target_layout"
    rd_cloudInit_id = "wave_detail_edit_item_options_cloud_init"

    # Bulk Edit Sync Options
    btn_selectAll_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/div[1]/article/div/div[2]/p-table/div/div[2]/table/thead/tr/th[1]/p-tableheadercheckbox/div/div[2]"
    btn_bulkEdit_xpath = "//*[@id='content']/article/div/div[2]/p-table/div/div[1]/div[1]/button[8]/span/i"
    drp_goal_id = "wave_detail_bulk_edit_item_existing_capture_type"
    ch_tngYes_id = "tng_yes"
    ch_tngNo_id = "tng_no"
    ch_verboseYes_id = "verbose_yes"
    ch_verboseNo_id = "verbose_no"
    ch_passwordLessYes_id = "ssh_yes"
    ch_passwordLessNo_id = "ssh_no"
    ch_AllowDirectFScopyYes_id = "allowDirectFscopy_yes"
    ch_AllowDirectFScopyNo_id = "allowDirectFscopy_no"
    ch_AllowFSDeletionYes_id = "allowFsDeletion_yes"
    ch_AllowFSDeletionNo_id = "allowFsDeletion_no"
    ch_NoTransferYes_id = "no_xfer_yes"
    ch_NoTransferNo_id = "no_xfer_no"
    ch_TransferCompressYes_id = "xferCompress_yes"
    ch_TransferCompressNo_id = "xferCompress_no"
    ch_NoTransferCompressYes_id = "no_xfer_compress_yes"
    ch_NoTransferCompressNo_id = "no_xfer_compress_no"
    ch_IgnoreMissingYes_id = "ignoreMissing_yes"
    ch_IgnoreMissingNo_id = "ignoreMissing_no"
    ch_NoInPlaceYes_id = "noInPlace_yes"
    ch_NoInPlaceNo_id = "noInPlace_no"
    ch_NoRebootYes_id = "noReboot_yes"
    ch_NoRebootNo_id = "noReboot_no"
    ch_IncludeSANYes_id = "include_san_yes"
    ch_IncludeSANNo_id = "include_san_no"
    ch_ExcludeSANYes_id = "exclude_san_yes"
    ch_ExcludeSANNo_id = "exclude_san_no"
    ch_OverrideRMMStorageCheckYes_id = "storage_override_yes"
    ch_OverrideRMMStorageCheckNo_id = "storage_override_no"
    ch_DeleteAllTargetFSYes_id = "delete_all_target_fs_yes"
    ch_DeleteAllTargetFSNo_id = "delete_all_target_fs_no"
    ch_KeepTargetLayoutYes_id = "keep_target_layout_yes"
    ch_KeepTargetLayoutNo_id = "keep_target_layout_no"
    ch_CloudInitYes_id = "cloud_init_yes"
    ch_CloudInitNo_id = "cloud_init_no"
    btn_next_xpath = "//*[@id='main']/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[5]/div/button[2]"
    btn_modifyAll_xpath = "//*[@id='main']/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[5]/div/button[2]"
    btn_yes_id = "wave_policy_wave_policy_wave_detail_autoprov_not_conf_yes_btn"

    # DR Policy
    txt_drPolicy_xpath = "//*[@id='content']/article/div/div[2]/div[2]/div[3]/div[2]/div"
    drp_selectDrPolicy_xpath = "//*[@id='wave_detail_wave_policy_dr_policy']/div/div[3]/span"
    ch_startPolicyNow_id = "wave_detail_wave_policy_start_now"
    btn_assignPolicy_id = "wave_detail_wave_policy_assign_policy_btn"

    # OCI Sync Options
    txt_OCIVCNName_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div[1]/div[3]/div/input"
    txt_OCISubnetName_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div[1]/div[4]/div/input"
    txt_OCIAVDomain_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div[1]/div[9]/div/input"

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def setAutoprovision(self, path):
        workBook = openpyxl.load_workbook(path)
        sheet = workBook.active
        rows = sheet.max_row
        time.sleep(5)
        for r in range(3, rows+1):
            waveName = sheet.cell(row=r, column=1).value
            # CUType = sheet.cell(row=r, column=2).value
            environment = sheet.cell(row=r, column=3).value

            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            self.driver.find_element(By.ID, self.txt_autoprovision_id).click()
            time.sleep(5)
            env = Select(self.driver.find_element(By.XPATH, self.txt_environment_xpath))
            env.select_by_visible_text(environment)
            if environment == "VCenter":
                self.setVCenter(sheet, r)
            elif environment == "OCI":
                self.setOCI(sheet, r)

        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def setVCenter(self, sheet, r):
        clusterName = sheet.cell(row=r, column=3).value
        esxHost = sheet.cell(row=r, column=4).value
        datastore = sheet.cell(row=r, column=5).value

        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_clusterName_xpath).send_keys(clusterName)
        self.driver.find_element(By.XPATH, self.txt_ESXHost_xpath).send_keys(esxHost)
        self.driver.find_element(By.XPATH, self.txt_Datastore_xpath).send_keys(datastore)
        time.sleep(5)
        self.driver.find_element(By.ID, self.btn_applyChanges_id).click()
        time.sleep(5)

        totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
        if totalHosts == 1:
            self.setNICEdit(sheet, r)
        else:
            self.setNICBulkEdit(sheet, r)

    def setNICEdit(self, sheet, r):
        deviceName = sheet.cell(row=r, column=6).value
        Type = sheet.cell(row=r, column=7).value
        networkName = sheet.cell(row=r, column=8).value
        ipType = sheet.cell(row=r, column=9).value
        CIDR = sheet.cell(row=r, column=10).value
        gateway = sheet.cell(row=r, column=11).value
        DNS1 = sheet.cell(row=r, column=12).value
        DNS2 = sheet.cell(row=r, column=13).value

        self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[8]/span/div/i[2]').click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "vCenter Options").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_NICAdd_xpath).click()
        time.sleep(5)
        if ipType == "DHCP":
            self.driver.find_element(By.XPATH, self.rd_DHCP_xpath).click()
        elif ipType == "Static IP":
            self.driver.find_element(By.XPATH, self.rd_staticIP_xpath).click()
            self.driver.find_element(By.ID, self.txt_CIDR_id).send_keys(CIDR)
            self.driver.find_element(By.ID, self.txt_gateway_id).send_keys(gateway)
            self.driver.find_element(By.ID, self.txt_DNS1_id).send_keys(DNS1)
            self.driver.find_element(By.ID, self.txt_DNS2_id).send_keys(DNS2)
        self.driver.find_element(By.ID, self.txt_deviceName_id).send_keys(deviceName)
        self.driver.find_element(By.ID, self.txt_type_id).send_keys(Type)
        self.driver.find_element(By.ID, self.txt_networkName_id).send_keys(networkName)
        time.sleep(5)
        self.driver.find_element(By.ID, self.btn_save_id).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.btn_modify_id).click()

    def setNICBulkEdit(self, sheet, r):
        deviceName = sheet.cell(row=r, column=6).value
        Type = sheet.cell(row=r, column=7).value
        networkName = sheet.cell(row=r, column=8).value
        ipType = sheet.cell(row=r, column=9).value
        CIDR = sheet.cell(row=r, column=10).value
        gateway = sheet.cell(row=r, column=11).value
        DNS1 = sheet.cell(row=r, column=12).value
        DNS2 = sheet.cell(row=r, column=13).value

        self.driver.find_element(By.XPATH, self.btn_selectAll_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_bulkEdit_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "vCenter Options").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_NICAddBulkEdit_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_deviceNameBulkEdit_xpath).send_keys(deviceName)
        self.driver.find_element(By.XPATH, self.txt_typeBulkEdit_xpath).send_keys(Type)
        self.driver.find_element(By.XPATH, self.txt_networkNameBulkEdit_xpath).send_keys(networkName)
        if ipType == "DHCP":
            self.driver.find_element(By.XPATH, self.rd_DHCPBulkEdit_xpath).click()
        elif ipType == "Static IP":
            self.driver.find_element(By.XPATH, self.rd_staticIPBulkEdit_xpath).click()
            self.driver.find_element(By.XPATH, self.txt_CIDRBulkEdit_xpath).send_keys(CIDR)
            self.driver.find_element(By.XPATH, self.txt_gatewayBulkEdit_xpath).send_keys(gateway)
            self.driver.find_element(By.XPATH, self.txt_DNS1BulkEdit_xpath).send_keys(DNS1)
            self.driver.find_element(By.XPATH, self.txt_DNS2BulkEdit_xpath).send_keys(DNS2)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_next_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_modifyAll_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.btn_yes_id).click()

    def setOCI(self, waveName, environment, VCNName, SubnetName, AVDomain):
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.txt_autoprovision_id).click()
        time.sleep(5)
        env = Select(self.driver.find_element(By.XPATH, self.txt_environment_xpath))
        time.sleep(5)
        env.select_by_visible_text(environment)
        time.sleep(5)
        self.driver.find_element(By.ID, self.btn_applyChanges_id).click()
        time.sleep(5)
        totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
        if totalHosts == 1:
            self.setOCISync(VCNName, SubnetName, AVDomain)
        else:
            self.setOCIBulkSync(VCNName, SubnetName, AVDomain)

        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def setOCISync(self, VCNName, SubnetName, AVDomain):
        self.driver.find_element(By.XPATH,'//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[8]/span/div/i[2]').click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "OCI Options").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_OCIVCNName_xpath).send_keys(VCNName)
        self.driver.find_element(By.XPATH, self.txt_OCISubnetName_xpath).send_keys(SubnetName)
        self.driver.find_element(By.XPATH, self.txt_OCIAVDomain_xpath).send_keys(AVDomain)
        time.sleep(5)
        self.driver.find_element(By.ID, self.btn_modify_id).click()

    def setOCIBulkSync(self, VCNName, SubnetName, AVDomain):
        self.driver.find_element(By.XPATH, self.btn_selectAll_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_bulkEdit_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "OCI Options").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "oci_vcn_name").send_keys(VCNName)
        self.driver.find_element(By.ID, "oci_subnet_name").send_keys(SubnetName)
        self.driver.find_element(By.ID, "oci_av_domain").send_keys(AVDomain)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_next_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_modifyAll_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.btn_yes_id).click()

    def setSyncOptions(self, path):
        workBook = openpyxl.load_workbook(path)
        sheet = workBook.active
        rows = sheet.max_row
        for r in range(3, rows+1):
            waveName = sheet.cell(row=r, column=1).value
            hostNumber = sheet.cell(row=r, column=2).value

            tng = sheet.cell(row=r, column=3).value
            verbose = sheet.cell(row=r, column=4).value
            directFScopy = sheet.cell(row=r, column=5).value
            FSDeletion = sheet.cell(row=r, column=6).value
            NoTransfer = sheet.cell(row=r, column=7).value
            transferCompress = sheet.cell(row=r, column=8).value
            noTransferCompress = sheet.cell(row=r, column=9).value
            ignoreMissing = sheet.cell(row=r, column=10).value
            noInPlace = sheet.cell(row=r, column=11).value
            noReboot = sheet.cell(row=r, column=12).value
            includeSAN = sheet.cell(row=r, column=13).value
            excludeSAN = sheet.cell(row=r, column=14).value
            overrideRMMStorageCheck = sheet.cell(row=r, column=15).value
            deleteAllTargetFS = sheet.cell(row=r, column=16).value
            keepTargetLayout = sheet.cell(row=r, column=17).value
            cloudInit = sheet.cell(row=r, column=18).value

            time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            totalHosts = len(self.driver.find_elements(By.ID, "wave_policy_wave_policy_wave_detail_elapsed_time_info"))
            if totalHosts == 1:
                self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr/td[8]/span/div/i[2]').click()
            else:
                self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr['+str(hostNumber)+']/td[8]/span/div/i[2]').click()
            time.sleep(5)

            syncOption = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.btn_syncOptions_xpath))
            )
            syncOption.click()
            time.sleep(5)

            if tng:
                self.driver.find_element(By.ID, self.rd_tng_id).click()
                self.logger.info("********** Sync Option 'TNG' is set **********")
            if verbose:
                self.driver.find_element(By.ID, self.rd_verbose_id).click()
                self.logger.info("********** Sync Option 'Verbose' is set **********")
            if directFScopy:
                self.driver.find_element(By.ID, self.rd_directFScopy_id).click()
                self.logger.info("********** Sync Option 'Direct FScopy' is set **********")
            if FSDeletion:
                self.driver.find_element(By.ID, self.rd_FSDeletion_id).click()
                self.logger.info("********** Sync Option 'FS Deletion' is set **********")
            if NoTransfer:
                self.driver.find_element(By.ID, self.rd_NoTransfer_id).click()
                self.logger.info("********** Sync Option 'No Transfer' is set **********")
            if transferCompress:
                self.driver.find_element(By.ID, self.rd_transferCompress_id).click()
                self.logger.info("********** Sync Option 'Transfer Compress' is set **********")
            if noTransferCompress:
                self.driver.find_element(By.ID, self.rd_noTransferCompress_id).click()
                self.logger.info("********** Sync Option 'No Transfer Compress' is set **********")
            if ignoreMissing:
                self.driver.find_element(By.ID, self.rd_ignoreMissing_id).click()
                self.logger.info("********** Sync Option 'Ignore Missing' is set **********")
            if noInPlace:
                self.driver.find_element(By.ID, self.rd_noInPlace_id).click()
                self.logger.info("********** Sync Option 'No In Place' is set **********")
            if noReboot:
                self.driver.find_element(By.ID, self.rd_noReboot_id).click()
                self.logger.info("********** Sync Option 'No Reboot' is set **********")
            if includeSAN:
                self.driver.find_element(By.ID, self.rd_includeSAN_id).click()
                self.logger.info("********** Sync Option 'Include SAN' is set **********")
            if excludeSAN:
                self.driver.find_element(By.ID, self.rd_excludeSAN_id).click()
                self.logger.info("********** Sync Option 'Exclude SAN' is set **********")
            if overrideRMMStorageCheck:
                self.driver.find_element(By.ID, self.rd_overrideRMMStorageCheck_id).click()
                self.logger.info("********** Sync Option 'Override RMM Storage' Check is set **********")
            if deleteAllTargetFS:
                self.driver.find_element(By.ID, self.rd_deleteAllTargetFS_id).click()
                self.logger.info("********** Sync Option 'Delete All Target' FS is set **********")
            if keepTargetLayout:
                self.driver.find_element(By.ID, self.rd_keepTargetLayout_id).click()
                self.logger.info("********** Sync Option 'Keep Target Layout' is set **********")
            if cloudInit:
                self.driver.find_element(By.ID, self.rd_cloudInit_id).click()
                self.logger.info("********** Sync Option 'Cloud Init' is set **********")

            time.sleep(5)
            self.driver.find_element(By.ID, self.btn_modify_id).click()
        time.sleep(5)

    def bulkEditOption(self, path):
        workBook = openpyxl.load_workbook(path)
        sheet = workBook.active
        rows = sheet.max_row
        time.sleep(5)
        for r in range(2, rows+1):
            waveName = sheet.cell(row=r, column=1).value
            # goal = sheet.cell(row=r, column=2).value
            tng = sheet.cell(row=r, column=3).value
            verbose = sheet.cell(row=r, column=4).value
            passwordLess = sheet.cell(row=r, column=5).value
            directFScopy = sheet.cell(row=r, column=6).value
            FSDeletion = sheet.cell(row=r, column=7).value
            NoTransfer = sheet.cell(row=r, column=8).value
            transferCompress = sheet.cell(row=r, column=9).value
            noTransferCompress = sheet.cell(row=r, column=10).value
            ignoreMissing = sheet.cell(row=r, column=11).value
            noInPlace = sheet.cell(row=r, column=12).value
            noReboot = sheet.cell(row=r, column=13).value
            includeSAN = sheet.cell(row=r, column=14).value
            excludeSAN = sheet.cell(row=r, column=15).value
            overrideRMMStorageCheck = sheet.cell(row=r, column=16).value
            deleteAllTargetFS = sheet.cell(row=r, column=17).value
            keepTargetLayout = sheet.cell(row=r, column=18).value
            cloudInit = sheet.cell(row=r, column=19).value

            self.driver.find_element(By.LINK_TEXT, waveName).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.btn_selectAll_xpath).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.btn_bulkEdit_xpath).click()
            time.sleep(5)
            if tng == "Yes":
                self.driver.find_element(By.ID, self.ch_tngYes_id).click()
                self.logger.info("********** Sync Option 'TNG' is set as yes **********")
            if tng == "No":
                self.driver.find_element(By.ID, self.ch_tngNo_id).click()
                self.logger.info("********** Sync Option 'TNG' is set as no **********")

            if verbose == "Yes":
                self.driver.find_element(By.ID, self.ch_verboseYes_id).click()
                self.logger.info("********** Sync Option 'Verbose' is set as yes **********")
            if verbose == "No":
                self.driver.find_element(By.ID, self.ch_verboseNo_id).click()
                self.logger.info("********** Sync Option 'Verbose' is set as no **********")

            if passwordLess == "Yes":
                self.driver.find_element(By.ID, self.ch_passwordLessYes_id).click()
                self.logger.info("********** Sync Option 'Passwordless' is set as yes **********")
            if passwordLess == "No":
                self.driver.find_element(By.ID, self.ch_passwordLessNo_id).click()
                self.logger.info("********** Sync Option 'Passwordless' is set as no **********")

            if directFScopy == "Yes":
                self.driver.find_element(By.ID, self.ch_AllowDirectFScopyYes_id).click()
                self.logger.info("********** Sync Option 'Allow Direct Fscopy' is set as yes **********")
            if directFScopy == "No":
                self.driver.find_element(By.ID, self.ch_AllowDirectFScopyNo_id).click()
                self.logger.info("********** Sync Option 'Allow Direct Fscopy' is set as no **********")

            if FSDeletion == "Yes":
                self.driver.find_element(By.ID, self.ch_AllowFSDeletionYes_id).click()
                self.logger.info("********** Sync Option 'Allow FS Deletion' is set as yes **********")
            if FSDeletion == "No":
                self.driver.find_element(By.ID, self.ch_AllowFSDeletionNo_id).click()
                self.logger.info("********** Sync Option 'Allow FS Deletion' is set as no **********")

            if NoTransfer == "Yes":
                self.driver.find_element(By.ID, self.ch_NoTransferYes_id).click()
                self.logger.info("********** Sync Option 'No Transfer' is set as yes **********")
            if NoTransfer == "No":
                self.driver.find_element(By.ID, self.ch_NoTransferNo_id).click()
                self.logger.info("********** Sync Option 'No Transfer' is set as no **********")

            if transferCompress == "Yes":
                self.driver.find_element(By.ID, self.ch_TransferCompressYes_id).click()
                self.logger.info("********** Sync Option 'Transfer Compress' is set as yes **********")
            if transferCompress == "No":
                self.driver.find_element(By.ID, self.ch_TransferCompressNo_id).click()
                self.logger.info("********** Sync Option 'Transfer Compress' is set as no **********")

            if noTransferCompress == "Yes":
                self.driver.find_element(By.ID, self.ch_NoTransferCompressYes_id).click()
                self.logger.info("********** Sync Option 'No Transfer Compress' is set as yes **********")
            if noTransferCompress == "No":
                self.driver.find_element(By.ID, self.ch_NoTransferCompressNo_id).click()
                self.logger.info("********** Sync Option 'No Transfer Compress' is set as no **********")

            if ignoreMissing == "Yes":
                self.driver.find_element(By.ID, self.ch_IgnoreMissingYes_id).click()
                self.logger.info("********** Sync Option 'Ignore Missing' is set as yes **********")
            if ignoreMissing == "No":
                self.driver.find_element(By.ID, self.ch_IgnoreMissingNo_id).click()
                self.logger.info("********** Sync Option 'Ignore Missing' is set as no **********")

            if noInPlace == "Yes":
                self.driver.find_element(By.ID, self.ch_NoInPlaceYes_id).click()
                self.logger.info("********** Sync Option 'No In Place' is set as yes **********")
            if noInPlace == "No":
                self.driver.find_element(By.ID, self.ch_NoInPlaceNo_id).click()
                self.logger.info("********** Sync Option 'No In Place' is set as no **********")

            if noReboot == "Yes":
                self.driver.find_element(By.ID, self.ch_NoRebootYes_id).click()
                self.logger.info("********** Sync Option 'No Reboot' is set as yes **********")
            if noReboot == "No":
                self.driver.find_element(By.ID, self.ch_NoRebootNo_id).click()
                self.logger.info("********** Sync Option 'No Reboot' is set as no **********")

            if includeSAN == "Yes":
                self.driver.find_element(By.ID, self.ch_IncludeSANYes_id).click()
                self.logger.info("********** Sync Option 'Include SAN' is set as yes **********")
            if includeSAN == "No":
                self.driver.find_element(By.ID, self.ch_IncludeSANNo_id).click()
                self.logger.info("********** Sync Option 'Include SAN' is set as no **********")

            if excludeSAN == "Yes":
                self.driver.find_element(By.ID, self.ch_ExcludeSANYes_id).click()
                self.logger.info("********** Sync Option 'Exclude SAN' is set as yes **********")
            if excludeSAN == "No":
                self.driver.find_element(By.ID, self.ch_ExcludeSANNo_id).click()
                self.logger.info("********** Sync Option 'Exclude SAN' is set as no **********")

            if overrideRMMStorageCheck == "Yes":
                self.driver.find_element(By.ID, self.ch_OverrideRMMStorageCheckYes_id).click()
                self.logger.info("********** Sync Option 'Override RMM Storage Check' is set as yes **********")
            if overrideRMMStorageCheck == "No":
                self.driver.find_element(By.ID, self.ch_OverrideRMMStorageCheckNo_id).click()
                self.logger.info("********** Sync Option 'Override RMM Storage Check' is set as no **********")

            if deleteAllTargetFS == "Yes":
                self.driver.find_element(By.ID, self.ch_DeleteAllTargetFSYes_id).click()
                self.logger.info("********** Sync Option 'Delete All Target FS' is set as yes **********")
            if deleteAllTargetFS == "No":
                self.driver.find_element(By.ID, self.ch_DeleteAllTargetFSNo_id).click()
                self.logger.info("********** Sync Option 'Delete All Target FS' is set as no **********")

            if keepTargetLayout == "Yes":
                self.driver.find_element(By.ID, self.ch_KeepTargetLayoutYes_id).click()
                self.logger.info("********** Sync Option 'Keep Target Layout' is set as yes **********")
            if keepTargetLayout == "No":
                self.driver.find_element(By.ID, self.ch_KeepTargetLayoutNo_id).click()
                self.logger.info("********** Sync Option 'Keep Target Layout' is set as no **********")

            if cloudInit == "Yes":
                self.driver.find_element(By.ID, self.ch_CloudInitYes_id).click()
                self.logger.info("********** Sync Option 'Cloud Init' is set as yes **********")
            if cloudInit == "No":
                self.driver.find_element(By.ID, self.ch_CloudInitNo_id).click()
                self.logger.info("********** Sync Option 'Cloud Init' is set as no **********")

            time.sleep(5)
            self.driver.find_element(By.XPATH, self.btn_next_xpath).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.btn_modifyAll_xpath).click()
            time.sleep(5)
            self.driver.find_element(By.ID, self.btn_yes_id).click()
            time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, "Waves").click()

    def assignDRPolicy(self, waveName, policyNumber, startPolicy):
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_drPolicy_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.drp_selectDrPolicy_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="wave_detail_wave_policy_dr_policy"]/div/div[4]/div/ul/li['+str(policyNumber)+']/span').click()
        time.sleep(5)
        if startPolicy:
            self.driver.find_element(By.ID, self.ch_startPolicyNow_id).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.btn_assignPolicy_id).click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Waves").click()
