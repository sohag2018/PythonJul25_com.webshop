import time
from selenium.webdriver.common.by import By
class LoginPage():
    # find all locators
    login_link_xpath="//a[normalize-space()='Log in']"
    txt_username_id="Email"
    txt_password="Password"
    btn_login_cssSelector="input[value='Log in']"
    usr_profileName_CssSelector="div[class='header-links'] a[class='account']"


    #constructor receives webdriver instance
    def __init__(self, driver):
        self.driver = driver

    #action methods
    def click_login_link(self):
        self.driver.find_element(By.XPATH, self.login_link_xpath).click()
        time.sleep(2)

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).clear()
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)
        time.sleep(2)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password).clear()
        self.driver.find_element(By.ID, self.txt_password).send_keys(password)
        time.sleep(2)
    def clickLoginBtn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_login_cssSelector).click()

    def getProfileText(self):
        profileTxt=self.driver.find_element(By.CSS_SELECTOR, self.usr_profileName_CssSelector).text
        return profileTxt
