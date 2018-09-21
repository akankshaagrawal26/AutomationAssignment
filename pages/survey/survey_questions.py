"""
SurveyQuestions class implementation
It defines questions for the survey
"""


from base.base_page import BasePage
import logging
import utilities.custom_logger as cl
from base.config_reader import ConfigReader
import time


class SurveyQuestions(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """
        Init SurveyQuestions class
        :param driver

        """
        super().__init__(driver)
        self.driver = driver
        self.conf = ConfigReader("config.yaml")

    # Locators

    _click_new_question = "//a[contains(@class,'main-add-question-cta wds-button')]"
    _enter_question = "editTitle"
    _click_question_type = "changeQType"
    _click_type_option = "//div[@id='editQuestion']//select[@id='answerBankCategorySelect']"
    _save_question = "//div[@id='editQuestion']//section[@class='t1']//a[contains(@class,'save')]"
    _cancel_question = "//div[@id='editQuestion']//section[@class='t1']//a[contains(@class,'cancel')]"

    _time_option_untick = "//table[@id='rows']//label[contains(text(),'Time Info')]"
    _click_builder = "//li[@title='Builder']"
    _drop_element = "//div[contains(@class,'add-question-btn')]"
    _drag_element_checkboxes = "//div[@id='builderQuestionContainer']//li[2]"
    _drag_element_multiplechoice = "//div[@id='builderQuestionContainer']//li[1]"
    _drag_element_dropdown = "//div[@id='builderQuestionContainer']//li[4]"

    _que2_option_value1 = "Regularly"
    _que2_option_value2 = "Sometimes"
    _que2_option_value3 = "Never Tried"

    _que6_option_value1 = "Question Bank"
    _que6_option_type1 = "//table[@id='rows']/tbody/tr[4]/td[2]/div/div[1]"
    _que6_option_value2 = "Themes"
    _que6_option_type2 = "//table[@id='rows']/tbody/tr[5]/td[2]/div/div[1]"
    _que6_option_value3 = "Graphical Result"
    _que6_option_type3 = "//table[@id='rows']/tbody/tr[6]/td[2]/div/div[1]"
    _que6_option_value4 = "Template Re-usability"
    _que6_option_type4 = "//table[@id='rows']/tbody/tr[7]/td[2]/div/div[1]"
    _que6_option_value5 = "Collectors"
    _que6_option_type5 = "//table[@id='rows']/tbody/tr[8]/td[2]/div/div[1]"

    _que7_option_value1 = "Service"
    _que7_option_type1 = "//div[@id='rowsWrap']//table/tbody/tr[3]/td[1]/div/div[1]"
    _que7_option_value2 = "Support"
    _que7_option_type2 = "//div[@id='rowsWrap']//table/tbody/tr[4]/td[1]/div/div[1]"
    _que7_option_value3 = "Responsiveness"
    _que7_option_type3 = "//div[@id='rowsWrap']//table/tbody/tr[5]/td[1]/div/div[1]"
    _que7_option_value4 = "Very Good"
    _que7_option_type4 = "//div[@id='columnsWrap']//table/tbody/tr[2]/td[1]/div/div[1]"
    _que7_option_value5 = "Good"
    _que7_option_type5 = "//div[@id='columnsWrap']//table/tbody/tr[3]/td[1]/div/div[1]"
    _que7_option_value6 = "Average"
    _que7_option_type6 = "//div[@id='columnsWrap']//table/tbody/tr[4]/td[1]/div/div[1]"
    _que7_option_value7 = "Below Average"
    _que7_option_type7 = "//div[@id='columnsWrap']//table/tbody/tr[5]/td[1]/div/div[1]"
    _del_column = "//div[@id='columnsWrap']//table/tbody/tr[6]/td[3]/a[2]/span"

    _que8_option_value1 = "Question Bank"
    _que8_option_type1 = "//table[@id='rows']/tbody/tr[3]/td[1]/div[1]/div[1]"
    _que8_option_value2 = "Themes"
    _que8_option_type2 = "//table[@id='rows']/tbody/tr[4]/td[1]/div[1]/div[1]"
    _que8_option_value3 = "Graphical Result"
    _que8_option_type3 = "//table[@id='rows']/tbody/tr[5]/td[1]/div[1]/div[1]"
    _que8_option_value4 = "Template Re-usability"
    _que8_option_type4 = "//table[@id='rows']/tbody/tr[6]/td[1]/div[1]/div[1]"
    _que8_option_value5 = "Collectors"
    _que8_option_type5 = "//table[@id='rows']/tbody/tr[7]/td[1]/div[1]/div[1]"

    def click_new_question(self):
        self.element_click(self._click_new_question, locator_type="xpath")

    def enter_question(self, question_no):
        qs = self.conf.get_question(question_no)
        self.wait_for_element(self._enter_question)
        self.send_keys(qs, locator=self._enter_question)

    def click_question_type(self):
        self.element_click(self._click_question_type)

    def select_question_type(self, question_type):
        qs_type = self.conf.get_question_type(question_type)
        self.wait_for_element("//a[contains(text(),'" + qs_type + "')]", locator_type="xpath")
        self.element_click("//a[contains(text(),'" + qs_type + "')]", locator_type="xpath")

    def save_question(self):
        self.wait_for_element(self._save_question, locator_type="xpath")
        self.element_click(self._save_question, locator_type="xpath")

    def cancel_question(self):
        self.wait_for_element(self._cancel_question, locator_type="xpath")
        self.element_click(self._cancel_question, locator_type="xpath")

    def set_question1(self):
        self.log.info("Adding question 1")
        self.enter_question("Que1")
        self.click_question_type()
        self.select_question_type("Type1")
        time.sleep(2)
        self.save_question()

    def set_question2(self):
        self.log.info("Adding question 2")
        self.element_click(self._click_builder, locator_type="xpath")
        time.sleep(1)
        self.drag_n_drop(self._drag_element_multiplechoice, drop=self._drop_element)
        time.sleep(2)
        self.enter_question("Que2")
        self.send_keys(self._que2_option_value1, locator=self._que6_option_type1, locator_type="xpath")
        self.send_keys(self._que2_option_value2, locator=self._que6_option_type2, locator_type="xpath")
        self.send_keys(self._que2_option_value3, locator=self._que6_option_type3, locator_type="xpath")
        time.sleep(2)
        self.save_question()

    def set_question3(self):
        self.log.info("Adding question 3")
        self.element_click(self._click_new_question, locator_type="xpath")
        self.enter_question("Que3")
        self.click_question_type()
        self.select_question_type("Type3")
        self.element_click(self._time_option_untick, locator_type="xpath")
        time.sleep(2)
        self.save_question()

    def set_question4(self):
        self.log.info("Adding question 4")
        self.element_click(self._click_new_question, locator_type="xpath")
        time.sleep(1)
        self.enter_question("Que4")
        self.click_question_type()
        self.select_question_type("Type4")
        time.sleep(2)
        self.save_question()

    def set_question5(self):
        self.log.info("Adding question 5")
        self.element_click(self._click_builder, locator_type="xpath")
        self.wait_for_element(self._drag_element_dropdown, locator_type="xpath")
        self.drag_n_drop(self._drag_element_dropdown, drop=self._drop_element)
        time.sleep(2)
        self.enter_question("Que5")
        element = self.get_element(self._click_type_option, locator_type="xpath")
        time.sleep(1)
        self.drop_down(element, data="Yes - No", select_type="visible text")
        time.sleep(2)
        self.save_question()

    def set_question6(self):
        self.log.info("Adding question 6")
        self.element_click(self._click_builder, locator_type="xpath")
        self.wait_for_element(self._drag_element_checkboxes, locator_type="xpath")
        self.drag_n_drop(self._drag_element_checkboxes, drop=self._drop_element)
        self.enter_question("Que6")
        self.send_keys(self._que6_option_value1, locator=self._que6_option_type1, locator_type="xpath")
        self.send_keys(self._que6_option_value2, locator=self._que6_option_type2, locator_type="xpath")
        self.send_keys(self._que6_option_value3, locator=self._que6_option_type3, locator_type="xpath")
        self.send_keys(self._que6_option_value4, locator=self._que6_option_type4, locator_type="xpath")
        self.send_keys(self._que6_option_value5, locator=self._que6_option_type5, locator_type="xpath")
        time.sleep(2)
        self.save_question()

    def set_question7(self):
        self.log.info("Adding question 7")
        self.element_click(self._click_new_question, locator_type="xpath")
        self.enter_question("Que7")
        self.click_question_type()
        self.select_question_type("Type7")
        self.send_keys(self._que7_option_value1, locator=self._que7_option_type1, locator_type="xpath")
        self.send_keys(self._que7_option_value2, locator=self._que7_option_type2, locator_type="xpath")
        self.send_keys(self._que7_option_value3, locator=self._que7_option_type3, locator_type="xpath")
        self.send_keys(self._que7_option_value4, locator=self._que7_option_type4, locator_type="xpath")
        self.send_keys(self._que7_option_value5, locator=self._que7_option_type5, locator_type="xpath")
        self.send_keys(self._que7_option_value6, locator=self._que7_option_type6, locator_type="xpath")
        self.send_keys(self._que7_option_value7, locator=self._que7_option_type7, locator_type="xpath")
        time.sleep(1)
        self.element_click(self._del_column,locator_type="xpath")
        time.sleep(2)
        self.save_question()

    def set_question8(self):
        self.log.info("Adding question 8")
        self.element_click(self._click_new_question, locator_type="xpath")
        self.enter_question("Que8")
        self.click_question_type()
        self.select_question_type("Type8")
        self.send_keys(self._que8_option_value1, locator=self._que8_option_type1, locator_type="xpath")
        self.send_keys(self._que8_option_value2, locator=self._que8_option_type2, locator_type="xpath")
        self.send_keys(self._que8_option_value3, locator=self._que8_option_type3, locator_type="xpath")
        self.send_keys(self._que8_option_value4, locator=self._que8_option_type4, locator_type="xpath")
        self.send_keys(self._que8_option_value5, locator=self._que8_option_type5, locator_type="xpath")
        time.sleep(2)
        self.save_question()

    def set_question9(self):
        self.log.info("Adding question 9")
        self.element_click(self._click_builder, locator_type="xpath")
        self.wait_for_element(self._drag_element_multiplechoice, locator_type="xpath")
        self.drag_n_drop(self._drag_element_multiplechoice, drop=self._drop_element)
        time.sleep(2)
        self.enter_question("Que9")
        element = self.get_element(self._click_type_option, locator_type="xpath")
        time.sleep(1)
        self.drop_down(element, data="Yes - No", select_type="visible text")
        time.sleep(2)
        self.save_question()

    def set_question10(self):
        self.log.info("Adding question 10")
        self.element_click(self._click_new_question, locator_type="xpath")
        self.enter_question("Que10")
        self.click_question_type()
        self.select_question_type("Type10")
        time.sleep(2)
        self.save_question()

    def verify_question_added_successfully(self, question, ques_type):
        try:
            self.log.info("In verify_question_added_successfully :: " + question + " :: " + ques_type)
            time.sleep(5)
            element_into_view = self.get_element("//h4[@class='question-title-container']//span[contains(text(),'"
                                                 + question + "')]", locator_type="xpath")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element_into_view)
            time.sleep(1)
            self.driver.execute_script("window.scrollBy(0, -200);")
            self.element_click(element=element_into_view)
            self.wait_for_element("//a[@id='changeQType']//span[contains(text(),'" + ques_type + "')]",
                                  locator_type="xpath")
            result = self.is_element_present(locator="//a[@id='changeQType']//span[contains(text(),'" + ques_type +
                                                     "')]", locator_type="xpath")
            time.sleep(2)
            self.cancel_question()
            time.sleep(3)
            return result
        except Exception as e:
            self.log.info("Exception while verifying question::", e)
            return False

    def check_question_added(self, question, question_type):
        ques = self.conf.get_question(question)
        ques_type = self.conf.get_question_type(question_type)
        return self.verify_question_added_successfully(ques, ques_type)

