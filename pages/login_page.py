import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    scout_panel_text_xpath = "//h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_hyperlink_xpath = "//a"
    language_selector_xpath = "//input[@class='MuiSelect-nativeInput']"
    sign_in_button_xpath = "//button[@type='submit']"
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts.futbolkolektyw.pl/en/"
    identifier_or_password_invalid_xpath = "//div[1]/div[3]/span"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_title_of_page(self):
        self.wait_visibility_of_element_located(self.scout_panel_text_xpath)
        #time.sleep(5)
        #assert self.get_page_title(self.login_url) == self.expected_title

