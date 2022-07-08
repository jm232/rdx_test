from automation.utilities.UtilFunctions import Utils

util = Utils()
log = util.getLoggingConfig()

def get_full_page_screenshot(driver):
    try:
        log.info("Getting full page screenshot..")
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
        driver.set_window_size(S('Width'),
                               S('Height'))
        scheight = .1
        while scheight < 9.9:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
            scheight += .01
        if driver.find_element_by_id('root').screenshot('fail_screenshot.png'):
            return 'fail_screenshot.png'
    except Exception as e:
        log.error("Exception arrived at " + str(e))
        return None
