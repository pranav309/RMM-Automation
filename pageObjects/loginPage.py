import time

from selenium.webdriver.common.by import By


class LoginPage:
    txt_username_id = "username"
    txt_password_id = "password"
    btn_login_id = "login_btn"
    txt_admin_xpath = "/html/body/app-root/app-main-layout/header/div/div[2]/rw-user-settings/div[2]/span/i[2]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def clickOnLogout(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txt_admin_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Log out").click()
        time.sleep(5)
