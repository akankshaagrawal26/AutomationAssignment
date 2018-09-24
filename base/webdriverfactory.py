"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

"""
from selenium import webdriver
import os
from base.config_reader import ConfigReader
from selenium.common.exceptions import TimeoutException
import logging
import utilities.custom_logger as cl


class WebDriverFactory:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, browser):
        """
        Init WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        self.conf = ConfigReader("config.yaml")

    def get_web_driver_instance(self):
        try:
            """
           Get WebDriver Instance based on the browser configuration
    
            Returns:
                'WebDriver Instance'
            """
            base_url = self.conf.get_url()
            if self.browser == "ie":
                # Set ie driver
                ie_driver = "D:\\Selenium\\IEDriverServer.exe"
                os.environ["webdriver.ie.driver"] = ie_driver
                driver = webdriver.Ie(ie_driver)
            elif self.browser == "firefox":
                # Set firefox driver
                driver = webdriver.Firefox()
            else:
                chromedriver = "D:\\Selenium\\chromedriver.exe"
                os.environ["webdriver.chrome.driver"] = chromedriver
                driver = webdriver.Chrome(chromedriver)
                driver.set_window_size(1440, 900)

            # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(10)
            # Maximize the window
            driver.maximize_window()
            # Sets page timeout
            driver.set_page_load_timeout(30)
            # Loading browser with App URL
            driver.get(base_url)
            return driver
        except TimeoutException as te:
            self.log.info("Unable to load page" + str(te))
        except Exception as e:
            self.log.info("Something went wrong while loading page " + str(e))



