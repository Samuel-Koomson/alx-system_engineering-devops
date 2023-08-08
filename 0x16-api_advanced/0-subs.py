#!/usr/bin/python3
"""
Function which queries Reddit API and return number of
Subscribers for a given reddit
Return 0 if invalid sub-reddit is given
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries for number of subscribers
    Args:
        subreddit: String
    Return:
        0 if invalid sub-reddit is given, else number
        of subscribers
    """
    reddit_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    sub_check_url = 'https://www.reddit.com/api/search_reddit_names.json'
    sub_check = requests.get(sub_check_url,
                             headers={
                                 'User-Agent': 'Safari 12.1'
                             },
                             params={
                                 'exact': True,
                                 'query': subreddit
                             })

    if 'error' in sub_check.json():
        return 0

    data = requests.get(reddit_url,
                        headers={'User-Agent': 'Safari 12.1'})

    return data.json().get('data').get('subscribers')


if __name__ == "__main__":
    import sys
    print(number_of_subscribers(sys.argv[1]))
