

# ===================================== #
# Tests
# Ref: https://playwright.dev/python/docs/test-assertions
# ===================================== #
import pytest
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *

@pytest.mark.tags("JIRA-5", "ui", "cart")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_standard_user_should_be_able_to_add_products_to_cart(products_page):
    page=products_page 
    # Auto waiting
    # -------------
    # Ref: https://playwright.dev/python/docs/actionability
    products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    products_page.wait_for_timeout(2000) # Explicit wait for 2 seconds (delay)

    page.locator(LOCATORS_PRODUCT_PAGE_ADD_TO_CART_BUTTON).click()
    page.locator(LOCATORS_PRODUCT_PAGE_CART_ICON).click()
    page.locator(LOCATORS_CART_CONTINUE_BUTTON).click()
    page.locator(LOCATORS_PRODUCT_PAGE_ADD_BIKE_LIGHT_TO_CART).click()
    page.locator(LOCATORS_PRODUCT_PAGE_ADD_FLEECE_JACKET_TO_CART).click()
    page.locator(LOCATORS_PRODUCT_PAGE_ADD_BOLT_T_SHIRT_TO_CART).click()
    page.locator(LOCATORS_PRODUCT_PAGE_CART_ICON).click()
    page.locator(LOCATORS_CART_PAGE_REMOVE_BOLT_T_SHIRT).click()
    page.locator(LOCATORS_CART_PAGE_REMOVE_FLEECE_JACKET).click()
    