import os
import time
import unittest
from selenium import webdriver

from pages.add_player_page import AddPlayerPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_title_page()
        dashboard_page.add_player()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.check_title_of_page()

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
