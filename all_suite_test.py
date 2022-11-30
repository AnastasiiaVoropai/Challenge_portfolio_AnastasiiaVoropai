import unittest
from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.test_add_a_player import TestAddPlayer
from test_cases.test_case_id_1 import TestCaseId1
from test_cases.test_case_id_2 import TestCaseId2
from test_cases.test_case_id_3 import TestCaseId3
from test_cases.test_case_id_4 import TestCaseId4
from test_cases.test_case_id_5 import TestCaseId5


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestCaseId1))
   test_suite.addTest(makeSuite(TestCaseId2))
   test_suite.addTest(makeSuite(TestCaseId3))
   test_suite.addTest(makeSuite(TestCaseId4))
   test_suite.addTest(makeSuite(TestCaseId5))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())