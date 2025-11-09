import pytest
from playwright.sync_api import sync_playwright 
from test_login import login

def test_menu_button(login):
    page = login
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("button", name="Close Menu").click()