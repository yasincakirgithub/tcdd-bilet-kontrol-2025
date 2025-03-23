import requests


def post_request(url, body, headers, params):
    return requests.post(url, json=body, headers=headers, params=params)
