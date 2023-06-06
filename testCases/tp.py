# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Firefox()
# driver.get("https://172.29.30.127/#/auth/login")
# driver.maximize_window()
# time.sleep(10)
# driver.find_element(By.ID, "username").send_keys("admin")
# driver.find_element(By.ID, "password").send_keys("Pranav309")
# time.sleep(5)
# driver.find_element(By.ID, "login_btn").click()
# WebDriverWait(driver, 120).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="waves_add_wave"]/span/i'))
# )
# time.sleep(5)
# # Find the element
# element = driver.find_element(By.LINK_TEXT, "Replication")
#
# # Retrieve the class attribute
# element_class = element.get_attribute("class")
#
# print(element_class)
#
# driver.find_element(By.LINK_TEXT, "Logout").click()
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="nav-panel"]/nav/rw-nav-user-settings/div[2]/span[3]/rw-rmmlite-logout/p-confirmdialog/div/div[3]/button[1]/span').click()
# time.sleep(5)
#
# driver.quit()

import openpyxl
workBook = openpyxl.load_workbook(r"C:\Users\Pranav Pawar\PycharmProjects\RMM_DataDriven\TestData\firstFlow/changeTargetType.xlsx")
sheet = workBook.active
rows = sheet.max_row
print(rows)
