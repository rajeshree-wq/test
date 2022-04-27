import os
from datetime import datetime

import pytest
from selenium import webdriver






@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome("C:\\Users\\Chepa\\PycharmProjects\\chromedriver.exe")
        print("Launching Chrome browser")
    elif browser=='edge':
        driver=webdriver.Edge("C:\\Users\\Chepa\\PycharmProjects\\msedgedriver.exe")
        print("Launching Edge browser")

    return driver


def pytest_addoption(parser):  #this will get the value from command line arg
    parser.addoption("--browser")

@pytest.fixture( )
def browser(request):  #this will return the browser value to set up method
    return request.config.getoption("--browser")


##############    Pytest HTML Report ###########################33
# It is hook for adding environment into html Report
def pytest_configure(config):
    config._metadata['Project Name']="E Commerence"
    config._metadata['Module Name'] = "Customer"
    config._metadata['Tester'] = "Rajeshree"
    config._metadata['Developmer'] = "xyz"

    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = 'Reorts/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"



##  It is hook for adding / deleting  environment into html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)  ## this detail bydefault display in html report
    metadata.pop("Plugins", None)   ## this detail bydefault display in html report

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config._metadata['Project Name'] = "E Commerence"
#     config._metadata['Module Name'] = "Customer"
#     config._metadata['Tester'] = "Rajeshree"
#     config._metadata['Developmer'] = "xyz"
#     if not os.path.exists('reports'):
#         os.makedirs('reports')
#     config.option.htmlpath = 'Reorts/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


