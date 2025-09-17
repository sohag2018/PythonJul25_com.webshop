#locator
import time
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from pageObjects.ReuseableMethods import BasePage

from pageObjects.sohag_LoginPage import LoginPage


class HomePage:
    
    logo_xpath="//img[@alt='Tricentis Demo Web Shop']"
    login_link_xpath = "//a[normalize-space()='Log in']"

    #constructor
    def __init__(self, driver):
        self.driver = driver
        self.rm = BasePage(driver)

    #actions method

    def is_LogoPresent(self):
        print("sohag.......")
        #flag=self.driver.find_element(By.XPATH, self.logo_xpath).is_displayed()
        flag=self.rm.find_SingleElement("xpath",self.logo_xpath).is_displayed()
        return flag


    def click_login_link(self):
        self.driver.find_element(By.XPATH, self.login_link_xpath).click()
        time.sleep(2)
