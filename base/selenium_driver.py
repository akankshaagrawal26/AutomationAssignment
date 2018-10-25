"""
@package base

SeleniumDriver Factory class implementation

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os
import pytest


class SeleniumDriver:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """
        Init SeleniumDriver
        :param driver:
        """
        self.driver = driver

    def screen_shot(self, result_message):
        """

        Takes screenshot of the current open web page
        :param result_message: Name of screenshot

        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "..\\screenshots\\"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory:: " + destination_file)
        except Exception as e:
            self.log.info("Exception occurred when taking screenshot", e)

    def allure_attach_screenshot(self, name):
        """
        Attach a screenshot
        :param name: Name to be appeared on the report under which screenshot will be shown.
        """
        name = str(name)
        pytest.allure.attach(self.driver.get_screenshot_as_png(), name, attachment_type=pytest.allure.attachment_type.PNG)

    def get_title(self):
        """

        :return: Title of the web page
        """
        return self.driver.title

    def get_by_type(self, locator_type):
        """
        Gets the type of the locator
        :param locator_type: Type of locator
        :return: Type of the locator
        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type +
                          " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        """
        Get element
        :param locator: Value of locator
        :param locator_type: Type of locator
        :return: element found with the given locator and locator type
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        Get list of elements
        :param locator: Value of locator
        :param locator_type: Type of locator
        :return: Elements found with the given locator and locator type
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locator_type: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and locator_type: " + locator_type)
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        """
        Click on an element
        :param locator: Value of locator
        :param locator_type: Type of locator
        :param element :Element value

        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locator_type: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locator_type: " + locator_type)

    def send_keys(self, data, locator="", locator_type="id", element=None):
        """
        Send keys to an element
        :param data : Data to be send to an element
        :param locator: Value of locator
        :param locator_type: Type of locator
        :param element :Element value
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data to the element with locator: " + locator +
                          " locator_type: " + locator_type)
        except:
            self.log.info("Cannot send data to the element with locator: " + locator + " locator_type: " + locator_type)

    def clear_field(self, locator="", locator_type="id"):
        """
        Clear an element field
        :param locator: Value of locator
        :param locator_type: Type of locator
        """
        element = self.get_element(locator, locator_type)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locator_type: " + locator_type)

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """
        Get 'Text' on an element
        :param locator: Value of locator
        :param locator_type: Type of locator
        :param element :Element value
        :param info: Element info
        :return: Text on the element
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.info("Failed to get text on element " + info)
            text = None
        return text

    def is_element_present(self, locator="", locator_type="id", element=None):
        """
        Check if element is present
        :param locator: Value of locator
        :param locator_type: Type of locator
        :param element :Element value
        return: Boolean value
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locator_type: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locator_type: " + locator_type)
                return False
        except Exception as e:
            self.log.info("Element not found", e)
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """

        Check if element is displayed
        :param locator: Value of locator
        :param locator_type: Type of locator
        :param element :Element value
        return: Boolean value
        """
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return is_displayed
        except Exception as e:
            self.log.info("Element not found" + e)
            return False

    def element_presence_check(self, locator, by_type):
        """
        Check if element is present
        :param locator: Value of locator
        :param by_type: Type of locator
        return: Boolean value
        """
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(by_type))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(by_type))
                return False
        except Exception as e:
            self.log.info("Element not found" + e)
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=60, poll_frequency=0.5):
        """
        Wait for the element to appear
        :param locator: Value of locator
        :param locator_type: Type of locator
        :param timeout: Max time to wait
        :param poll_frequency: Time to check after how many seconds
        :return: Element found
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + ":: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except Exception as e:
            self.log.info("Element not appeared on the web page" + e)
        return element

    def web_scroll(self, direction="up"):
        """
        Scroll page
        :param direction: Direction in which to scroll

        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def drop_down(self, element, data, select_type="index"):
        """
        To select element in dropdown
        :param element:
        :param data: Value by which element to be selected
        :param select_type: Type by which element to be selected
        """
        try:
            sel = Select(element)
            if select_type == "index":
                sel.select_by_index(data)
            elif select_type == "value":
                sel.select_by_value(data)
            elif select_type == "visible text":
                sel.select_by_visible_text(data)
            else:
                self.log.info("Select Type " + select_type + "not correct/supported")
            self.log.info("Selected element with select type: " + select_type)
        except:
            self.log.info("Cannot select the element with select type: " + select_type)

    def drag_n_drop(self, drag, drop):
        """
        To drag and drop the element
        :param drag: Element to be dragged
        :param drop: Element where to be dropped

        """
        try:
            source = self.get_element(drag, locator_type="xpath")
            destination = self.get_element(drop, locator_type="xpath")
            actions = ActionChains(self.driver)
            actions.click_and_hold(source).move_to_element(destination).release().perform()
            self.log.info("Element dragged and dropped")
        except Exception as e:
            self.log.info("Unable to Drag and drop", e)

