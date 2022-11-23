import os
import time
import unittest
from selenium import webdriver

from pages.add_player_page import AddPlayerPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestCaseId2(unittest.TestCase):

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

    def test_case_id_2(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.assert_element_text(driver=self.driver,
                                       xpath=LoginPage.scout_panel_text_xpath,
                                       expected_text="Scouts Panel")
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-4321')
        user_login.click_on_the_sign_in_button()
        user_login.wait_visibility_of_element_located(LoginPage.identifier_or_password_invalid_xpath)
        self.driver.save_screenshot("../screenshots/test_case_id_2.png")



