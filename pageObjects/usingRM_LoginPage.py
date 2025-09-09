from pageObjects.ReuseableMethods import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


