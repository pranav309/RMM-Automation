import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def setup(browser):
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(options=options)
        print("Launching firefox browser.........")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):  # This will return the Browser value to /setup method
    return request.config.getoption("--browser")


#####################
# pytest HTML Report #
#####################

# It is /hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'RMM Product'
    config._metadata['Module Name'] = 'Disaster Recovery'
    config._metadata['Tester'] = 'Pranav Pawar'


# It is /hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
