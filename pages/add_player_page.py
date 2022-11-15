import time

from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"

    def check_title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title