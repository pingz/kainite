from .setup_driver import setup_driver
from .delete_tweets_from_archive_file import delete_tweets_from_archive_file

def main(author, tweet_archive_fn, fx_profile_dir, rate=12, start_ts=None, end_ts=None):
    driver = setup_driver(fx_profile_dir)
    delete_tweets_from_archive_file(
        driver, author, tweet_archive_fn, rate, start_ts, end_ts
    )

