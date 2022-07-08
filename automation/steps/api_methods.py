import allure
import requests
from behave import *
from hamcrest import assert_that, equal_to
import json
from json import JSONDecodeError

from automation.utilities.UtilFunctions import Utils

util = Utils()
config = util.get_config()
log = util.getLoggingConfig()

header = {"Connection": "keep-alive",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept": "*/*",
          "Content-Type": "application/json"}

@When('I call GET request on movies service')
def step_impl(context):
    url = context.endpoint + config['api']['list_all_movies']
    context.response = requests.get(url=url, headers=header, verify=True)

@When('I call GET request on movie service "{id}"')
def step_impl(context, id):
    url = context.endpoint + config['api']['movie_base'] + "/" + id
    context.response = requests.get(url=url, headers=header, verify=True)

@When('I call POST request on movie service without body')
def step_impl(context):
    url = context.endpoint + config['api']['movie_base']
    context.response = requests.post(url=url, headers=header, verify=True)

@When('I call POST request on movie service')
def step_impl(context):
    url = context.endpoint + config['api']['movie_base']
    context.response = requests.post(url=url, headers=header, json=json.loads(context.text), verify=True)

@Then('I log response from the server')
def step_impl(context):
    log.info(context.response.json())

@Then('I get a "{code:d}" response')
def step_impl(context, code):
    try:
        response_json = context.response.json()
    except JSONDecodeError:
        log.error('Decoding response JSON has failed;' + str(context.response.status_code))
        log.error('Decoding response JSON has failed;' + context.response.text)
        raise AssertionError('Decoding response JSON has failed; status code '
                             + str(context.response.status_code) + " " + context.response.text)
    log.info(json.dumps(response_json, indent=4))
    allure.attach(json.dumps(response_json, indent=4), name='response', attachment_type=allure.attachment_type.JSON)
    assert_that(context.response.status_code, equal_to(code))

@When('I call PUT request on movie service "{name}"')
def step_impl(context, name):
    response_json = context.response.json()
    value_id = None
    for key in response_json["data"]:
        if key["name"] == name:
            value_id = key["_id"]
            break
    url = context.endpoint + config['api']['movie_base'] + "/" + value_id
    context.response = requests.put(url=url, headers=header, json=json.loads(context.text), verify=True)