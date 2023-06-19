import time
import keyboard

from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    txt_username_id = "username"
    txt_password_id = "password"
    btn_login_id = "login_btn"
    txt_admin_xpath = "/html/body/app-root/app-main-layout/header/div/div[2]/rw-user-settings/div[2]/span/i[2]"
    txt_rackWare_xpath = "//*[@id='content']/h1"
    txt_logout_xpath = '//*[@id="nav-panel"]/nav/rw-nav-user-settings/div[2]/span[3]/rw-rmmlite-logout/p-confirmdialog/div/div[1]/span'
    btn_yes_xpath = '//*[@id="nav-panel"]/nav/rw-nav-user-settings/div[2]/span[3]/rw-rmmlite-logout/p-confirmdialog/div/div[3]/button[1]/span'
    btn_no_xpath = '//*[@id="nav-panel"]/nav/rw-nav-user-settings/div[2]/span[3]/rw-rmmlite-logout/p-confirmdialog/div/div[3]/button[2]/span'

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickOnLogin(self):
        userName = self.driver.find_element(By.ID, self.txt_username_id)
        password = self.driver.find_element(By.ID, self.txt_password_id)
        self.driver.find_element(By.ID, self.btn_login_id).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Waves"))
        )
        if len(self.driver.find_elements(By.LINK_TEXT, "Waves")) == 0:
            self.logger.info("********** Login Failed **********")
            # note = self.driver.find_element(By.XPATH,'/html/body/app-root/simple-notifications/div/simple-notification/div').text
            # self.logger.info(note)
            if userName.get_attribute("value") == "" and password.get_attribute("value") == "":
                self.logger.info("********** Username & Password Both Fields Are Empty **********")
            elif userName.get_attribute("value") == "":
                self.logger.info("********** Username Field Is Empty **********")
            elif password.get_attribute("value") == "":
                self.logger.info("********** Password Field Is Empty **********")
        else:
            self.logger.info("********** Login Successful **********")

    def clickOnLogout(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
        )
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_logout_xpath))
        )
        self.driver.find_element(By.XPATH, self.btn_yes_xpath).click()
        time.sleep(5)
        if len(self.driver.find_elements(By.XPATH, self.txt_rackWare_xpath)) == 0:
            self.logger.info("********** Logout Failed **********")
            self.driver.find_element(By.XPATH, self.btn_no_xpath).click()
        else:
            self.logger.info("********** Logout Successful **********")
