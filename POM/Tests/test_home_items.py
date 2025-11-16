import pytest
from playwright.sync_api import sync_playwright 
from test_login import login

Item_home_selectors = [
    ('[data-test="add-to-cart-sauce-labs-backpack"]'),
    ('[data-test="add-to-cart-sauce-labs-bike-light"]'),
    ('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'),
    ('[data-test="add-to-cart-sauce-labs-fleece-jacket"]'),
    ('[data-test="add-to-cart-sauce-labs-onesie"]'),
    ('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')

]

@pytest.mark.parametrize('selectors', Item_home_selectors)
def test_home_items(login, selectors):
    page = login
    page.click(selectors)
    cart = page.locator('[data-test="shopping-cart-badge"]')

    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    assert TimeoutError

    page.close()
