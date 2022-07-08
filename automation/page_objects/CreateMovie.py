from selenium.webdriver.common.by import By

from automation.utilities.ui_utilities import *

util = Utils()
log = util.getLoggingConfig()

class CreateMovie:

    BUTTON_ADD_MOVIE = (By.XPATH, "//button[text()='Add Movie']")
    BUTTON_UPDATE_MOVIE = (By.XPATH, "//button[text()='Update Movie']")
    BUTTON_CANCEL = (By.XPATH, "//a[text()='Cancel']")
    INPUT_NAME = (By.XPATH, "//label[text()='Name: ']/following-sibling::input")
    INPUT_RATING = (By.XPATH, "//label[text()='Rating: ']/following-sibling::input")
    INPUT_TIME = (By.XPATH, "//label[text()='Time: ']/following-sibling::input")
    #not implemented in simple app, but it should be
    ERROR_ICON = (By.XPATH, "//icon[@id='required_field'][text()='Please fill in required fields']")

    def __init__(self, driver):
        self.driver = driver

    def page_loaded(self):
        wait_until_element_is_visible(self.driver, CreateMovie.BUTTON_ADD_MOVIE)

    def click_on_add_movie_button(self):
        wait_until_element_is_visible(self.driver, CreateMovie.BUTTON_ADD_MOVIE)
        click_element(self.driver, CreateMovie.BUTTON_ADD_MOVIE)
        wait_until_alert_is_present(self.driver)
        obj1 = self.driver.switch_to.alert
        log.info(obj1.text)
        obj1.accept()

    def click_on_add_movie_button_empty_fields(self):
        wait_until_element_is_visible(self.driver, CreateMovie.BUTTON_ADD_MOVIE)
        click_element(self.driver, CreateMovie.BUTTON_ADD_MOVIE)

    def click_on_update_movie_button(self):
        wait_until_element_is_visible(self.driver, CreateMovie.BUTTON_UPDATE_MOVIE)
        click_element(self.driver, CreateMovie.BUTTON_UPDATE_MOVIE)
        wait_until_alert_is_present(self.driver)
        obj1 = self.driver.switch_to.alert
        log.info(obj1.text)
        obj1.accept()

    def click_on_cancel_button(self):
        wait_until_element_is_visible(self.driver, CreateMovie.BUTTON_CANCEL)
        click_element(self.driver, CreateMovie.BUTTON_CANCEL)

    def input_movie_name(self, value):
        wait_until_element_is_visible(self.driver, CreateMovie.INPUT_NAME)
        input_text(self.driver, CreateMovie.INPUT_NAME, value)

    def input_movie_rating(self, value):
        wait_until_element_is_visible(self.driver, CreateMovie.INPUT_RATING)
        input_text(self.driver, CreateMovie.INPUT_RATING, value)

    def input_movie_time(self, value):
        wait_until_element_is_visible(self.driver, CreateMovie.INPUT_TIME)
        input_text(self.driver, CreateMovie.INPUT_TIME, value)

    def check_error_message(self):
        wait_until_element_is_visible(self.driver, CreateMovie.ERROR_ICON)

