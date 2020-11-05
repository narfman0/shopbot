from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from shopbot import settings

DEFAULT_SEARCH_URL = "https://www.newegg.com/p/pl?d=5900x"
SHOPPING_CART_URL = "https://secure.newegg.com/Shopping/ShoppingCart.aspx?Submit=view"


def _attempt(driver, search_url, search_link_text):
    # add item
    driver.get(search_url)
    driver.find_element_by_partial_link_text(search_link_text).click()

    # shopping cart
    driver.get(SHOPPING_CART_URL)
    driver.find_element_by_css_selector(".summary-actions > .btn-primary").click()

    # checkout
    driver.find_element_by_css_selector(
        ".item-cell:nth-child(1) .checkout-step-action-done"
    ).click()  # step 1
    driver.find_element_by_css_selector(
        ".item-cell:nth-child(2) .checkout-step-action-done"
    ).click()  # step 2
    cvv2 = driver.find_element_by_css_selector(".mask-cvv-4")
    ActionChains(driver).click(cvv2).send_keys(settings.CVV2).perform()
    driver.find_element_by_css_selector(
        ".item-cell:nth-child(3) .checkout-step-action > .btn"
    ).click()  # step 3
    # TODO auto checkout? YOLO


def attempt_purchase(search_url, search_link_text):
    # attempt to purchase item from newegg. selenium starts browser anew, so
    # no cookies, no session, thus no login or payment info. for this case,
    # we will start the browser once, input login information, then run the bot.
    # this way, we will stay logged in. a user should change the approach
    # to run full time pro-strat level scalper scams.
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
