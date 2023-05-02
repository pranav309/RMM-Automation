import time
import openpyxl
import keyboard

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utilities.customLogger import LogGen


class TP:

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def selectCheck(self, waveName):
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, waveName).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/article/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[8]/span/div/i[2]').click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, 'System').click()
        time.sleep(5)
        tmp = self.driver.find_element(By.LINK_TEXT, 'System').is_selected()
        print(tmp)
        tmp1 = self.driver.find_element(By.LINK_TEXT, 'vCenter Options').is_selected()
        print(tmp1)
        self.driver.find_element(By.ID, "wave_detail_edit_item_modify_btn").click()
