
"""Playwright test examples for BlazeDemo and a commented dynamic-table example.

This file contains a sample test that automates booking the cheapest flight
on https://blazedemo.com/ using Playwright's synchronous API. Inline comments
explain each step to make the flow easier to follow for newcomers.

There is also a commented-out dynamic table example (kept for reference).
"""

from playwright.sync_api import Page, expect


# Example (commented out) dynamic table test used as a reference. Left here
# intentionally so you can enable and adapt it later if you want to practice
# reading table data and matching rows.
# def test_dynamic_table(page: Page):
#     page.goto("https://practice.expandtesting.com/dynamic-table")
#     page.wait_for_timeout(5000)
#
#     # Retrieve the CPU Load value for the Chrome process and compare it
#     # against the value displayed in the yellow label.
#     table = page.locator('#table table tbody')
#     rows = page.locator('tr').all()
#
#     column = ()
#     for row in rows:
#         column = page.locator('td').nth(0).inner_text()
#         if column=='Chrome':
#             print(column)
#             break
#     text = page.locator('#chrome-cpu').inner_text()
#     print(text)
#
#     page.close()


def test_flight_booking(page: Page):
    """Book the cheapest available flight on BlazeDemo and verify success.

    Steps:
    - Open the BlazeDemo homepage
    - Select departure and destination cities
    - Find the flight with the lowest price and choose it
    - Fill the purchase form and submit
    - Assert that a success heading is displayed
    """

    # Navigate to the demo site (remove accidental leading space if present)
    page.goto("https://blazedemo.com/")
    # short explicit wait to let the page load (prefer proper waits in real tests)
    page.wait_for_timeout(3000)

    # Select departure and destination from the dropdowns
    departure = page.locator("select[name='fromPort']").select_option("Boston")
    destination_ = page.locator("select[name='toPort']").select_option("London")

    # Submit the form to search flights
    page.locator("input[type='submit']").click()

    # Locate rows of flight results and count them
    rows = page.locator('table.table tbody tr')
    flight_rows = rows.count()
    print("\nTotal number of available flights: ", flight_rows)

    # Collect prices from each row so we can determine the lowest one.
    prices = []
    for i in range(flight_rows):
        # price cell is the 6th td (index 5)
        price_text = rows.nth(i).locator("td").nth(5).inner_text()
        print(price_text)
        prices.append(price_text)
    print(prices)

    # Sort the price strings and pick the first (lowest) value. Note: for
    # production tests convert to numeric values to avoid string-sorting issues.
    sorted_list = sorted(prices)
    lowest_price = sorted_list[0]
    print("Lowest Flight price: ", lowest_price)

    # Click the 'Choose This Flight' button for the row with the lowest price
    for i in range(flight_rows):
        price_text = rows.nth(i).locator("td").nth(5).inner_text()
        if price_text == lowest_price:
            rows.nth(i).locator("input.btn.btn-small").click()
            break

    # Fill out the purchase form
    page.wait_for_timeout(3000)
    page.locator('#inputName').fill("Sunita")
    page.locator('#address').fill("XYZ Street")
    page.locator('#city').fill("Ahmedabad")
    page.locator('#state').fill("Gujarat")
    page.locator('#zipCode').fill("123456")

    # Payment details
    page.wait_for_timeout(3000)
    page.locator('#cardType').select_option("American Express")
    page.locator('#creditCardNumber').fill("1234 5678 8908 2781")
    page.locator('#creditCardMonth').fill("04")
    page.locator('#creditCardYear').fill("2036")
    page.locator('#nameOnCard').fill("Sunita ABC")
    page.locator('#rememberMe').check()

    # Submit purchase and wait for confirmation
    page.get_by_role("button").click()
    page.wait_for_timeout(3000)

    # Verify the success heading is shown
    text = page.get_by_role("heading").inner_text()
    print(text)
    expect(page.get_by_role("heading")).to_contain_text("Thank you for your purchase today!")

    # Print the selected departure/destination values for debug/logging
    print(departure)
    print(destination_)

    # Close the page at the end of the test
    page.close()



