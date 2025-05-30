
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


@pytest.mark.tags("JIRA-6", "ui", "logout")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_standard_user_should_be_able_to_logout_successfully(products_page):
    page = products_page

    expect(page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html", timeout=10000)
    expect(page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_be_visible(timeout=5000)
    menu_button = page.get_by_role(LOCATORS_PRODUCT_PAGE_MENU_BUTTON, name="Open Menu")
    menu_button.wait_for(state="visible", timeout=5000)
    menu_button.click()
    logout_link = page.get_by_role(LOCATORS_PRODUCT_PAGE_LOGOUT_LİNK, name="Logout")
    logout_link.wait_for(state="visible", timeout=5000)
    logout_link.click()
    expect(page).to_have_url(f"{CONSTANTS_BASE_URL}/", timeout=5000)
    expect(page.locator(LOCATORS_AUTH_LOGIN_BTN)).to_be_visible() 