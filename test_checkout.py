import pytest
from playwright.sync_api import sync_playwright 
from test_login import login
from test_cart import cart
from random_generator import first_name, last_name, postal_code

@pytest.fixture
def checkout(cart):
    page = cart
    page.click('[data-test="checkout"]')
    
    page.fill('[data-test="firstName"]', first_name(3))

    page.fill('[data-test="lastName"]', last_name(3))

    page.fill('[data-test="postalCode"]', postal_code(5))

    yield page

def test_checkout(checkout):
    page = checkout
    assert 'https://www.saucedemo.com/checkout-step-two.html' in page.url, 'checkout not successful'

def test_cancel(cart):
    page = cart
    page.click('[data-test="cancel"]')

def test_checkout_two(checkout):
    page = checkout
    page.click('[data-test="finish"]')


def test_checkout_complete(checkout):
    page = checkout
    page.click('[data-test="back-to-products"]')    

