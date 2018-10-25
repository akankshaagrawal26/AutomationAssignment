"""

Create Survey Tests class implementation
Tests for Create survey page

"""


from pages.survey.create_survey import CreateSurvey
import unittest
import pytest
import utilities.custom_logger as cl
from utilities.teststatus import TestStatus
import logging
from base.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("get_login")
class CreateSurveyTests(unittest.TestCase):

    log = cl.custom_logger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        """
        Method for initializing object
        """
        self.cs = CreateSurvey(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SeleniumDriver(self.driver)    # for using allure_attach_screenshot() method

    @pytest.mark.run(order=3)
    def test_create_survey(self):
        """

        Function to test survey created successfully or not
        """
        try:
            self.log.info("In test_create_survey")
            self.cs.create_survey()
            result = self.cs.verify_create_survey()
            self.sd.allure_attach_screenshot(name='SCREENSHOTS')       # For taking screenshots with allure
            self.log.info("Survey created ::" + str(result))
            self.ts.mark_final("test_create_survey", result, "Survey created Verification")
        except Exception as e:
            self.log.info("Exception in test_create_survey", e)


