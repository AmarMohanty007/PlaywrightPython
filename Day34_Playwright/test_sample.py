"""
Playwright reporting lesson covering Allure attachments and pytest report hooks. This file focuses on sample.
"""

from playwright.sync_api import Page, expect


# Test case covering the url scenario.
def test_url(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    expect(page).to_have_url("https://www.demoblaze.com/index.html")


# Test case covering the Title scenario.
def test_Title(page: Page):
    page.goto('https://www.demoblaze.com/index.html')
    expect(page).to_have_title("STORE")


# Test case covering the google search scenario.
def test_google_search(page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")


# Test case covering the bing search scenario.
def test_bing_search(page):
    page.goto("https://www.bing.com/")
    expect(page).to_have_title("Bing123") #Intensionally failed
