"""
Playwright date-picker lesson covering jQuery date pickers, bootstrap date pickers, and hover assignment flow. This file focuses on Assignment.
"""


import pytest

from playwright.sync_api import Page

# Helper function that demonstrates mouse interactions for mouse hover.
def mouse_hover(page: Page):

    page.get_by_text('Cancel').hover()
