import time
from selenium import webdriver
from pageObjects.sohag_LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_002_Login:
    base_url =ReadConfig.getBaseUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    #call static loggen() which will return looger obj>store in a variable
    log=LogGen.logGen()
    """
    pytest method-validate login feature with valid credentials
    """
    def test_login(self,setup):
        self.log.info("########test_login starts###########")
        self.driver=setup
        self.driver.get(self.base_url)
        self.log.info("--------url launched---------")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        #create Loginpage obj
        self.lp=LoginPage(self.driver)
        self.log.info("--------clicing on login link---------")
        self.lp.click_login_link()
        self.log.info("--------passing login credentials--------")
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.log.info("-------clicking on login button--------")
        self.lp.clickLoginBtn()
        self.log.info("-------validating login success or not--------")
        act_login_title=self.driver.title
        time.sleep(3)
        self.log.info("-------getting profile text--------")
        actualProfileText=self.lp.getProfileText()
        time.sleep(3)
        self.log.info("-------validaying profile text--------")
        if actualProfileText == self.username:
            self.log.info("----test_login Test case pass---------")
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.log.info("--------test_login Test case failed---------")
            assert False
            self.driver.quit()

