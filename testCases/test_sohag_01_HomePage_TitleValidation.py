import time
from selenium import webdriver
from pageObjects.sohag_LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class Test_001_Login:
    #get url and credentials from config.ini file
    # base_url =ReadConfig.getBaseUrl()
    exp_title=ReadConfig.getTitle()

    #call static LogGen() which will return looger obj>store in a variable
    log=LogGen.logGen()

    #pytest method-validate homepage title
    #by using fixture (conftest.py file) getting driver instance through setup
    def test_validateHomepageTitle1(self):
        self.log.info("####### test Homepage title statrt ########") #using looger


        # Optional: Chrome options
        options = webdriver.ChromeOptions()

        # Correct way to use ChromeDriverManager with Selenium 4.6+
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://demowebshop.tricentis.com/")
        self.log.info("--------url launced---------")#using looger
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        act_title = self.driver.title
        self.log.info("--------actual title captured---------")  # using looger
        # time.sleep(3)
        self.log.info("--------title validating---------")  # using looger

        if act_title == self.exp_title:
            self.log.info("--------Test case passed---------")#using looger
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_validateHomepageTitle.png")
            self.log.error("--------Test case failed---------")
            assert False


