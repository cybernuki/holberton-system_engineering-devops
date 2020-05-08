#!/usr/bin/python3
"""
This function queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should return None.
"""
import requests

def recurse(subreddit, data_list=[], after=None):
    if type(subreddit) is not str:
        return None
    tmp = subreddit
    api_url = "https://api.reddit.com/r/{}/hot?after={}".format(tmp, after)
    headers = {'user-agent': 'firefox:holberton/0.1.0'}
    res = requests.get(api_url, headers=headers)
    if res.status_code == 200:
        data = res.json()["data"]["children"]
        after = res.json()["data"]["after"]
        if after is None:
            data_list = titles(data, len(data))
            return data_list
        data_list.append(recurse(subreddit, data_list, after=after))
        data_list = titles(data, len(data))
    else:
        return None
    return data_list


def titles(data_list, length, arr=[]):
    """
    Gets titles of posts from the data
    """
    if length == 0:
        return arr
    arr.append(arr[length - 1]["data"]["title"])
    return titles(arr, length - 1, arr)
