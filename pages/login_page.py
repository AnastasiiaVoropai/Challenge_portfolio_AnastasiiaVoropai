from pages.base_page import BasePage


class LoginPage(BasePage):
    scout_panel_text_xpath = "'//h5'"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@id='password']"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    language_selector_xpath = "//input[@class='MuiSelect-nativeInput']"
    sign_in_button_xpath = "//button[@type='submit']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
