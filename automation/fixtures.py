from behave import fixture
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@fixture(name="fixture.browser.chrome")
def browser_chrome(context):
    options = webdriver.ChromeOptions()
    context.browser = Chrome(ChromeDriverManager().install(), options=options)
    context.browser.maximize_window()
    context.browser.implicitly_wait(15)
    yield context.browser
    context.browser.quit()
