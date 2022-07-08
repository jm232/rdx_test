import time

from selenium.common.exceptions import TimeoutException

from automation.utilities.UtilFunctions import Utils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

util = Utils()

def wait_until_element_is_clickable(driver, element_locator):
    print('Wait for element to clickable: ' + str(element_locator))
    wait = WebDriverWait(driver, 3)
    wait.until(EC.element_to_be_clickable(element_locator))


def wait_until_element_is_visible(driver, element_locator):
    print('Wait for element to be visible: ' + str(element_locator))
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.presence_of_element_located(element_locator))
    except TimeoutException:
        print("arrived at exception: " + str(TimeoutException))
        raise AssertionError(f'Element is not visible: {element_locator}')


def click_element(driver, element_locator):
    print('Click on element: ' + str(element_locator))
    wait_until_element_is_clickable(driver, element_locator)
    driver.find_element(*element_locator).click()

def wait_until_alert_is_present(driver):
    print('Wait until alert is present')
    time.sleep(1)
    wait = WebDriverWait(driver, 3)
    return wait.until(EC.alert_is_present())


def get_element_text(driver, element_locator):
    print('Get element text: ' + str(element_locator))
    wait_until_element_is_visible(driver, element_locator)
    return driver.find_element(*element_locator).text


def element_text_should_be(driver, element_locator, expected_text):
    print('Verify element text for: ' + str(element_locator))
    try:
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(element_locator, expected_text))
    except TimeoutException:
        print("arrived at exception: " + str(TimeoutException))
        actual_element = get_element_text(driver, element_locator)
        raise AssertionError(f'Expected element: {expected_text}; Received: {actual_element}; ')

def wait_until_element_is_not_visible(driver, element_locator):
    print('Wait until element is not visible: ' + str(element_locator))
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(EC.invisibility_of_element_located(element_locator))
    except TimeoutException:
        print("arrived at exception: " + str(TimeoutException))
        raise AssertionError(f'Element is not invisible : {element_locator}')


def input_text(driver, element_locator, text):
    print('Input Text: ' + str(element_locator))
    wait_until_element_is_visible(driver, element_locator)
    driver.find_element(*element_locator).clear()
    driver.find_element(*element_locator).send_keys(text)

