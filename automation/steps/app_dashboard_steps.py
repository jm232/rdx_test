from behave import *

from automation.page_objects.Dashboard import Dashboard
from automation.page_objects.ListMovies import ListMovies
from automation.page_objects.CreateMovie import CreateMovie

from automation.utilities.UtilFunctions import Utils

util = Utils()
log = util.getLoggingConfig()
util = Utils()
config = util.get_config()

@Given('I enter simple app')
def step_impl(context):
    context.browser.get(context.url)
    dashboard = Dashboard(context.browser)
    dashboard.page_loaded()

@Then('I go to Create Movie page')
def step_impl(context):
    dashboard = Dashboard(context.browser)
    dashboard.click_on_create_movie_button()
    create_movie = CreateMovie(context.browser)
    create_movie.page_loaded()

@Then('I go to List Movies page')
def step_impl(context):
    dashboard = Dashboard(context.browser)
    dashboard.click_on_list_movies_button()
    list_movie = ListMovies(context.browser)
    list_movie.page_loaded()

