from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    MoveTargetOutOfBoundsException,
    ElementClickInterceptedException
)

from .move import move_button_to_viewport

def unlike(driver, ):
    try:
        unlike_btn = article.find_element_by_xpath(
            './/div[@data-testid="unlike"]'
        )
    except NoSuchElementException as exc:
        # logging.exception(exc)
        logging.error(
            'no unlike in the article element'
        )
        return False

    move_button_to_viewport(driver, unlike_btn)
    try:
        unlike_btn.click()
        # webdriver.ActionChains(driver).move_to_element(unlike_btn).click(unlike_bt).perform()
        # sleep(0.5)
    except Exception as exc:
        logging.error('failed to click `unretweet` button')
        return False


