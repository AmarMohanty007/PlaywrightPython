import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_context():
    """Create a browser context for the test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headed mode
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


def test_search_product(browser_context):
    """
    Test scenario:
    1. Open http://www.automationpractice.pl/index.php
    2. Search for "T-shirts"
    3. Verify that "Faded Short Sleeve T-shirts" is displayed in the search results
    """
    page = browser_context
    
    # Step 1: Open the website
    print("Step 1: Opening http://www.automationpractice.pl/index.php")
    try:
        response = page.goto("http://www.automationpractice.pl/index.php", timeout=30000, wait_until="domcontentloaded")
        print(f"Page loaded, response status: {response.status if response else 'None'}")
    except Exception as e:
        print(f"Warning: Load error: {e}, continuing...")
    
    page.wait_for_timeout(2000)
    print(f"Current URL: {page.url}")
    
    # Step 2: Search for "T-shirts"
    print("Step 2: Searching for 'T-shirts'")
    
    search_input = None
    
    # Try different selectors for the search input
    selectors = [
        "input[name='search_query']",
        "input[name='s']",
        "input[type='search']",
        "input.search-input",
        "#search_query"
    ]
    
    for selector in selectors:
        try:
            element = page.query_selector(selector)
            if element:
                print(f"Found search input with selector: {selector}")
                search_input = page.locator(selector)
                break
        except Exception as e:
            pass
    
    if not search_input:
        print("ERROR: Could not find search input!")
        page.screenshot(path="aitesting/search_input_not_found.png")
        raise Exception("Could not find search input")
    
    # Fill the search box
    search_input.fill("T-shirts")
    page.wait_for_timeout(500)
    print("Filled search input with 'T-shirts'")
    
    # Find and click search button
    button_selectors = [
        "button[name='submit_search']",
        "input[type='submit'][name='submit_search']",
        "button.submit",
        "input.submit",
        "button:has-text('Search')"
    ]
    
    search_button = None
    for selector in button_selectors:
        try:
            element = page.query_selector(selector)
            if element:
                print(f"Found search button with selector: {selector}")
                search_button = page.locator(selector)
                break
        except:
            pass
    
    if search_button:
        search_button.click()
        print("Clicked search button")
    else:
        print("Search button not found, pressing Enter")
        search_input.press("Enter")
    
    # Wait for results to load
    print("Waiting for search results to load...")
    page.wait_for_load_state("networkidle", timeout=30000)
    print(f"Results page URL: {page.url}")
    
    # Step 3: Verify that "Faded Short Sleeve T-shirts" is displayed in the search results
    print("Step 3: Verifying 'Faded Short Sleeve T-shirts' in search results")
    
    # Take screenshot for debugging
    page.screenshot(path="aitesting/search_result_debug.png")
    print("Screenshot saved to aitesting/search_result_debug.png")
    
    # Try to find the product
    product_text = "Faded Short Sleeve T-shirts"
    
    # Method 1: Check if text is in page content
    page_content = page.content()
    if product_text in page_content:
        print(f"✓ Found product text in page content: {product_text}")
        assert True
        return
    
    # Method 2: Try to find with locator
    try:
        locator = page.locator(f"text={product_text}")
        if locator.is_visible(timeout=5000):
            print(f"✓ Found product with locator: {product_text}")
            assert True
            return
    except Exception as e:
        print(f"Locator text search failed: {e}")
    
    # Method 3: Look for partial matches
    try:
        locators = page.locator("h5, .productname, .product-name")
        count = locators.count()
        print(f"Found {count} potential product elements")
        for i in range(count):
            try:
                element = locators.nth(i)
                text = element.text_content()
                print(f"  Product {i}: {text}")
                if "Faded Short Sleeve T-shirts" in text or "Faded" in text and "T-shirt" in text:
                    print(f"✓ Found matching product: {text}")
                    assert True
                    return
            except:
                pass
    except Exception as e:
        print(f"Error checking product elements: {e}")
    
    raise AssertionError(f"'{product_text}' not found in search results")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
