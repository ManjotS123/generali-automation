import pytest
from playwright.sync_api import sync_playwright 
from test_login import login

def test_menu_tabs(login):
    page = login
    page.get_by_role("button", name="Open Menu").click()
    page.click('[data-test="inventory-sidebar-link"]')

    #external site page
    #page.click('[data-test="about-sidebar-link"]')

    page.click('[data-test="reset-sidebar-link"]')

    page.click('[data-test="logout-sidebar-link"]')

    page.wait_for_timeout(3000)