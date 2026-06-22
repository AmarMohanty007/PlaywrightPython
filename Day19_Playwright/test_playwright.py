"""
Day 19 - Playwright Browser Automation Basics
Introduces Playwright for web browser automation testing.
Demonstrates browser navigation, page verification, and element interaction.
This module covers:
- Navigating to URLs using page.goto()
- Verifying page URLs with expect()
- Verifying page titles
- Locating elements on page
- Using Playwright assertions
"""

import time
from playwright.sync_api import Page, expect


# Test case covering the verifyPageUrl scenario.
def test_verifyPageUrl(page: Page):
    """
    Test to verify the page URL is correct.

    Steps:
    1. Navigate to the application URL
    2. Get the current page URL
    3. Assert that the URL matches expected value

    Args:
        page: Playwright Page fixture (browser automation object)
    """
    # Navigate to the application
    page.goto("https://demowebshop.tricentis.com/")

    # Get the current URL of the page
    myurl = page.url
    print("Url of the application:", myurl)

    # Verify that the page URL matches expected value
    expect(page).to_have_url("https://demowebshop.tricentis.com/")


# Test case covering the verifyTitle scenario.
def test_verifyTitle(page: Page):
    """
    Test to verify the page title is correct.

    Steps:
    1. Navigate to the application URL
    2. Get the page title
    3. Assert that the title matches expected value

    Args:
        page: Playwright Page fixture
    """
    # Navigate to the application
    page.goto("https://demowebshop.tricentis.com/")

    # Get the title of the page
    mytitle = page.title()
    print("Title of the page:", mytitle)

    # Verify that the page title matches expected value
    expect(page).to_have_title("Demo Web Shop")


# Test case covering the amazonlogin scenario.
def test_amazonlogin(page: Page):
    """
    Test to navigate to Amazon and locate the logo element.

    Steps:
    1. Navigate to Amazon India
    2. Wait for page to load
    3. Locate the logo element using XPath
    4. Print the located element

    Args:
        page: Playwright Page fixture
    """
    # Navigate to Amazon India
    page.goto("https://www.amazon.in/")

    # Wait for 5 seconds for page to load
    time.sleep(5)

    # Locate the Amazon logo using XPath
    # XPath: //*[@id="nav-logo-sprites"]
    logo = page.locator('//*[@id="nav-logo-sprites"]')
    print(logo)
