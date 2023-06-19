from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_driver(browser_name):
    if browser_name.lower() == "chrome":
        chrome_options = ChromeOptions()
        return webdriver.Chrome(options=chrome_options)
    elif browser_name.lower() == 'firefox':
        firefox_options = FirefoxOptions()
        return webdriver.Firefox(options=firefox_options)
    elif browser_name.lower() == 'edge':
        edge_options = EdgeOptions()
        return webdriver.Edge(options=edge_options)

    else:
        raise ValueError("Invalid browser name. Supported browsers: Chrome, Firefox, Edge, Safari, Chromium")
