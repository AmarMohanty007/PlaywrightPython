"""
Playwright dropdown and method lesson covering bootstrap dropdowns, autosuggest lists, and page/locator methods. This file focuses on autosuggestdropdown flipkart.
"""

import pytest
from playwright.sync_api import sync_playwright, expect, Page


# Test case covering the autosuggest dropdown scenario.
def test_autosuggest_dropdown(page: Page):
    # Step 1: Open Flipkart
    page.goto("https://www.flipkart.com/")

    # Close the Login Option
    page.wait_for_timeout(3000)
    page.locator('span.b3wTlE').click()

    # Step 2: Type "smart" in the search box
    page.wait_for_timeout(3000)
    search_box = page.locator("input.nw1UBF.v1zwn25:visible").fill("smart")
    # expect(search_box).to_be_visible()  # Assert dropdown is visible
    # expect(search_box).to_be_enabled()  #Assert dropdown is enabled
    # search_box.fill("smart")
    print(search_box)

    # Wait for suggestions to appear
    page.wait_for_timeout(5000)

    # Step 3: Locate all suggestions
    options = page.locator("ul > li")
    count = options.count()
    print("Number of suggested options:", count)

    # Assertion: Expect at least 1 suggestion
    expect(options).to_have_count(count)

    # Step 4: Print the 5th option (index starts from 0)
    if count > 5:
        print("5th option:", options.nth(5).inner_text())

    print("Printing all auto suggestions...")
    for i in range(count):
        print(options.nth(i).text_content())

    # Step 5: Select "smartphone" if it appears
    for i in range(count):
        text = options.nth(i).inner_text()
        if text.strip().lower() == "smartphone":
            options.nth(i).click()
            break

    page.wait_for_timeout(3000)
