"""
CreateSurvey class implementation
Class to create a survey
"""

from base.base_page import BasePage
import logging
import utilities.custom_logger as cl
from base.config_reader import ConfigReader


class CreateSurvey(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """
        Init CreateSurvey class
        :param driver

        """
        super().__init__(driver)
        self.driver = driver
        self.conf = ConfigReader("config.yaml")

    # Locators
    _create_survey = "//div[@class='actions']//a[contains(@class,'create-survey')]"
    _survey_title = "surveyTitle"
    _click_category_list = "//div[@class='Select-control']//div[@class='Select-placeholder']"
    _survey_category = "react-select-2--option-1"
    _click_create_survey_button = "//button[contains(text(),'CREATE SURVEY')]"
    _click_start_from_scratch = "scratch"
    _create_survey_success = "//div[@class='global-navigation-header-centered']//a[contains(@href,'/create/?sm=')]"

    def click_survey_link(self):
        self.element_click(self._create_survey, locator_type="xpath")

    def click_scratch_link(self):
        scratch_present = self.is_element_present(self._click_start_from_scratch)
        if scratch_present:
            self.element_click(self._click_start_from_scratch)

    def enter_survey_title(self, title):
        self.wait_for_element(self._survey_title)
        self.send_keys(title, locator=self._survey_title)

    def enter_category(self):
        self.element_click(self._click_category_list, locator_type="xpath")
        self.element_click(self._survey_category)

    def click_create_button(self):
        self.wait_for_element(self._click_create_survey_button, locator_type="xpath")
        self.element_click(self._click_create_survey_button, locator_type="xpath")

    def create_survey(self):
        title = self.conf.get_survey_title()
        self.click_survey_link()
        self.click_scratch_link()
        self.enter_survey_title(title)
        self.enter_category()
        self.click_create_button()

    def verify_create_survey(self):
        result = self.is_element_present(self._create_survey_success, locator_type="xpath")
        return result


