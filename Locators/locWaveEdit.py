txt_waveName_xpath = '//*[@id="content"]/article/div/div[1]/div/h3/strong'
txt_totalNICs_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div/div[4]/div[1]/div/div'
txt_editSystem_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_edit_item"]/div/div/div/form/div[2]/div/p-tabview/div/ul/li[1]'
txt_editSyncOption_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_edit_item"]/div/div/div/form/div[2]/div/p-tabview/div/ul/li[2]'
txt_bulkEditSyncOption_xpath = '//*[@id="main"]/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[4]/div/p-tabview/div/ul/li[1]'
txt_editCU_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_edit_item"]/div/div/div/form/div[2]/div/p-tabview/div/ul/li[3]'
txt_bulkEditCU_xpath = '//*[@id="main"]/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[4]/div/p-tabview/div/ul/li[2]'
txt_setAutoEnv_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_cloudUserEdit"]/div/div/div/form/div[1]/h4'
txt_totalHosts_id = "wave_policy_wave_policy_wave_detail_elapsed_time_info"


# Autoprovision
txt_environment_xpath = "//*[@id='clouduser']"
txt_clusterName_xpath = "//*[@id='wave_detail_cu_edit_vc_clustername']/div/input"
txt_ESXHost_xpath = "//*[@id='wave_detail_cu_edit_vc_esx_host']/div/input"
txt_Datastore_xpath = "//*[@id='wave_detail_cu_edit_vc_dc']/div/input"
txt_autoprovision_id = "wave_policy_wave_policy_wave_detail_autoprovision"

btn_applyChanges_id = "wave_detail_cu_edit_apply_changes_btn"


# Single Edit Set NIC
txt_deviceName_id = "wave_detail_edit_item_nic_device_name"
txt_type_id = "wave_detail_edit_item_nic_type"
txt_networkName_id = "wave_detail_edit_item_nic_networkName"
txt_CIDR_id = "wave_detail_edit_item_nic_cidr"
txt_gateway_id = "wave_detail_edit_item_nic_gateway"
txt_DNS1_id = "wave_detail_edit_item_nic_dns1"
txt_DNS2_id = "wave_detail_edit_item_nic_dns2"

btn_NICAdd_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div/div[4]/div[2]/a"
btn_save_id = "wave_detail_edit_item_nic_save_btn"

rd_DHCP_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/edit-item-nic/div/div/div/form/div[2]/div[1]/div[4]/div/div[1]/div/div/input"
rd_staticIP_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/edit-item-nic/div/div/div/form/div[2]/div[1]/div[4]/div/div[2]/div/div/input"


# Bulk Edit Set NIC
txt_deviceNameBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[1]/span/input"
txt_typeBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[2]/span/input"
txt_networkNameBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[3]/span/input"
txt_CIDRBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[2]/div[1]/span/input"
txt_gatewayBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[2]/div[2]/span/input"
txt_DNS1BulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[2]/div[3]/span/input"
txt_DNS2BulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[2]/div[4]/span/input"

btn_save_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[3]/div/button[2]"
btn_NICAddBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[4]/div/p-tabview/div/div/p-tabpanel[2]/div/div/div[5]/div[3]/a/i"

rd_DHCPBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[4]/div/div[1]/div/div/input"
rd_staticIPBulkEdit_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[2]/div[1]/div[4]/div/div[2]/div/div/input"


# Sync Options
txt_filePathOnRmm_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[2]/div/div[2]/div[3]/div[2]/input"
txt_eventScript_id = "wave_detail_edit_item_options_eventScript"
txt_eventScriptArgs_id = "wave_detail_edit_item_options_eventArgs"
txt_excludeFile_id = "wave_detail_edit_item_options_exclude"
txt_includeFile_id = "wave_detail_edit_item_options_include"

btn_syncOptions_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/ul/li[2]/a/span"
btn_cancelEdit_xpath = '//*[@id="wave_detail_edit_item_cancel_btn"]'
btn_uploadLocalFile_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[2]/div/div[2]/div[3]/div[2]/div/div/label"
btn_modify_id = "wave_detail_edit_item_modify_btn"

rd_uploadLocalFile_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[2]/div/div[2]/div[3]/div[1]/div[1]/div/div/input"
rd_filePathOnRmm_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[2]/div/div[2]/div[3]/div[1]/div[2]/div/div/input"
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
txt_blkExcludeFile_id = "wave_detail_bulk_edit_item_options_exclude"
txt_blkIncludeFile_id = "wave_detail_bulk_edit_item_options_include"

btn_selectAll_xpath = "//*[@id='content']/article/div/div[2]/p-table/div/div[2]/table/thead/tr/th[1]/p-tableheadercheckbox/div/div[2]"
btn_bulkEdit_xpath = "//*[@id='content']/article/div/div[2]/p-table/div/div[1]/div[1]/button[8]/span/i"
btn_next_xpath = "//*[@id='main']/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[5]/div/button[2]"
btn_modifyAll_xpath = "//*[@id='main']/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[5]/div/button[2]"
btn_cancelBulkEdit_xpath = '//*[@id="main"]/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[5]/div/button[1]'
btn_yes_id = "wave_policy_wave_policy_wave_detail_autoprov_not_conf_yes_btn"

