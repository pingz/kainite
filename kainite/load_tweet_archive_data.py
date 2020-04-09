import json
import arrow

def load_tweet_archive_data(
        archive_fn, header='window.YTD.tweet.part0 = ', full=False
):
    with open(archive_fn, 'r') as taf:
        tweets = taf.read()
        tweets = json.loads(tweets[len(header):])

    res = {}

    for t in tweets:
        _t = t['tweet']
        ts = arrow.get(_t['created_at'], 'ddd MMM D HH:mm:ss Z YYYY').timestamp
        id_str = _t['id_str']
        if full:
            res[ts] = _t
        else:
            res[ts] = id_str
    return res
