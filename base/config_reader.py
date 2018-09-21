"""
@package base

ConfigReader class implementation
Returns config.yaml file data

"""
import yaml
import os
from os import path
import logging
import utilities.custom_logger as cl


class ConfigReader:
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, file_name):
        """

        Init ConfigReader class
        * :param file_name: name of file
        * :param self :current instance of class

        """

        relative_file_name = "..\\configuration\\" + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        self.file = destination_file

    def read_file(self):
        """

        Reads complete config.yaml file and stores data in form of dictionary

        * :param self: current instance of class
        * :return: file_data in dictionary format

        """

        try:
            if path.exists(self.file):
                reader = open(self.file, "r")
                file_data = yaml.load(reader)
                return file_data
            else:
                self.log.info("File does not exist")
        except Exception as e:
            self.log.info("Problem in reading file", e)
        finally:
            reader.close()

    def get_browser(self):
        """

        Get browser from config file

        * :param self: current instance of class
        * :return: broswer

        """
        try:
            fetch_data = self.read_file()
            browser = fetch_data['platfrom']['browser']
            self.log.info("Browser ::" + browser)
            return browser
        except Exception as e:
            self.log.info("Problem in getting browser value", e)

    def get_url(self):
        """

         Get url from config file
        * :param self: current instance of class
        * :return: url

        """
        try:
            fetch_data = self.read_file()
            url = fetch_data['siteconfiguration']['url']
            self.log.info("URL ::" + url)
            return url
        except Exception as e:
            self.log.info("Problem in getting url value", e)

    def get_survey_title(self):
        """

         Get survey title from config file
        * :param self: current instance of class
        * :return: survey title

        """
        try:
            fetch_data = self.read_file()
            survey_title = fetch_data['surveyConfig']['survey_title']
            self.log.info("Survey Title ::" + survey_title)
            return survey_title
        except Exception as e:
            self.log.info("Problem in getting survey title", e)

    def get_survey_title_new(self):
        """

         Get modified survey title from config file
        * :param self: current instance of class
        * :return: changed survey title

        """
        try:
            fetch_data = self.read_file()
            survey_title_new = fetch_data['surveyConfig']['survey_title_new']
            self.log.info("Modified Survey Title ::" + survey_title_new)
            return survey_title_new
        except Exception as e:
            self.log.info("Problem in getting modified survey title", e)

    def get_page_title(self):
        """

         Get page title from config file
        * :param self: current instance of class
        * :return: page title

        """
        try:
            fetch_data = self.read_file()
            page_title = fetch_data['surveyConfig']['page_title']
            self.log.info("Page Title ::" + page_title)
            return page_title
        except Exception as e:
            self.log.info("Problem in getting page title", e)

    def get_question(self, question_no):
        """

        Get question from config file

        * :param self: current instance of class
        * :param question_no
        * :return: question

        """
        try:
            fetch_data = self.read_file()
            question = fetch_data['Questions'][question_no]
            self.log.info("Question ::" + question)
            return question
        except Exception as e:
            self.log.info("Problem in getting question", e)

    def get_question_type(self, que_type):
        """

        Get question type from config file

        * :param self: current instance of class
        * :param type: Question Type
        * :return: type

        """
        try:
            fetch_data = self.read_file()
            question_type = fetch_data['Questions'][que_type]
            self.log.info("Question Type ::" + question_type)
            return question_type
        except Exception as e:
            self.log.info("Problem in getting question type", e)
