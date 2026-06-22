"""
Playwright dropdown lesson covering single-select, multi-select, sorted dropdowns, and product sorting. This file focuses on single dropdown.
"""

import time

import pytest
from playwright.sync_api import expect, Page


# Test case covering the single dropdown scenario.
def test_single_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.locator('#country').select_option(label="India")
    page.locator('#name').fill("Amar TCS")
    time.sleep(2)
    page.locator('#email').fill("abc@gmail.com")
    time.sleep(2)
    page.locator('#phone').fill("1234567890")
    time.sleep(2)
    page.locator('#textarea').fill("Bhubaneswar, Odisha")
    time.sleep(2)
    page.locator('#male').check()
    time.sleep(2)
    page.locator('#sunday').check()
    page.locator('#monday').check()
    page.locator('#tuesday').check()
    time.sleep(2)
    dropdown_value = page.locator('#country').select_option(label="India")
    print(dropdown_value)
    time.sleep(5)
