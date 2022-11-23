import os
import time
import unittest
from selenium import webdriver

from pages.add_player_page import AddPlayerPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver
from PIL import Image


class TestCaseId1(unittest.TestCase):

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

    def test_case_id_1(self):
        user_login = LoginPage(self.driver)
        user_login.check_title_of_page()
        user_login.assert_element_text(driver=self.driver,
                                       xpath=LoginPage.scout_panel_text_xpath,
                                       expected_text="Scouts Panel")
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_title_page()
        dashboard_page.add_player()

        add_player_page = AddPlayerPage(self.driver)
        add_player_page.type_email("1234@gmail.com")
        add_player_page.type_name("A")
        add_player_page.type_surname("B")
        add_player_page.type_phone("12345678")
        add_player_page.type_weight("800")
        add_player_page.type_age("10102000")
        add_player_page.type_main_position("goalkeeper")
        add_player_page.select_leg(AddPlayerPage.left_leg_xpath)
        add_player_page.submit()
        add_player_page.wait_visibility_of_element_located(AddPlayerPage.player_added_contains_xpath)
        self.driver.save_screenshot("../screenshots/test_case_id_1.png")


