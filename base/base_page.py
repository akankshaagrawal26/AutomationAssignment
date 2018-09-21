"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

"""
from base.selenium_driver import SeleniumDriver


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class
        """

        super(BasePage, self).__init__(driver)
        self.driver = driver


