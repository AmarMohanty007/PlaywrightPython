"""
Playwright dropdown lesson covering single-select, multi-select, sorted dropdowns, and product sorting. This file focuses on Assignment.
"""

# Import necessary modules from pytest and playwright
import pytest
from playwright.sync_api import expect, Page

# Test function to verify dropdown functionality on BStack demo application
def test_demo_application(page: Page):
    # Navigate to the BStack demo website
    page.goto("https://www.bstackdemo.com/")

    # Wait for 5 seconds to allow page to load
    page.wait_for_timeout(5000)

    # Locate the sort dropdown element using CSS selector
    # display = page.locator('#value').select_option(value="lowestprice")
    order_by_dropdown = page.locator("div.sort>select")

    # Verify that the dropdown is visible on the page
    expect(order_by_dropdown).to_be_visible()

    # Verify that the dropdown is enabled and interactive
    expect(order_by_dropdown).to_be_enabled()

    # Select the "Lowest to highest" option from the dropdown
    order_by_dropdown.select_option(label="Lowest to highest")

    # Print the dropdown element for debugging purposes
    print(order_by_dropdown)

    # Close the browser page
    page.close()


