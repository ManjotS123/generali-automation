import pytest
from playwright.sync_api import sync_playwright 
from test_login import login

item_selectors = [
    
    ('[data-test="item-4-title-link"]'),
    ('[data-test="item-0-title-link"]'),
    ('[data-test="item-1-title-link"]'),
    ('[data-test="item-5-title-link"]'),
    ('[data-test="item-2-title-link"]'),
    ('[data-test="item-3-title-link"]')
]


@pytest.mark.parametrize('item_selectors', item_selectors)
def test_items(item_selectors, login):
    page = login
    page.click(item_selectors)
    page.click('[data-test="add-to-cart"]')
    
    cart = page.locator('[data-test="shopping-cart-badge"]')
    
    assert int(cart.inner_text()) > 0, 'item was not added to the cart'

    page.close()

    #page.screenshot(path= "C:/Users/manjo/OneDrive/Desktop/gen_Test/Screenshots/items/item.png" )
    
    
