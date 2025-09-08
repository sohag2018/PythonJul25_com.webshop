from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    """
    Constructor: takes driver and timeout to use in every methods

    """
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

        def find_element(self, locator_type: str, locator_value: str):
            locator_type = locator_type.lower()
            by_types = {
                "id": By.ID,
                "name": By.NAME,
                "xpath": By.XPATH,
                "css": By.CSS_SELECTOR,
                "class": By.CLASS_NAME,
                "tag": By.TAG_NAME,
                "link_text": By.LINK_TEXT,
                "partial_link_text": By.PARTIAL_LINK_TEXT,
            }

            return self.driver.find_element(by_types.get(locator_type), locator_value)

        # How to use:
        """

        rm=ReuseableMethods(driver)
    elem = rm.find_element("id", "login-button")
    elem = rm.find_element("xpath", "//input[@name='username']")   
        """

    def find(self, by, value):
        """Find a single element"""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            raise Exception(f"Element not found: {by} = {value}")

    def find_all(self, by, value):
        """Find multiple elements"""
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        """Click an element"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
        except TimeoutException:
            raise Exception(f"Unable to click on the element: {by} = {value}")

    def send_keys(self, by, value, text, clear_first=True):
        """Send text to input field"""
        element = self.find(by, value)
        if clear_first:
            element.clear()
        element.send_keys(text)
        """ USE: self(CHILD).send_keys(*self.USERNAME_INPUT, text=username)"""
    def get_text(self, by, value):
        """Get text from element"""
        element = self.find(by, value)
        return element.text

    def is_displayed(self, by, value):
        """Check if element is displayed"""
        try:
            return self.find(by, value).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_element(self, by, value):
        """Wait for an element to be present"""
        return self.find(by, value)

    def wait_for_invisibility(self, by, value):
        """Wait until an element is not visible"""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.invisibility_of_element_located((by, value))
            )
        except TimeoutException:
            raise Exception(f"Element still visible after timeout: {by} = {value}")

    def get_attribute(self, by, value, attribute):
        """Get an element's attribute"""
        element = self.find(by, value)
        return element.get_attribute(attribute)