#!/usr/bin/python3
"""
This function queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    if after is None:
        return []

    url_redd = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url_redd += "?limit=100&after={}".format(after)
    headers = {'user-agent': 'request'}
    response = requests.get(url_redd, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return None
    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")
    for post in hot_posts_json:
        hot_list.append(post.get("data").get("title"))
    return hot_list + recurse(subreddit, [], r_json.get("data").get("after"))
