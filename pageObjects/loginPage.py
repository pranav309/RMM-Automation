import time
import keyboard

from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen


class LoginPage:
    txt_username_id = "username"
    txt_password_id = "password"
    btn_login_id = "login_btn"
    txt_admin_xpath = "/html/body/app-root/app-main-layout/header/div/div[2]/rw-user-settings/div[2]/span/i[2]"
    txt_rackWare_xpath = "//*[@id='content']/h1"

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()
        time.sleep(10)
        if len(self.driver.find_elements(By.LINK_TEXT, "Waves")) == 0:
            self.logger.info("********** Login Failed **********")
            time.sleep(2)
            # note = self.driver.find_element(By.XPATH,'/html/body/app-root/simple-notifications/div/simple-notification/div').text
            # self.logger.info(note)
            userName = self.driver.find_element(By.ID, self.txt_username_id)
            password = self.driver.find_element(By.ID, self.txt_password_id)
            if userName.get_attribute("value") == "" and password.get_attribute("value") == "":
                self.logger.info("********** Username & Password Both Fields Are Empty **********")
            elif userName.get_attribute("value") == "":
                self.logger.info("********** Username Field Is Empty **********")
            elif password.get_attribute("value") == "":
                self.logger.info("********** Password Field Is Empty **********")
            time.sleep(5)
        else:
            self.logger.info("********** Login Successful **********")

    def clickOnLogout(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_admin_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Log out").click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.txt_rackWare_xpath)) == 0:
            self.logger.info("********** Logout Failed **********")
        else:
            self.logger.info("********** Logout Successful **********")
