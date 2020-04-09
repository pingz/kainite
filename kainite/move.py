import logging

def move_button_to_viewport(driver, button):
    logging.info(
        "do some calculate, "
        "move `more` button into the viewport, "
        "if it was located outside of the viewport."
    )
    viewport_height = driver.get_window_size()['height']
    button_y = button.location['y']
    if button_y >= viewport_height:
        logging.info(
            'the button is below the viewport bottom, '
            'scroll down'
        )
        driver.execute_script(
            'window.scrollTo(%s,%s);' % (
                0, button_y - viewport_height / 2 + 50,
            )
        )
    elif button_y <= 0 :
        logging.info(
            'the button is above the viewport bottom, '
            'scroll up'
        )
        driver.execute_script(
            'window.scrollTo(%s,%s);' % (
                0, button_y - viewport_height / 2,
            )
        )
    else:
        logging.info(
            'the button should in the viewport, no move'
        )
