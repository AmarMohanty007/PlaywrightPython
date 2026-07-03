


import pytest
from playwright.sync_api import Playwright


def test_google_link(playwright:Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://www.google.com/")
    print("\n",response.status_text)

    headers = response.headers

    for key,value in headers.items():
        #print(key,value)
        print(f"{key}===>{value}")



    assert response.status==200
    assert response.status_text=="OK"

