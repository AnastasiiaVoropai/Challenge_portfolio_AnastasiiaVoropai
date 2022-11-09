from pages.base_page import BasePage


class Matchform(BasePage):
    my_team_label_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/label"
    my_team_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    enemy_team_label_xpath = "//*[@id='__next'/div[1]/main/div[2]/form/div[2]/div/div[2]/div/label"
    enemy_team_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    my_team_score_label_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/label"
    my_team_score_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    enemy_team_score_label_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/label"
    enemy_team_score_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    date_label_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/label"
    date_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    match_at_home_radio_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[1]/span[1]/input"
    match_at_home_label_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[2]"
    match_out_home_radio_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]/input"
    match_out_home_label_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[2]"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
