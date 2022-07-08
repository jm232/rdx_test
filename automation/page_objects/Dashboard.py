from selenium.webdriver.common.by import By

from automation.utilities.ui_utilities import *


class Dashboard:

    BUTTON_HOME = (By.XPATH, "//a[text()='Simple Application']")
    BUTTON_LIST_MOVIES = (By.XPATH, "//a[text()='List Movies']")
    BUTTON_CREATE_MOVIE = (By.XPATH, "//a[text()='Create Movie']")

    def __init__(self, driver):
        self.driver = driver

    def page_loaded(self):
        wait_until_element_is_visible(self.driver, Dashboard.BUTTON_HOME)
        wait_until_element_is_visible(self.driver, Dashboard.BUTTON_CREATE_MOVIE)
        wait_until_element_is_visible(self.driver, Dashboard.BUTTON_LIST_MOVIES)

    def click_on_home_button(self):
        wait_until_element_is_visible(self.driver, Dashboard.BUTTON_HOME)
        click_element(self.driver, Dashboard.BUTTON_HOME)

    def click_on_create_movie_button(self):
        wait_until_element_is_visible(self.driver, Dashboard.BUTTON_CREATE_MOVIE)
        click_element(self.driver, Dashboard.BUTTON_CREATE_MOVIE)

    def click_on_list_movies_button(self):
        wait_until_element_is_visible(self.driver, Dashboard.BUTTON_LIST_MOVIES)
        click_element(self.driver, Dashboard.BUTTON_LIST_MOVIES)