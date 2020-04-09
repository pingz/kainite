from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def setup_driver(firefox_profile_dir):
    firefox_profile = FirefoxProfile(firefox_profile_dir)
    driver = webdriver.Firefox(
        firefox_profile=firefox_profile
    )
    return driver

