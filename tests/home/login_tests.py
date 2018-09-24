"""

Login Tests class implementation
Tests for login page

"""

from pages.home.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from utilities.read_data import get_csv_data
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("get_login")
@ddt
class LoginTests(unittest.TestCase):
    log = cl.custom_logger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        """
        Method for initializing object
        """
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    @data(*get_csv_data("D:\\workspace\\AutomationAssignment\\configuration\\LoginData.csv"))
    @unpack
    def test_valid_login(self, username, password):
        """
        Function to test valid login
        :param username: Takes username for login
        :param password: Takes password for login

        """
        try:
            self.log.info("In test_valid_login")
            self.lp.login(username, password=password)
            result = self.lp.verify_login_successful()
            self.log.info("Successfully logged in ::" + str(result))
            self.ts.mark_final("test_valid_login", result, "Valid Login Verification")
        except Exception as e:
            self.log.info("Exception in test_valid_login", e)

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        """

        Function to test invalid login

        """
        try:
            self.log.info("In test_invalid_login")
            self.lp.logout()
            self.lp.login("akanksha.agrawal", "pass@123")
            result = self.lp.verify_login_failed()
            self.log.info("Login failed ::" + str(result))
            self.ts.mark_final("test_invalid_login", result, "Invalid Login Verification")
        except Exception as e:
            self.log.info("Exception in test_invalid_login", e)


