import logging
from time import sleep

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, MoveTargetOutOfBoundsException, ElementClickInterceptedException

from .move import move_button_to_viewport

def delete_on_article(driver, article):
    page = driver.find_element_by_tag_name('body')

    try:
        more_btn = article.find_element_by_xpath(
            ".//div[@aria-label='More']"
        )
    except NoSuchElementException as exc:
        logging.error(
            "can't locate the `more` button, give up\n, article:\n{}".format(
                article.get_attribute('innerHTML')
            )
        )
        return False


    logging.debug(more_btn)

    move_button_to_viewport(driver, more_btn)
    # viewport_height = driver.get_window_size()['height']
    # more_btn_y = more_btn.location['y']
    # if more_btn_y >= viewport_height:
    #     driver.execute_script(
    #         'window.scrollTo(%s,%s);' % (
    #             0, more_btn_y - viewport_height / 2 + 50,
    #         )
    #     )
    # elif more_btn_y <= 0 :
    #     driver.execute_script(
    #         'window.scrollTo(%s,%s);' % (
    #             0, more_btn_y - viewport_height / 2,
    #         )
    #     )
    # else:
    #     logging.info('no move, `more` button should in the viewport')

    logging.info('click `more` button')
    try:
        ## two way to click on an element
        # webdriver.ActionChains(driver).move_to_element(more_btn).click(more_btn).perform()
        more_btn.click()
        ## do we really need a sleep here?
        # sleep(0.2)
    except MoveTargetOutOfBoundsException as exc:
        logging.error('move out side the bounds')
        logging.exception(exc)
        return False
    except ElementClickInterceptedException as exc:
        logging.exception(exc)
        return False
    except Exception as exc:
        logging.exception(exc)
        return False

    try:
        delete_btn = driver.find_element_by_xpath(
            ".//div[@role='menu']"
            "//span[text()='Delete']"
        )
    except NoSuchElementException as exc:
        logging.info(
            "can't find `delete` button "
            "after click `more` button."
        )
        return False

    logging.info('click `delete` button')
    # webdriver.ActionChains(driver).move_to_element(delete_btn).click(delete_btn).perform()
    delete_btn.click()
    # sleep(0.2)

    try:
        confirm_btn = driver.find_element_by_xpath(
            ".//div[@data-testid='confirmationSheetConfirm']"
            "//span[text()='Delete']"
        )
    except NoSuchElementException as exc:
        # logging.exception(exc)
        logging.info(
            "can't find `confirm delete` button "
            "after click `delete` button."
        )
        return False

    logging.info('confirm deleting')
    # webdriver.ActionChains(driver).move_to_element(confirm_btn).click(confirm_btn).perform()
    confirm_btn.click()
    # sleep(1)
    return True
