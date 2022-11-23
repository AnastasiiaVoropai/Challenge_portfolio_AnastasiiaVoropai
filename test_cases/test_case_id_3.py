import os
import time
import unittest
from selenium import webdriver

from pages.add_player_page import AddPlayerPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestCaseId3(unittest.TestCase):

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

    def test_case_id_3(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.assert_element_text(driver=self.driver,
                                       xpath=LoginPage.scout_panel_text_xpath,
                                       expected_text="Scouts Panel")
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.change_language()
        dashboard_page.check_language()
        self.driver.save_screenshot("../screenshots/test_case_id_3.png")





