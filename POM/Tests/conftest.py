import pytest
from playwright.sync_api import sync_playwright
from Pages.login import Login_page
from Pages.cart import Cart
from Pages.checkout import Checkout
from utils.random_generator import first_name, last_name, postal_code

# Log in fixture
@pytest.fixture 
def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = Login_page(page)
        login_page.login()

        yield page

#cart page fixture
@pytest.fixture
def cart(login):
    page = login
    cart = Cart(page)
    cart.cart_button()

    yield page

#checkout page fixture
@pytest.fixture
def checkout(cart):
    page = cart
    checkout = Checkout(page)
    
    fname = first_name(3)
    lname = last_name(3)
    pcode = postal_code(5)
    
    checkout.checkout_info(fname, lname, pcode)
    
    yield page    