drp_goal_id = "wave_detail_bulk_edit_item_existing_capture_type"


# AWS CU
txt_AwsVpcId_id = "wave_detail_cu_edit_aws_options_vpc_id"
txt_AWSSubnetID_id = "wave_detail_cu_edit_aws_options_subnet_id"

# OCI Sync Options
txt_OCIVCNName_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div[1]/div[3]/div/input"
txt_OCISubnetName_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div[1]/div[4]/div/input"
txt_OCIAVDomain_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div[1]/div[9]/div/input"
txt_OCIRegion_xpath = '//*[@id="wave_detail_cu_edit_oci_dc"]/div/input'

# Change Target Type
txt_captureImage_xpath = "//*[@id='wave_detail_edit_item_clone_name']"
txt_targetIP_id = "wave_detail_edit_item_target_dns_ip"
txt_friendlyName_id = "wave_detail_edit_item_target_friendlyname"
txt_userName_id = "wave_detail_edit_item_target_username"
txt_imageName_id = "wave_detail_edit_item_clone_name"

rd_autoprovision_id = "wave_detail_edit_item_provisioning_model_radio_0"
rd_existingSystem_id = "wave_detail_edit_item_provisioning_model_radio_1"
rd_capture_id = "wave_detail_edit_item_provisioning_model_radio_2"
rd_directSync_id = "wave_detail_edit_item_existing_capture_type_0"
rd_stage12_id = "wave_detail_edit_item_existing_capture_type_1"
rd_stage1_id = "wave_detail_edit_item_existing_capture_type_2"
rd_stage2_id = "wave_detail_edit_item_existing_capture_type_3"

ch_passthrough_id = "wave_detail_edit_item_options_sshonly_target"


# Change Datastore
txt_editDatastore_xpath = "//*[@id='target_vcenter_datastore']/div/input"
txt_sinClusterName_xpath = '//*[@id="wave_detail_cu_edit_vc_clustername"]/div/input'
txt_esxHost_xpath = '//*[@id="wave_detail_cu_edit_vc_esx_host"]/div/input'
txt_dataStore_xpath = '//*[@id="target_vcenter_datastore"]/div/input'
txt_vmFolder_xpath = '//*[@id="wave_detail_edit_item_options_vm_folder"]'
txt_resourcePool_xpath = '//*[@id="wave_detail_edit_item_options_resource_pool"]'
txt_routes_xpath = '//*[@id="wave_detail_edit_item_options_routes"]'
txt_vmFolder_id = "wave_detail_bulk_edit_item_options_vm_folder"
txt_resourcePool_id = "wave_detail_bulk_edit_item_options_resource_pool"
txt_routes_id = "wave_detail_bulk_edit_item_options_routes"

btn_vCenterOption_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[4]/div/p-tabview/div/ul/li[2]/a/span'
btn_cancelVCEdit_xpath = '//*[@id="main"]/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[5]/div/button[1]'
btn_cancelSingleVC_xpath = '//*[@id="wave_detail_edit_item_cancel_btn"]'

drp_clusterName_id = "wave_b_edit_vc_clustername"
drp_esxHost_id = "wave_b_edit_vc_esx_host"
drp_datastore_id = "target_vcenter_datastore"

val_vCenterEdit_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[4]/div/p-tabview/div/div/p-tabpanel[2]/div/div/div[2]/label'


# Pop-up Banners
var_waveDetails_xpath = '//*[@id="rmm_lite_header"]/div/div[1]/div[2]'
var_addNIC_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div/div[4]/div[1]/div/div/div[1]/div[1]/b'
var_bulkNIC_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[4]/div/p-tabview/div/div/p-tabpanel[2]/div/div/div[5]/div[1]/div/div/div[1]/div[1]/b'

pop_setAutoprovision_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_cloudUserEdit"]/div/div/div/form/div[1]/h4'
pop_edit_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_edit_item"]/div/div/div/form/div[1]/h4'
pop_addNIC_xpath = '//*[@id="wave_detail_edit_item_edit_item_nic"]/div/div/div/form/div[1]/h4'
pop_bulkEdit_xpath = '//*[@id="main"]/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[1]/h4'
pop_bulkNIC_xpath = '//*[@id="main"]/rw-wave-detail/bulk-edit/edit-item-nic/div/div/div/form/div[1]/h4'
pop_bulkSyncOpt_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/bulk-edit/div[1]/div/div/form/div[4]/div/p-tabview/div/div/p-tabpanel[1]/div/div[1]/div[1]/label'
pop_moveHost_xpath = '//*[@id="wave_policy_wave_policy_wave_detail_move_item"]/div/div/div/div[1]/h4'
pop_successful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification/div'
pop_deleteSuccessful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification[2]/div'
pop_editHost_xpath = '/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[1]/div/div[3]/div[1]/h3'
pop_vc_xpath = "/html/body/app-root/app-main-layout/div/rw-wave-detail/edit-item/div/div/div/form/div[2]/div/p-tabview/div/div/p-tabpanel[3]/div/div/div[1]/label"


# Move hosts
btn_moveMachine_id = "wave_detail_move_item_move_machine_btn"

drp_selectWave_xpath = "//*[@id='wave_policy_wave_policy_wave_detail_move_item']/div/div/div/div[2]/div/div/select"
