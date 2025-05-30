

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


@pytest.mark.tags("JIRA-2", "ui", "inventory")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_inventory_page_should_be_able_to_see_product_list(products_page):
    page = products_page
    expect(page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")
    expect(page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(page.locator(LOCATORS_PROUCTS_PAGE_PRODUCT_LIST)).to_have_count(CONSTANTS_PRODUCT_COUNT)

@pytest.mark.tags("JIRA-3", "ui", "product-name-and-price-verification")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_product_names_and_prices_are_displayed_correctly(products_page):
    page = products_page

    actual_names = page.locator(LOCATORS_PRODUCTS_PAGE_PRODUCT_NAMES).all_text_contents()
    actual_prices = page.locator(LOCATORS_PRODUCTS_PRICES).all_text_contents()
    assert actual_names == CONSTANTS_EXPECTED_PRODUCT_NAMES
    assert actual_prices == CONSTANTS_EXPECTED_PRODUCT_PRICES

@pytest.mark.tags("JIRA-4", "ui", "sorting")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_sorting_products_by_price(products_page):
    page = products_page

    expect(page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")
    expect(page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_be_visible(timeout=5000)
    expect(page.locator(LOCATORS_SORT_DROPDOWN)).to_be_visible(timeout=5000)
    page.locator(LOCATORS_SORT_DROPDOWN).select_option("lohi")
    price_elements = page.locator(LOCATORS_PRODUCTS_PRICES)
    prices = price_elements.all_inner_texts()
    numeric_prices = [float(price.replace("$", "")) for price in prices]
    assert numeric_prices == sorted(numeric_prices), f"Prices are not sorted low to high: {numeric_prices}"