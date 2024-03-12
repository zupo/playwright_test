from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

for browser_type in ["chromium", "firefox", "webkit"]:
    with sync_playwright() as p:
        print(f"Running test on {browser_type}")
        browser = getattr(p, browser_type).launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://nixos.org/")
        expect(page.get_by_text("Declarative builds and deployments")).to_be_visible()
