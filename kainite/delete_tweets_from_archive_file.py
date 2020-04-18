from time import sleep
import logging

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, MoveTargetOutOfBoundsException, ElementClickInterceptedException

from .delete_on_article import delete_on_article
from .unretweet import unretweet

from .load_tweet_archive_data import load_tweet_archive_data

def check_article(article, author):
    try:
        author_link = article.find_element_by_xpath(
            './/div[@data-testid="tweet"]//a[@role="link"]'
        )
    except NoSuchElementException as exc:
        logging.exception(exc)
        return False
    except StaleElementReferenceException as exc:
        logging.exception(exc)
        return False

    author_url = author_link.get_attribute('href')
    if author_url != 'https://twitter.com/{}'.format(author):
        logging.info('not your article')
        return False
    return True

def delete_tweets_from_id(
        driver, id_str, author, rate, sorted_reverse
):
    tweet_url = 'https://twitter.com/{}/status/{}' \
        .format(author, id_str)
    driver.get(tweet_url)
    sleep(rate)
    articles = driver.find_elements_by_tag_name('article')
    if sorted_reverse:
        articles = articles[::-1]
    for ar in articles:
        if check_article(ar, author):
            delete_on_article(driver, ar)
        else:
            unretweet(driver, ar)

def delete_tweets_from_archive_file(
        driver, author, tweet_archive_fn,
        rate=15, start_ts=None, end_ts=None, retries=10,
        sorted_reverse=False,
):
    tweets = load_tweet_archive_data(tweet_archive_fn)
    for k in sorted(tweets.keys(), reverse=sorted_reverse):
        retry_cntr = retries

        if start_ts and k < start_ts:
            logging.info(
                'current ts {} is ahead of start ts {}'
                .format(k, start_ts)
            )
            continue
        if end_ts and k > end_ts:
            logging.info(
                'current ts {} is behind end ts {}'
                .format(k, end_ts)
            )
            break
        logging.info('current ts {}'.format(k, start_ts))
        while retry_cntr > 0:
            retry_cntr -= 1
            try:
                delete_tweets_from_id(
                    driver, tweets[k], author,
                    rate, sorted_reverse
                )
            except StaleElementReferenceException as exc:
                logging.error(
                    'page have been refreshed, try again'
                )
                continue
            break
