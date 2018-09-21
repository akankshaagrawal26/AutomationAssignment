import unittest
from tests.home.login_tests import LoginTests
from tests.survey.create_survey_tests import CreateSurveyTests
from tests.survey.survey_operations_tests import SurveyOperationsTests


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CreateSurveyTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(SurveyOperationsTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
