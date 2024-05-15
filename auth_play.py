import time
from playwright.sync_api import expect

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()

    page.goto('https://agro-management.itcase.pro/auth/')
    page.type('input[data-test-id="usernameFieldInput"]', 'test@itcase.pro')
    page.type('input[data-test-id="passwordFieldInput"]', 'Ki2gxM75QrdDuNH9')
    page.click('button[data-test-id="submitButton"]')
    expect(page).to_have_url('https://agro-management.itcase.pro/')




    #time.sleep(5)
