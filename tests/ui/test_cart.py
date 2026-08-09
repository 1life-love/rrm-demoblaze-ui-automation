"""Cart test cases."""

from __future__ import annotations

import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage, normalize_price


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_cart_01_add_product_to_cart_and_validate_it(
    home_page: HomePage,
    product_page: ProductPage,
    cart_page: CartPage,
) -> None:
    """Test case CART-01.

    Intent: verify a product can be added and validated in the cart.
    Preconditions: Demoblaze is available; browser context is clean.
    Steps: open home, open Samsung galaxy s6, capture name/price, add to cart,
    handle dialog, open cart, validate matching product and price.
    Expected results: add confirmation appears; cart row and normalized price match.
    """
    home_page.open()
    home_page.open_product("Samsung galaxy s6")
    product_name = product_page.displayed_name()
    product_price = normalize_price(product_page.displayed_price_text())

    confirmation_message = product_page.add_to_cart()

    assert "Product added" in confirmation_message

    product_page.navigation.go_to_cart()

    expect(cart_page.product_row(product_name)).to_be_visible()
    cart_price = normalize_price(cart_page.product_price_text(product_name))
    assert cart_price == product_price, (
        f"Cart price {cart_price} did not match product page price {product_price}."
    )
