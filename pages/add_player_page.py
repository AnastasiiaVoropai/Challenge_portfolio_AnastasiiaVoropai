import time

from pages.base_page import BasePage


class AddPlayerPage(BasePage):

    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    email_input_xpath = "//div[1]/div/div/input"
    name_input_xpath = "//div[2]/div/div/input"
    surname_input_xpath = "//div[3]/div/div/input"
    phone_input_xpath = "//div[4]/div/div/input"
    weight_input_xpath = "//div[5]/div/div/input"
    age_input_xpath = "//div[7]/div/div/input"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    left_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    right_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    main_position_input_xpath = "//div[11]/div/div/input"
    submit_button_xpath = "//div[3]/button[1]"
    player_added_expected_text = "Added player."
    player_added_contains_xpath = '//*[contains(text(), "' + player_added_expected_text + '")]'
    field_alert_expected_text = "Required"
    field_alert_expected_xpath = '//*[contains(text(), "' + field_alert_expected_text + '")]'
    cannot_add_player_expected_text = "Cannot add player."
    cannot_add_player_contains_xpath = '//*[contains(text(), "' + cannot_add_player_expected_text + '")]'

    def check_title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def select_leg(self, leg_xpath):
        self.click_on_the_element(self.leg_dropdown_xpath)
        self.wait_visibility_of_element_located(leg_xpath)
        self.click_on_the_element(leg_xpath)

    def type_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def type_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def type_email(self, email):
        self.field_send_keys(self.email_input_xpath, email)

    def type_phone(self, phone):
        self.field_send_keys(self.phone_input_xpath, phone)

    def type_weight(self, weight):
        self.field_send_keys(self.weight_input_xpath, weight)

    def type_age(self, age):
        self.field_send_keys(self.age_input_xpath, age)

    def type_main_position(self, main_position):
        self.field_send_keys(self.main_position_input_xpath, main_position)

    def submit(self):
        self.click_on_the_element(self.submit_button_xpath)

    def check_field_alert(self):
        self.wait_visibility_of_element_located(self.field_alert_expected_xpath)

