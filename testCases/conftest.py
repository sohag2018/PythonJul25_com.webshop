import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
   if browser == 'chrome':
      driver=webdriver.Chrome()
   elif browser == 'firefox':
      driver=webdriver.Firefox()
   elif browser == 'safari':
      driver=webdriver.Safari()
   elif browser == 'opera':
      driver=webdriver.Opera()
   else:
      driver = webdriver.Edge()
   return driver

#hook which will help to recognize --broser as an option keyword to pytest
def pytest_addoption(parser):
   parser.addoption("--browser")

#adding one more fixture to read value of --browser and return as a fixture
@pytest.fixture
def browser(request):
   return request.config.getoption('--browser')

##############################for HTML########################################
# def pytest_configure(config):  #hook to add configuratoin
#    config._metadata['Project']='Demoshop'
#    config._metadata['Module']='Login'
#    config._metadata['Build Version']='1.0'
#    config._metadata['Tester']='Sohag'
#
#
# #hook to delete info from html repot
# def pytest_metadata(metadata):
#    metadata.pop('JAVA_HOME', None)
#    metadata.pop('Plugins', None)







