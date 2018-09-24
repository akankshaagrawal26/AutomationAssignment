"""
Login Page class implementation
It defines necessary login actions

"""

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
import logging
import time


class LoginPage(SeleniumDriver):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """
        Init LoginPage class
        :param driver:

        """

        self.driver = driver
        super(LoginPage, self).__init__(driver)

    # Locators
    _login_link = "//div[contains(@class,'inner-header-top')]//a[contains(@class,'log-in')]"
    _username_field = "username"
    _password_field = "password"
    _login_button = "//div[contains(@class,'input-list-item')]//button[@type='submit']"
    _login_success = "userAcctTab_MainMenu"
    _login_fail = "//div[contains(@class,'account-header')]//h1[contains(@class,'page-title')]"
    _logout = "//li[@id='dd-my-account']//a[contains(@href,'/user/sign-out/')]"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type="xpath")

    def enter_username(self, username):
        self.send_keys(username, self._username_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="xpath")

    def login(self, username="", password=""):
        self.click_login_link()
        self.clear_fields()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        login_link_element = self.wait_for_element(self._login_success)
        result = self.is_element_present(element=login_link_element)
        return result

    def verify_login_failed(self):
        result = self.is_element_present(self._login_fail, locator_type="xpath")
        return result

    def logout(self):
        self.element_click(locator=self._login_success)
        logout_link_element = self.wait_for_element(self._logout, locator_type="xpath")
        time.sleep(2)
        self.element_click(element=logout_link_element)

    def clear_fields(self):
        username = self.get_element(locator=self._username_field)
        username.clear()
        password = self.get_element(locator=self._password_field)
        password.clear()


