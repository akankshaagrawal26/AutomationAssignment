"""

Survey Operations Tests class implementation
Tests for survey operation page

"""

from pages.survey.survey_operations import SurveyOperations
from pages.survey.survey_questions import SurveyQuestions
import unittest
import pytest
import utilities.custom_logger as cl
from base.config_reader import ConfigReader
from utilities.teststatus import TestStatus
import logging


@pytest.mark.usefixtures("get_survey")
class SurveyOperationsTests(unittest.TestCase):

    log = cl.custom_logger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        """
        Method for initializing object
        """
        self.so = SurveyOperations(self.driver)
        self.sq = SurveyQuestions(self.driver)
        self.ts = TestStatus(self.driver)
        self.config = ConfigReader("config.yaml")

    @pytest.mark.run(order=4)
    # def test_change_survey_title(self):
    #     """
    #
    #     Function to test survey title changed or not
    #     """
    #     try:
    #         self.log.info("In test_change_survey_title")
    #         self.so.edit_survey_title()
    #         result = self.so.verify_survey_title_edited()
    #         self.log.info("Edited title received ::" + result)
    #         self.ts.mark_final("test_change_survey_title", result, "Title Change Verification")
    #     except Exception as e:
    #         self.log.info("Exception in test_change_survey_title", e)
    #
    # @pytest.mark.run(order=5)
    # def test_add_page_title(self):
    #     """
    #
    #     Function to test page title added or not
    #     """
    #     try:
    #         self.log.info("In test_add_page_title")
    #         self.so.add_page_title()
    #         result = self.so.verify_page_title_added()
    #         self.log.info("Page title received ::" + result)
    #         self.ts.mark_final("test_add_page_title", result, "Add Page Verification")
    #     except Exception as e:
    #         self.log.info("Exception in test_change_survey_title", e)
    #
    @pytest.mark.run(order=6)
    def test_verify_question1_added(self):
        """
        Function to verify question1 added or not

        """
        try:
            self.log.info("In test_verify_question1_added")
            self.sq.set_question1()
            result = self.sq.check_question_added("Que1", question_type="Type1")
            self.log.info("Question1 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question1_added", result, "Question1 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question1" + str(e))

    @pytest.mark.run(order=7)
    def test_verify_question2_added(self):
        """
        Function to verify question2 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question2_added")
            self.sq.set_question2()
            result = self.sq.check_question_added("Que2", question_type="Type2")
            self.log.info("Question2 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question2_added", result, "Question2 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question2" + str(e))

    @pytest.mark.run(order=8)
    def test_verify_question3_added(self):
        """
        Function to verify question3 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question3_added")
            self.sq.set_question3()
            result = self.sq.check_question_added("Que3", question_type="Type3")
            self.log.info("Question3 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question3_added", result, "Question3 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question3" + str(e))

    @pytest.mark.run(order=9)
    def test_verify_question4_added(self):
        """
        Function to verify question4 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question4_added")
            self.sq.set_question4()
            result = self.sq.check_question_added("Que4", question_type="Type4")
            self.log.info("Question4 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question4_added", result, "Question4 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question4" + str(e))

    @pytest.mark.run(order=10)
    def test_verify_question5_added(self):
        """
        Function to verify question5 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question5_added")
            self.sq.set_question5()
            result = self.sq.check_question_added("Que5", question_type="Type5")
            self.log.info("Question5 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question5_added", result, "Question5 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question5" + str(e))

    @pytest.mark.run(order=11)
    def test_verify_question6_added(self):
        """
        Function to verify question6 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question6_added")
            self.sq.set_question6()
            result = self.sq.check_question_added("Que6", question_type="Type6")
            self.log.info("Question6 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question6_added", result, "Question6 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question6" + str(e))

    @pytest.mark.run(order=12)
    def test_verify_question7_added(self):
        """
        Function to verify question7 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question7_added")
            self.sq.set_question7()
            result = self.sq.check_question_added("Que7", question_type="Type7")
            self.log.info("Question7 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question7_added", result, "Question7 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question7" + str(e))

    @pytest.mark.run(order=13)
    def test_verify_question8_added(self):
        """
        Function to verify question8 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question8_added")
            self.sq.set_question8()
            result = self.sq.check_question_added("Que8", question_type="Type8")
            self.log.info("Question8 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question8_added", result, "Question8 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question8" + str(e))

    @pytest.mark.run(order=14)
    def test_verify_question9_added(self):
        """
        Function to verify question9 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question9_added")
            self.sq.set_question9()
            result = self.sq.check_question_added("Que9", question_type="Type9")
            self.log.info("Question9 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question9_added", result, "Question9 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question9" + str(e))

    @pytest.mark.run(order=15)
    def test_verify_question10_added(self):
        """
        Function to verify question10 added or not
        :return:
        """
        try:
            self.log.info("In test_verify_question10_added")
            self.sq.set_question10()
            result = self.sq.check_question_added("Que10", question_type="Type10")
            self.log.info("Question10 verification result ::" + str(result))
            self.ts.mark_final("test_verify_question10_added", result, "Question10 Verification")
        except Exception as e:
            self.log.info("Exception while verifying Question10" + str(e))

