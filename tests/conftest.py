import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
from pages.survey.create_survey import CreateSurvey
import logging
import utilities.custom_logger as cl

log = cl.custom_logger(logging.DEBUG)


@pytest.yield_fixture(scope="class")
def get_login(request, browser):
    log.info("Running get login one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login("akanksha.agrawal", "password@123")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.close()
    log.info("Running get login one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.yield_fixture(scope="class")
def get_survey(request, browser):
    log.info("Running get survey one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login("akanksha.agrawal", "password@123")
    cs = CreateSurvey(driver)
    cs.create_survey()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.close()
    log.info("Running get survey one time tearDown")