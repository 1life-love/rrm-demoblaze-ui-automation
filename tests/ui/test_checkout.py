"""Checkout test cases."""

from __future__ import annotations

import re

import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.order_modal import OrderModal
from pages.product_page import ProductPage
from test_data.order_data import VALID_ORDER


def add_named_product_to_cart(
    home_page: HomePage,
    product_page: ProductPage,
    product_name: str = "Samsung galaxy s6",
) -> None:
    """Add a product to the cart for independent checkout scenarios."""
    home_page.open()
    home_page.open_product(product_name)
    confirmation_message = product_page.add_to_cart()
    assert "Product added" in confirmation_message


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_01_complete_valid_purchase(
    home_page: HomePage,
    product_page: ProductPage,
    cart_page: CartPage,
    order_modal: OrderModal,
) -> None:
    """Test case CHECKOUT-01.

    Intent: verify a customer can complete a valid order.
    Preconditions: Demoblaze is available; browser context is clean.
    Steps: add product, open cart, place order, fill data, purchase, verify success.
    Expected results: success message contains order id, numeric amount, and date.
    """
    add_named_product_to_cart(home_page, product_page)
    product_page.navigation.go_to_cart()

    cart_page.open_order_modal()
    expect(cart_page.order_modal).to_be_visible()

    order_modal.fill_order_information(VALID_ORDER)
    order_modal.purchase()

    expect(order_modal.success_confirmation).to_be_visible()
    expect(order_modal.success_confirmation).to_contain_text("Thank you for your purchase!")

    details = order_modal.parsed_success_details()
    assert details.get("Id"), f"Expected a non-empty order id in {details!r}."
    amount = details.get("Amount", "")
    assert re.search(r"\d+", amount), f"Expected a numeric amount in {details!r}."
    assert details.get("Date"), f"Expected a purchase date in {details!r}."

    order_modal.close_success_confirmation()
    expect(order_modal.success_confirmation).to_be_hidden()


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_02_validate_required_checkout_fields(
    home_page: HomePage,
    product_page: ProductPage,
    cart_page: CartPage,
    order_modal: OrderModal,
) -> None:
    """Test case CHECKOUT-02.

    Intent: verify orders cannot be completed when required fields are blank.
    Preconditions: Demoblaze is available; browser context is clean.
    Steps: add product, open order modal, leave fields blank, purchase.
    Expected results: validation dialog appears; success is hidden; modal remains open.
    """
    add_named_product_to_cart(home_page, product_page)
    product_page.navigation.go_to_cart()
    cart_page.open_order_modal()

    validation_message = order_modal.purchase_expect_validation_dialog()

    assert validation_message == "Please fill out Name and Creditcard."
    expect(order_modal.success_confirmation).to_be_hidden()
    expect(order_modal.modal).to_be_visible()
