from selenium.webdriver.common.by import By

from automation.utilities.ui_utilities import *

util = Utils()
log = util.getLoggingConfig()

class ListMovies:


    BUTTON_DELETE_MOVIE = (By.XPATH, "//div[text()='Delete']")
    BUTTON_UPDATE_MOVIE = (By.XPATH, "//div[text()='Upadate']")
    FILTER_ID = (By.XPATH, "//div[@role='rt-thead -filters']/div[@class='rt-tr']/div[1]/input")
    FILTER_NAME = (By.XPATH, "//div[@class='rt-thead -filters']/div[@class='rt-tr']/div[2]/input")
    FILTER_RATING = (By.XPATH, "//div[@class='rt-thead -filters']/div[@class='rt-tr']/div[3]/input")
    MOVIE_NAME = (By.XPATH, "//div[@role='row']/div[@class='rt-td'][2]")
    MOVIE_RATING = (By.XPATH, "//div[@role='row']/div[@class='rt-td'][3]")
    MOVIE_TIME = (By.XPATH, "//div[@role='row']/div[@class='rt-td'][4]/span")

    def __init__(self, driver):
        self.driver = driver

    def page_loaded(self):
        wait_until_element_is_visible(self.driver, ListMovies.BUTTON_DELETE_MOVIE)

    def filter_movie_name(self, value):
        wait_until_element_is_visible(self.driver, ListMovies.FILTER_NAME)
        input_text(self.driver, ListMovies.FILTER_NAME, value)

    def filter_movie_rating(self, value):
        wait_until_element_is_visible(self.driver, ListMovies.FILTER_RATING)
        input_text(self.driver, ListMovies.FILTER_RATING, value)

    def filter_movie_id(self, value):
        wait_until_element_is_visible(self.driver, ListMovies.FILTER_ID)
        input_text(self.driver, ListMovies.FILTER_ID, value)

    def check_movie_name(self, name):
        element_text_should_be(self.driver, ListMovies.MOVIE_NAME, name)

    def check_movie_rating(self, name):
        element_text_should_be(self.driver, ListMovies.MOVIE_RATING, name)

    def check_movie_time(self, name):
        element_text_should_be(self.driver, ListMovies.MOVIE_TIME, name)

    def delete_movie_name(self, name):
        click_element(self.driver, (By.XPATH, "//div[@class='rt-tr -odd']/div[@class='rt-td'][2][text()='" + name +"']/following-sibling::div/span/div[text()='Delete']"))
        wait_until_alert_is_present(self.driver)
        obj1 = self.driver.switch_to.alert
        log.info(obj1.text)
        obj1.accept()

    def update_movie_name(self, name):
        click_element(self.driver, (By.XPATH, "//div[@class='rt-tr -odd']/div[@class='rt-td'][2][text()='" + name +"']/following-sibling::div/span/div[text()='Upadate']"))
        wait_until_element_is_not_visible(self.driver, ListMovies.BUTTON_UPDATE_MOVIE)

    def check_movie_name_not_present(self, name):
        wait_until_element_is_not_visible(self.driver, (By.XPATH, "//div[@class='rt-tr -odd']/div[@class='rt-td'][2][text()='" + name +"']"))

