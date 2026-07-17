from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    print("Loading page with networkidle wait...")
    try:
        # Use networkidle which waits for network to be idle
        page.goto("http://www.automationpractice.pl/index.php", 
                  timeout=60000, 
                  wait_until="networkidle")
    except Exception as e:
        print(f"Navigation error (continuing anyway): {e}")
    
    # Wait for stabilization
    time.sleep(5)
    
    print(f"Current URL after navigation: {page.url}")
    print(f"Page title: {page.title()}")
    
    # Take a screenshot first
    page.screenshot(path="aitesting/page_debug.png")
    print("Screenshot saved")
    
    # Try to get a small snippet of HTML
    try:
        title_element = page.query_selector("title")
        if title_element:
            print(f"Title element found: {title_element.text_content()}")
    except Exception as e:
        print(f"Error getting title: {e}")
    
    # Try to access HTML via different method
    try:
        body = page.query_selector("body")
        if body:
            print("Body element exists")
        else:
            print("No body element found")
    except Exception as e:
        print(f"Error: {e}")
    
    context.close()
    browser.close()


