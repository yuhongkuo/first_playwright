from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    # Step 1: 開啟頁面
    page.goto("https://www.facebook.com/")

    # Step 2: 輸入帳號密碼
    page.fill("#email", "victor167036@gmail.com")
    page.fill("#pass", "win167036")

    # Step 3: 點擊登入
    page.click("button[name='login']")

    page.wait_for_load_state("networkidle")

    browser.close()
