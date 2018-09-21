"""
Survey Operations class implementation
It defines necessary survey actions
"""


from base.base_page import BasePage
import logging
import utilities.custom_logger as cl
from base.config_reader import ConfigReader
import time


class SurveyOperations(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """
        Init SurveyOperations class
        :param driver

        """
        super().__init__(driver)
        self.driver = driver
        self.conf = ConfigReader("config.yaml")

    # Locators

    _logo_popup = "//div[@id='suggested-design-dialog']//a[contains(text(),'REMOVE')]"
    _click_survey_title = "//div[contains(@class,'has-survey-title')]"
    _survey_title = "surveyTitle"
    _save_survey_title = "//form[@id='surveyTitleForm']//a[contains(@class,'save')]"
    _check_survey_title = "//h2[contains(@class,'notranslate')]"
    _click_page_title = "//div[contains(@class,'page-title-container clearfix')]"
    _page_title = "pageTitle"
    _save_page_title = "//form[@id='pageTitleForm']//a[contains(@class,'save')]"
    _check_page_title = "//span[contains(@class,'page-title user-generated')]"

    def remove_logo_popup(self):
        try:
            if self.get_element(self._logo_popup, locator_type="xpath") is not None:
                return True
            else:
                return False
        except Exception as e:
            self.log.info("Exception while checking logo", e)
            return False

    def click_remove(self):
        self.element_click(self._logo_popup, locator_type="xpath")

    def check_popup(self):
        if self.remove_logo_popup():
            self.click_remove()

    def click_survey_title(self):
        self.wait_for_element(self._click_survey_title, locator_type="xpath")
        self.element_click(self._click_survey_title, locator_type="xpath")

    def enter_survey_title(self,title):
        self.clear_field(self._survey_title)
        self.send_keys(title, self._survey_title)

    def save_survey_title(self):
        self.element_click(self._save_survey_title, locator_type="xpath")

    def click_page_title(self):
        self.element_click(self._click_page_title, locator_type="xpath")

    def enter_page_title(self, page_title):
        self.clear_field(self._page_title)
        self.send_keys(page_title, self._page_title)

    def save_page_title(self):
        self.element_click(self._save_page_title, locator_type="xpath")

    def edit_survey_title(self):
        new_title = self.conf.get_survey_title_new()
        self.check_popup()
        time.sleep(5)
        self.click_survey_title()
        self.enter_survey_title(new_title)
        time.sleep(1)
        self.save_survey_title()

    def add_page_title(self):
        time.sleep(2)
        page_title = self.conf.get_page_title()
        self.click_page_title()
        self.enter_page_title(page_title)
        time.sleep(1)
        self.save_page_title()

    def verify_page_title_added(self):
        time.sleep(1)
        page_title = self.get_text(self._check_page_title, locator_type="xpath", info="Page Title")
        return page_title

    def verify_survey_title_edited(self):
        time.sleep(1)
        survey_title = self.get_text(self._check_survey_title, locator_type="xpath", info="Survey Title")
        return survey_title

