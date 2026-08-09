"""Navigation test cases.

NAV-01 verifies primary navigation between Home and Cart.
NAV-02 verifies that modal navigation items open and close the expected modal.

Failure diagnostics: pytest-playwright records trace, screenshot, and video on
failure; pytest-html writes a self-contained report to reports/report.html.
"""

from __future__ import annotations

import re

import pytest
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.home_page import HomePage


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.navigation
def test_nav_01_navigate_between_home_and_cart(
    page: Page,
    home_page: HomePage,
    cart_page: CartPage,
) -> None:
    """Test case NAV-01.

    Intent: verify navigation routes to the catalogue and shopping cart.
    Preconditions: Demoblaze is available; browser context is clean.
    Steps: open home, verify catalogue, select Cart, verify cart, select Home.
    Expected results: STORE title, cart URL/table/button, and visible products.
    """
    home_page.open()

    expect(page).to_have_title("STORE")
    expect(home_page.catalogue).to_be_visible()
    expect(home_page.product_cards.first).to_be_visible()

    home_page.navigation.go_to_cart()

    expect(page).to_have_url(re.compile(r".*/cart\.html$"))
    expect(cart_page.cart_table).to_be_visible()
    expect(cart_page.place_order_button).to_be_visible()

    cart_page.navigation.go_to_home()

    expect(page).to_have_url(re.compile(r".*/index\.html$"))
    expect(home_page.catalogue).to_be_visible()
    expect(home_page.product_cards.first).to_be_visible()


MODAL_CASES = [
    pytest.param("Contact", "New message", id="contact-modal"),
    pytest.param("About us", "About us", id="about-modal"),
    pytest.param("Log in", "Log in", id="login-modal"),
    pytest.param("Sign up", "Sign up", id="signup-modal"),
]


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.navigation
@pytest.mark.parametrize(("nav_item", "expected_title"), MODAL_CASES)
def test_nav_02_verify_modal_based_navigation_items(
    home_page: HomePage,
    nav_item: str,
    expected_title: str,
) -> None:
    """Test case NAV-02.

    Intent: verify modal navigation items display the correct modal.
    Preconditions: Demoblaze is available; browser context is clean.
    Steps: open home, select a modal nav item, verify title, close modal.
    Expected results: modal is visible with the expected title, then hidden.
    """
    home_page.open()

    modal = home_page.navigation.open_modal_by_name(nav_item)

    expect(modal).to_be_visible()
    expect(home_page.navigation.modal_title(nav_item)).to_have_text(expected_title)

    home_page.navigation.close_modal(nav_item)

    expect(modal).to_be_hidden()
