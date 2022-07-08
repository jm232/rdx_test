from behave import *

from automation.page_objects.ListMovies import ListMovies

from automation.utilities.UtilFunctions import Utils

util = Utils()
log = util.getLoggingConfig()
util = Utils()
config = util.get_config()

@Then('I verify movie is present with name "{name}", rating "{rating}" and time "{time}"')
def step_impl(context, name, rating, time):
    list_movie = ListMovies(context.browser)
    list_movie.filter_movie_name(name)
    list_movie.check_movie_name(name)
    list_movie.check_movie_rating(rating)
    list_movie.check_movie_time(time)

@Then('I delete movie with name "{name}"')
def step_impl(context, name):
    list_movie = ListMovies(context.browser)
    list_movie.filter_movie_name(name)
    list_movie.delete_movie_name(name)
    list_movie.check_movie_name_not_present(name)

@Then('I filter movie name "{name}" by value "{value}"')
def step_impl(context, name, value):
    list_movie = ListMovies(context.browser)
    list_movie.filter_movie_name(value)
    list_movie.check_movie_name(name)

