import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.ExcelReader import ExcelReader
from utilities.customLogger import LogGen


class Test_001_Login:

    # base_url = "https://demowebshop.tricentis.com/"
    # username = "dummypass123@gmail.com"
    # password = "DummyPass123"
    base_url =ReadConfig.getBaseUrl()
    log=LogGen.logGen()

    def test_validateHomepageTitle1(self, setup):
        self.log.info("--------test_validateHomepageTitle1 starts--------")
        testDataFile = 'C:/Users/enthr/PycharmProjects/com.demoshop/TestData/TestData.xlsx'
        #self.log.info("--------testData file loaded---------")
        rows = ExcelReader.getRowCount(testDataFile, 'Sheet1')
        for r in range(2, rows + 1):
            self.log.info("--------data read from testdata file--------")
            username = ExcelReader.getCellData(testDataFile, 'Sheet1', r, 1)
            password = ExcelReader.getCellData(testDataFile, 'Sheet1', r, 2)
            self.log.info("--------Webdriver instance getting--------")
            self.driver = setup
            self.driver.get(self.base_url)
            self.log.info("--------url launched---------")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            # create Loginpage obj
            self.log.info("--------Login page object creating--------")
            self.lp = LoginPage(self.driver)
            self.log.info("--------clicing on login link-------")
            self.lp.click_login_link()
            self.log.info("--------using login credentials--------")
            self.lp.setUsername(username)
            self.lp.setPassword(password)
            self.lp.clickLoginBtn()
            self.log.info("--------successfully logged in--------")



