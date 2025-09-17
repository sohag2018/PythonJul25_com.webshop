from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    for commmonly used methods
    note: through constructor it will get driver
    How to use these methods:
    1.we will use in our page classes by making Bases class as a
    perent class (put Base class in parenthise oof child class)
    2. in chile class constructor we will call Base class constructor and passs driver
    by super()
    ____
    Or
    ____
    we can create an obj of Base class in page classes
    """

    #generic/reuseabe methods
    #findElement
    #findsElement
    #sendKeys
    #ClickOnElement
    #
    def __init__(self,driver):
        self.driver=driver

    # findElement


    def find_SingleElement(self,locatorType,locatorValue):
        locatorType=locatorType.lower()
        #map
        by_type={
           "id":By.ID,
           "name":By.NAME,
           "class":By.CLASS_NAME,
           "link_text":By.LINK_TEXT,
           "partial_link_text":By.PARTIAL_LINK_TEXT,
           "xpath":By.XPATH,
           "css_selector":By.CSS_SELECTOR,
           "tag_name":By.TAG_NAME
        }

        element=self.driver.find_element(by_type.get(locatorType),locatorValue)
        return element

    # def find_SingleElement(self,locatorType,locatorValue,timeout=10):
    #
    #     locatorType=locatorType.lower()
    #     #map
    #     try:
    #         by_type={
    #            "id":By.ID,
    #            "name":By.NAME,
    #            "class":By.CLASS_NAME,
    #            "link_text":By.LINK_TEXT,
    #            "partial_link_text":By.PARTIAL_LINK_TEXT,
    #            "xpath":By.XPATH,
    #            "css_selector":By.CSS_SELECTOR,
    #            "tag_name":By.TAG_NAME
    #         }
    #
    #         element=WebDriverWait(self.driver, timeout).until(
    #         EC.visibility_of_element_located((by_type.get(locatorType),locatorValue))
    #     )
    #         return element
    #     except (TimeoutException, NoSuchElementException) as e:
    #         print(e)


    def find_ListOfElements(self, locatorType, locatorValue):
        locatorType = locatorType.lower()
        # map
        by_type = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "css_selector": By.CSS_SELECTOR,
            "tag_name": By.TAG_NAME
        }

        elements = self.driver.find_elements(by_type.get(locatorType), locatorValue)
        return elements

    def select_dropdown(self, locatorType, locatorValue,select_method,method_value):
        locatorType = locatorType.lower()
        # map
        by_type = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "css_selector": By.CSS_SELECTOR,
            "tag_name": By.TAG_NAME
        }

        element = self.driver.find_element(by_type.get(locatorType), locatorValue)

        #obj of Select--to call select class methods
        select=Select(element)
        select_method=select_method.lower()
        if select_method=="index":
            dropdown_value=select.select_by_index(method_value)
        elif select_method=="visible_text":
            dropdown_value=select.select_by_visible_text(method_value)
        elif select_method == "value":
            dropdown_value=select.select_by_value(method_value)

        return dropdown_value



