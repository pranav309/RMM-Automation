# import openpyxl
#
# workBook = openpyxl.load_workbook(r"C:\Users\Pranav Pawar\PycharmProjects\RMM_DataDriven\TestData\secondFlow\bulkEditOptionsWindows.xlsx")
# sheet = workBook.active
# rows = sheet.max_row

# hosts = sheet.cell(row=3, column=2).value
# TNG = sheet.cell(row=2, column=3).value
#
# print("Type of hosts: ", type(hosts))
# print("Type of TNG: ", type(TNG))

# res = tuple(map(int, hosts.split(', ')))
# for i in res:
#     print(i)
# if type(TNG) != str:
#     print("Hello...")
# print("Number Of Rows : ", rows)

import time
import paramiko
#
# router_ip = "172.29.31.111"
# router_username = "root"
# router_password = "rackware"
#
# ssh = paramiko.SSHClient()
#
# # Load SSH host keys.
# ssh.load_system_host_keys()
# # Add SSH host key automatically if needed.
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # Connect to router using username/password authentication.
# ssh.connect(router_ip,
#             username=router_username,
#             password=router_password,
#             look_for_keys=False)

# # Run command.
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("rpm -qa | grep rwfs")
#
# output = ssh_stdout.readlines()
# print(output)
# # Close connection.
# ssh.close()
#
# # Analyze show ip route output
# for line in output:
#     if "0.0.0.0/0" in line:
#         print("Found default route:")
#         print(line)


def loginSSH():
    vm_ip = "172.29.30.127"
    vm_username = "root"
    vm_password = "rackware"

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(vm_ip,
                username=vm_username,
                password=vm_password,
                look_for_keys=False)


def deleteSR(source, target):
    vm_ip = "172.29.30.127"
    vm_username = "root"
    vm_password = "rackware"

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(vm_ip,
                username=vm_username,
                password=vm_password,
                look_for_keys=False)
    ssh.exec_command("rw ic srd " + str(source) + " --target " + str(target))


# loginSSH()
deleteSR("psp-MyWinSecondFlow-src2-IMAGE", "psp-MyWinSecondFlow-tgt2")
