from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from shopbot import settings

DEFAULT_SEARCH_URL = (
    "https://www.bhphotovideo.com/c/search?Ntt=5900x&N=0&InitialSearch=yes"
)


def _attempt(driver, search_url, search_link_text):
    # add item
    driver.get(search_url)
    driver.find_element_by_partial_link_text(search_link_text).click()
    breakpoint()  # TODO :\ bhphoto auth servers broken

    # shopping cart
    driver.get("https://www.bhphotovideo.com/find/cart.jsp")


def attempt_purchase(search_url, search_link_text):
    if not search_url:
        search_url = DEFAULT_SEARCH_URL
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
