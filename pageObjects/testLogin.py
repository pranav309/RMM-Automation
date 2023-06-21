import time
import unittest

import Locators.locLogin as LOC

from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(unittest.TestCase):

    logger = LogGen.loggen()

    @staticmethod
    def setUserName(driver, username):
        driver.find_element(By.ID, LOC.txt_username_id).send_keys(username)

    @staticmethod
    def setPassword(driver, password):
        driver.find_element(By.ID, LOC.txt_password_id).send_keys(password)

    def clickOnLogin(self, driver, username, password):
        self.logger.info("********** Logging In **********")
        un = driver.find_element(By.ID, LOC.txt_username_id)
        pw = driver.find_element(By.ID, LOC.txt_password_id)
        un.send_keys(username)
        pw.send_keys(password)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, LOC.btn_login_id))
        )
        driver.find_element(By.ID, LOC.btn_login_id).click()
        time.sleep(10)
        if len(driver.find_elements(By.LINK_TEXT, "Waves")) == 0:
            self.logger.info("********** Login Failed **********")
            if un.get_attribute("value") == "" and pw.get_attribute("value") == "":
                self.logger.info("********** Username & Password Both Fields Are Empty **********")
            elif un.get_attribute("value") == "":
                self.logger.info("********** Username Field Is Empty **********")
            elif pw.get_attribute("value") == "":
                self.logger.info("********** Password Field Is Empty **********")
        else:
            self.logger.info("********** Login Successful **********")

    def clickOnLogout(self, driver):
        self.logger.info("********** Logging Out **********")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
        )
        driver.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, LOC.txt_logout_xpath))
        )
        driver.find_element(By.XPATH, LOC.btn_yes_xpath).click()
        time.sleep(5)
        if len(driver.find_elements(By.XPATH, LOC.txt_rackWare_xpath)) == 0:
            self.logger.info("********** Logout Failed **********")
            driver.find_element(By.XPATH, LOC.btn_no_xpath).click()
        else:
            self.logger.info("********** Logout Successful **********")
