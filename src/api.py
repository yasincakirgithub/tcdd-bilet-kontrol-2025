from curl_cffi import requests as cffi_requests


def post_request(url, body, headers, params):

    return cffi_requests.post(url, json=body, headers=headers, params=params, impersonate="chrome131")
