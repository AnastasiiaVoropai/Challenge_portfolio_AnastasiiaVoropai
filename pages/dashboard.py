import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "//ul[1]/div[1]/div[2]/span"
    players_xpath = "//ul[1]/div[2]/div[2]/span"
    language_selector_xpath = "//ul[2]/div[1]/div[2]/span"
    sign_out_xpath = "//ul[2]/div[2]/div[2]/span"
    players_count_xpath = "//div[2]/div[1]/div/div[1]"
    players_count_number_xpath = "//div[2]/div[1]/div/div[2]/b"
    reports_count_xpath = "//div[2]/div[3]/div/div[1]"
    reports_count_number_xpath = "//div[3]/div/div[2]/b"
    matches_count_xpath = "//div[2]/div[2]/div/div[1]"
    matches_count_number_xpath = "//div[2]/div/div[2]/b"
    events_count_xpath = "//div[4]/div/div[1]"
    events_count_number_xpath = "//div[4]/div/div[2]/b"
    logo_scouts_panel_xpath = "//div[3]/div[1]/div/div[1]"
    name_scouts_panel_xpath = "//div[1]/div/div[2]/h2"
    button_dev_team_contact_xpath = "//div[1]/div/div[3]/a/span[1]"
    shortcuts_xpath = "//div[2]/div/div/h2"
    button_add_player_xpath = "//div[2]/div/div/a/button/span[1]"
    activity_xpath = "//div[3]/div/div/h2"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts.futbolkolektyw.pl/en/"
    language_expected_text = "English"
    #wait = WebDriverWait(driver, 10)


    def check_title_page(self):
        self.wait_for_element_to_be_clickable(self.button_add_player_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def add_player(self):
        self.click_on_the_element(self.button_add_player_xpath)

    def change_language(self):
        self.click_on_the_element(self.language_selector_xpath)

    def check_language(self):
        language_element: WebElement = self.driver.find_element(By.XPATH, self.language_selector_xpath)
        assert language_element.text == self.language_expected_text