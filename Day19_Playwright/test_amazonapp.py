"""
Playwright introduction covering browser launch, page navigation, sync and async tests, and basic assertions. This file focuses on amazonapp.
"""

from playwright.sync_api import expect, sync_playwright


# Test case covering the amazon login scenario.
def test_amazon_login():
    """Launch Chromium, sign in to Amazon and perform a search.

    Notes/fixes applied:
    - Removed unused/incorrect imports (idlelib, pyautogui, re, Page).
    - Avoid running the test at import time; keep it as a pytest-style test function.
    - Replaced ad-hoc sleeps and pyautogui calls with Playwright waits and a dialog handler.
    - Ensured browser is closed in a finally-like flow.
    """
    with sync_playwright() as p:
        # Launch Chromium in headful mode and request a maximized window.
        # --start-maximized requests the browser to open maximized; viewport=None
        # tells Playwright to use the actual browser window size for the context.
        # Use the user's screen size so the browser opens with that window size.
        browser = p.chromium.launch(headless=False, args=["--start-maximized", "--window-size=1521,730"])
        context = browser.new_context(viewport=None)
        page = context.new_page()

        # Handle any JS dialog that might appear during navigation by dismissing it.
        page.on("dialog", lambda dialog: dialog.dismiss())

        try:
            page.goto("https://www.amazon.in/")
            # # wait for the page to finish loading resources
            # page.wait_for_load_state("networkidle")

            logo = page.locator('[aria-label="Amazon.in"]')
            expect(logo).to_be_visible(timeout=5000)

            # open sign-in panel
            page.locator("#nav-link-accountList-nav-line-1").click()

            # wait for email input and fill
            page.wait_for_selector('input[name="email"]', timeout=8000)
            page.fill('input[name="email"]', '7504312001')
            page.locator('input.a-button-input').click()

            # wait for password field, fill and submit
            page.wait_for_selector('#ap_password', timeout=10000)
            page.fill('#ap_password', 'Amar@3934')
            page.click('#signInSubmit')

            # wait for search box, perform a search and wait for results
            page.wait_for_selector('input#twotabsearchtextbox', timeout=10000)
            page.fill('input#twotabsearchtextbox', 'DJI Go Pro')
            page.click('input#nav-search-submit-button')
            page.wait_for_load_state('networkidle')

        finally:
            # Close browser/context to free resources
            try:
                context.close()
            except Exception:
                pass
            try:
                browser.close()
            except Exception:
                pass


