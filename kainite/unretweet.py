from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    MoveTargetOutOfBoundsException,
    ElementClickInterceptedException
)

from .move import move_button_to_viewport

import logging

def unretweet(driver, article):
    try:
        unrw_btn = article.find_element_by_xpath(
            './/div[@data-testid="unretweet"]'
        )
    except NoSuchElementException as exc:
        # logging.exception(exc)
        logging.error(
            'no unretweet in the article element'
        )
        return False

    move_button_to_viewport(driver, unrw_btn)

    try:
        unrw_btn.click()
        # webdriver.ActionChains(driver).move_to_element(unrw_btn).click(unrw_btn).perform()
        # sleep(0.5)
    except Exception as exc:
        logging.error('failed to click `unretweet` button')
        return False

    try:
        confirm_btn = driver.find_element_by_xpath(
            ".//div[@data-testid='unretweetConfirm']"
            "//span[text()='Undo Retweet']"
        )
    except NoSuchElementException as exc:
        # logging.exception(exc)
        logging.info(
            "can't find `confirm delete` button "
            "after click `delete` button."
        )
        return False
    logging.info('confirm deleting')
    confirm_btn.click()
    # webdriver.ActionChains(driver).move_to_element(confirm_btn).click(confirm_btn).perform()
    return True
