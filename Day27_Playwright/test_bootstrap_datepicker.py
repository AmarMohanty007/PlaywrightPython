"""
Playwright date-picker lesson covering jQuery date pickers, bootstrap date pickers, and hover assignment flow. This file focuses on bootstrap datepicker.
"""

from playwright.sync_api import sync_playwright, expect, Page

# Helper function to select check-in date in a Bootstrap datepicker
def select_checkin_date(page, year, month, day):
    # Wait for datepicker to be visible
    page.wait_for_selector('table.b8fcb0c66a tbody', timeout=10000)
    page.wait_for_timeout(1000)  # Wait for animations

    # Navigate through months until the desired check-in month and year are found
    max_attempts = 12
    attempt = 0

    while attempt < max_attempts:
        try:
            checkin_month_year = page.locator("h3[aria-live='polite']").nth(0).inner_text()
            current_month, current_year = checkin_month_year.split(" ")

            if current_month == month and current_year == year:
                break
            else:
                # Click next month button to navigate forward
                page.locator('button[aria-label="Next month"]').click()
                page.wait_for_timeout(500)
                attempt += 1
        except Exception as e:
            print(f"Error navigating months: {e}")
            break

    # Get all date cells from the first datepicker table and find the target day
    all_dates = page.locator('table.b8fcb0c66a tbody').nth(0).locator('td').all()
    for date in all_dates:
        if date.inner_text().strip() == day:
            date.click()
            break



# Helper function to select check-out date in a Bootstrap datepicker
def select_checkout_date(page, year, month, day):
    # Wait for any animations
    page.wait_for_timeout(500)

    # Navigate through months until the desired check-out month and year are found
    max_attempts = 12
    attempt = 0

    while attempt < max_attempts:
        try:
            checkout_month_year = page.locator("h3[aria-live='polite']").nth(1).inner_text()
            current_month, current_year = checkout_month_year.split(" ")

            if current_month == month and current_year == year:
                break
            else:
                # Click next month button to navigate forward
                page.locator('button[aria-label="Next month"]').click()
                page.wait_for_timeout(500)
                attempt += 1
        except Exception as e:
            print(f"Error navigating checkout months: {e}")
            break

    # Get all date cells from the second datepicker table and find the target day
    all_dates = page.locator('table.b8fcb0c66a tbody').nth(1).locator('td').all()
    for date in all_dates:
        if date.inner_text().strip() == day:
            date.click()
            break



# Test to verify booking.com date picker functionality
def test_booking_date_picker(page: Page):
    # Navigate to the booking.com website
    page.goto("https://www.booking.com/", wait_until="networkidle")

    # Wait for page to fully load
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(3000)  # Additional wait for dynamic content

    # Handle potential cookie/consent popups
    try:
        # Dismiss cookie consent if it appears
        page.locator("button:has-text('Accept')").first.click(timeout=2000)
    except:
        pass  # Cookie popup may not appear

    # Wait for the date picker element to be visible
    page.wait_for_selector('[data-testid="searchbox-dates-container"]', timeout=30000)

    # Click on the date picker search box to open the datepicker modal
    page.get_by_test_id("searchbox-dates-container").click(timeout=10000)


    # Select check-in date for October 10, 2025
    select_checkin_date(page, "2025", "October", "10")
    page.wait_for_timeout(1000)

    # Select check-out date for November 5, 2025
    select_checkout_date(page, "2025", "November", "5")
    page.wait_for_timeout(1000)

    # Retrieve the selected check-in and check-out dates for assertion
    checkin_text = page.locator("span[data-testid='date-display-field-start']").inner_text()
    checkout_text = page.locator("span[data-testid='date-display-field-end']").inner_text()

    # Print the selected dates for debugging
    print("Check-in date:===>", checkin_text)
    print("Check-out date: ===>", checkout_text)

    # Assert that the selected dates are displayed correctly in the date fields
    expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_text)
    expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_text)

    # Wait for 5 seconds for visual verification (optional)
    page.wait_for_timeout(5000)
