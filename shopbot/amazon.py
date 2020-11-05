from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from shopbot import settings


def _attempt(driver, search_url, search_link_text):
    # add item
    driver.get(search_url)
    driver.find_element_by_partial_link_text(search_link_text).click()

    # buy now
    driver.find_element_by_css_selector(".a-button-inner > #buy-now-button").click()
    if settings.BUY_NOW:
        driver.find_element_by_css_selector("#turbo-checkout-pyo-button").click()


def attempt_purchase(search_url, search_link_text):
    if not search_url:
        search_url = "https://www.amazon.com/s?k=5900x"
    driver = webdriver.Firefox()
    while True:
        try:
            _attempt(driver, search_url, search_link_text)
            if settings.BREAKPOINT_ON_SUCCESS:
                breakpoint()
            else:
                break
            # user might consider breaking here instead. given we keep the
            # session above i don't want to lose it on false-positives.
        except Exception as e:
            print(e)
            if settings.ABORT_ON_FAILURE:
                break
