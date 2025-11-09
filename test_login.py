import pytest
from playwright.sync_api import sync_playwright 


@pytest.fixture 
def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.wait_for_selector('[data-test="username"]')
        page.fill ('[data-test="username"]', 'standard_user')
        page.fill ('[data-test="password"]','secret_sauce')
        page.click ('[data-test="login-button"]')
        page.wait_for_timeout(4000)

        yield page
    
def test_login (login):
    page = login
    assert 'https://www.saucedemo.com/inventory.html' in page.url, "Login has failed"


     
    
     