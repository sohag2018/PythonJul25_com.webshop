"""
TC Homepage__02: Logo Validation
Validate that company logo is present
Launching URL "https://demowebshop.tricentis.com/"

"""

import time
from selenium import webdriver
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_Login:
    #get url and credentials from config.ini file
    base_url =ReadConfig.getBaseUrl()

    #call static LogGen() which will return looger obj>store in a variable
    log=LogGen.logGen()

    #by using fixture (conftest.py file) getting driver instance through setup
    def test_validateHomepageTitle1(self, setup):
        self.log.info("####### test Homepage Logo statrt ########") #using looger
        self.driver = setup
        self.driver.get(self.base_url)
        self.log.info("--------url launced---------")#using looger
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.log.info("--------Logo present or not capturing---------")  # using looger
        time.sleep(3)
        self.hp=HomePage(self.driver)
        logoPresentOrNot=self.hp.is_LogoPresent()
        print(logoPresentOrNot)
        self.log.info(f"--------Logo present:{logoPresentOrNot}---------")  # using looger

        if logoPresentOrNot == True:
            self.log.info("--------Test case passed---------")#using looger
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_validateHomepageTitle.png")
            self.log.error("--------Test case failed---------")
            assert False


