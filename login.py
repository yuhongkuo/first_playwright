from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    # Step 1: 開啟頁面
    page.goto("https://www.saucedemo.com/")

    # Step 2: 輸入帳號密碼
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    # Step 3: 點擊登入
    page.click("#login-button")

    page.wait_for_load_state("networkidle")

    browser.close()
