# Common Data for Cloud Users
txt_config_xpath = '//*[@id="nav-panel"]/nav/ul/li[8]'
txt_cu_xpath = '//*[@id="nav-panel"]/nav/ul/li[8]/ul/li[1]'
txt_org_xpath = '//*[@id="nav-panel"]/nav/ul/li[8]/ul/li[2]'
txt_vc_xpath = '//*[@id="nav-panel"]/nav/ul/li[8]/ul/li[3]'
txt_ds_xpath = '//*[@id="nav-panel"]/nav/ul/li[8]/ul/li[4w]'
txt_totalUser_xpath = '//*[@id="content"]/div/article/div/div[2]/p-table/div/div[2]/table/tbody/tr'
txt_name_id = "UserId"

btn_add_id = "conf_cu_add_btn"
btn_edit_id = "conf_cu_edit_btn"
btn_delete_id = "conf_cu_del_btn"
btn_confirm_id = "conf_cu_add_cloud_modal_submit_btn"
btn_cancel_id = "conf_cu_add_cloud_modal_cancel_btn"

drp_cloudProvider_xpath = "//*[@id='conf_cu_add_cloud_modal']/div/div/div/form/div[2]/div/div/div[2]/div/select"


# AWS
txt_AWSAccessKey_id = "configuration_clouduser_add_cloud_modal_aws_accessKey"
txt_AWSSecretAccessKey_id = "configuration_clouduser_add_cloud_modal_aws_secretAccessKey"


# Azure
txt_AzureSubscriptionId_id = "configuration_clouduser_add_cloud_modal_azure_subscriptionId"
txt_AzureTenantId_id = "configuration_clouduser_add_cloud_modal_azure_tenantId"
txt_AzureClientId_id = "configuration_clouduser_add_cloud_modal_azure_clientId"
txt_AzureClientSecret_id = "configuration_clouduser_add_cloud_modal_azure_clientSecret"

drp_AzureCloudType_xpath = "//*[@id='configuration_clouduser_add_cloud_modal_azure_datacenter']"
drp_AzureDataCentre_xpath = "//*[@id='configuration_clouduser_add_cloud_modal_azure_datacenter']/div/input"


# Google
txt_GGLPathOnRMM_id = "gcpFilePath"
txt_GGLProjectId_id = "projectid"

rd_GGLUploadLocal_xpath = "//*[@id='conf_cu_add_cloud_modal']/div/div/div/form/div[2]/div/div/div[3]/div[1]/div[1]/div[1]/div/div/input"
rd_GGLFilePath_xpath = "//*[@id='conf_cu_add_cloud_modal']/div/div/div/form/div[2]/div/div/div[3]/div[1]/div[1]/div[2]/div/div/input"

src_GGLBrowse_xpath = "//*[@id='browse_dropzone']/div/div/label/i"


# IBM Cloud VPC
txt_IBMapiKey_id = "apikey"
drp_IBMRegion_xpath = "//*[@id='configuration_clouduser_add_cloud_modal_ibmgen2_region']/div/input"


# CloudStack
txt_CSApiUrl_id = "cloudstack_apiUrl"
txt_CSApiKey_id = "cloudstack_apiKey"
txt_CSSecretKey_id = "cloudstack_secretKey"
txt_CSDomainId_id = "cloudstack_domainid"


# OCI
txt_OCIUserId_id = "oci_userId"
txt_OCIPathOnRMM_id = "oci_pkFilePath"
txt_OCIFingerprint_id = "oci_fingerprint"
txt_OCITenantId_id = "oci_tenantId"
txt_OCIPassphrase_id = "oci_passphrase"
txt_OCIApiUrl_id = "oci_apiUrl"
txt_OCICompartmentName_id = "oci_compartment_name"
txt_OCICompartmentId_id = "oci_compartment_id"
txt_OCICertPathOnRMM_id = "oci_certificateSourcePath"

rd_OCIFilePath_xpath = "ociPrivateKeySourceFile path on RMM"
rd_OCICertFilePath_xpath = "ociCertificateSourceUpload local File"
rd_OCIUploadFile_id = "ociPrivateKeySourceUpload local File"
rd_OCIParameterName_id = "ociParamTypeName"
rd_OCIParameterId_id = "ociParamTypeID"
rd_OCICertUploadFile_id = "ociCertificateSourceUpload local File"

src_OCICertBrowse_xpath = "//*[@id='browse_dropzone']/div/div/label"
src_OCIBrowse_xpath = "//*[@id='browse_dropzone']/div/div/label/i"
drp_OCIRegion_xpath = "//*[@id='configuration_clouduser_add_cloud_modal_oci_datacenter']/div/input"


# Softlayer
txt_SLUserName_id = "userName"
txt_SLApiKey_id = "apiKey"
txt_SlDomainName_id = "domainName"
txt_SLAccessRights_id = "accessrights"

chBox_SLHourly_id = "check-hourly"


# Zadara
txt_ZadaraAccessKey_id = "configuration_clouduser_add_cloud_modal_zadara_accessKey"
txt_ZadaraSecretAccessKey_id = "configuration_clouduser_add_cloud_modal_zadara_secretAccessKey"
txt_ZadaraApiUrl_id = "zadara_apirul"
txt_ZadaraRegion_id = "zadara_region"


# VCenter data
txt_VCName_id = "name"
txt_VCipAddress_id = "address"
txt_VCUserName_id = "username"
txt_VCPassword_id = "password"
txt_VCPort_id = "port"

btn_createVC_id = "conf_vc_add_btn"
btn_editVC_id = "conf_vc_edit_btn"
btn_deleteVC_id = "conf_vc_del_btn"
btn_addVC_id = "conf_vc_vc_add_modal_submit_btn"


# Organization
btn_addAdminOrg_xpath = "//*[@id='content']/div/article/div/div[2]/div[2]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node/div/tree-node-wrapper/div[1]/div/span/i[1]"
btn_addAdminUser_xpath = "//*[@id='content']/div/article/div/div[2]/div[2]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node/div/tree-node-wrapper/div[1]/div/span/i[2]"
btn_editAdminOrg_xpath = "//*[@id='content']/div/article/div/div[2]/div[2]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node/div/tree-node-wrapper/div[1]/div/span/i[3]"


# Pop-up Banners
pop_addCloudUser_xpath = '//*[@id="conf_cu_add_cloud_modal"]/div/div/div/form/div[1]/h4'
pop_addVC_xpath = '//*[@id="conf_vc_add_vc_modal_btn"]/div/div/div/form/div[1]/h4'
not_addVC_xpath = '/html/body/app-root/simple-notifications/div/simple-notification[2]/div'
pop_successful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification/div'
pop_deleteSuccessful_xpath = '/html/body/app-root/simple-notifications/div/simple-notification[2]/div'
