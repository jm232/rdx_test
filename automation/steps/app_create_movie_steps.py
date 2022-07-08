from behave import *

from automation.page_objects.CreateMovie import CreateMovie
from automation.page_objects.ListMovies import ListMovies

from automation.utilities.UtilFunctions import Utils

util = Utils()
log = util.getLoggingConfig()
util = Utils()
config = util.get_config()

@When('I create new movie with name "{name}", rating "{rating}" and time "{time}"')
def step_impl(context, name, rating, time):
    create_movie = CreateMovie(context.browser)
    create_movie.input_movie_name(name)
    create_movie.input_movie_rating(rating)
    create_movie.input_movie_time(time)
    create_movie.click_on_add_movie_button()

@When('I click on Add Movie button')
def step_impl(context):
    create_movie = CreateMovie(context.browser)
    create_movie.click_on_add_movie_button_empty_fields()

@When('I update movie with name "{name}" to name "{updated_name}", rating "{updated_rating}" and time "{updated_time}"')
def step_impl(context, name, updated_name, updated_rating, updated_time):
    list_movie = ListMovies(context.browser)
    list_movie.filter_movie_name(name)
    list_movie.update_movie_name(name)
    create_movie = CreateMovie(context.browser)
    create_movie.input_movie_name(updated_name)
    create_movie.input_movie_rating(updated_rating)
    create_movie.input_movie_time(updated_time)
    create_movie.click_on_update_movie_button()

@Then('I verify error message')
def step_impl(context):
    create_movie = CreateMovie(context.browser)
    create_movie.check_error_message()

