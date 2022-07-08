import platform

import allure
from allure_commons.types import AttachmentType
from behave import use_fixture
from automation.utilities.screenshot_utils import get_full_page_screenshot
from fixtures import browser_chrome
from automation.utilities.folder_operations import folder
from automation.utilities.UtilFunctions import Utils

util = Utils()
local_config = util.get_config()
log = util.getLoggingConfig()

def before_all(context):
    context.os_name = platform.system()
    print("os name::", context.os_name)
    context.test_case_ids = []

    context.url = local_config['main']['url']
    context.endpoint = local_config['main']['endpoint']
    context.api_movie_base = local_config['api']['movie_base']
    context.api_list_movies = local_config['api']['list_all_movies']


    folder.create_directory("reports")
    folder.create_directory("output")
    folder.create_directory("Logs")

def before_feature(context, feature):
    log.info('Executing Feature - ' + feature.name)


def before_step(context, step):
    log.info('Executing Step - ' + step.name)


def after_step(context, step):
    log.info('Step Name - ' + step.name)
    if step.status == 'failed' and hasattr(context, 'browser'):
        log.info('Taking screenshot')
        screenshot = get_full_page_screenshot(context.browser)
        if screenshot is not None:
            allure.attach.file(screenshot, name="Screenshot", attachment_type=AttachmentType.PNG)
        else:
            allure.attach(context.browser.get_screenshot_as_png(), name="Screenshot"
                          , attachment_type=AttachmentType.PNG)

def before_scenario(context, feature):
    log.info('Scenario Execution is starting')

def before_tag(context, tag):
    log.info(tag + ' tag is starting')
    if tag == "ui":
        use_fixture(browser_chrome, context)

def after_tag(context, tag):
    log.info(tag + ' tag is completed')

def after_scenario(context, feature):
    log.info('Scenario Execution is completed')

def after_feature(context, feature):
    log.info('Execution for Feature is completed  - ' + feature.name)


def after_all(context):
    log.info('Teared Down Framework')
