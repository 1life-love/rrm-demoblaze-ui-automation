"""Shared pytest fixtures and Playwright browser context settings."""

from __future__ import annotations

import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.order_modal import OrderModal
from pages.product_page import ProductPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict[str, object]) -> dict[str, object]:
    """Configure every test context with a consistent desktop profile."""
    return {
        **browser_context_args,
        "viewport": {"width": 1440, "height": 900},
        "locale": "en-CA",
    }


@pytest.fixture
def home_page(page: Page) -> HomePage:
    """Return the home page object for the current isolated page."""
    return HomePage(page)


@pytest.fixture
def product_page(page: Page) -> ProductPage:
    """Return the product detail page object for the current isolated page."""
    return ProductPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """Return the cart page object for the current isolated page."""
    return CartPage(page)


@pytest.fixture
def order_modal(page: Page) -> OrderModal:
    """Return the order modal component for the current isolated page."""
    return OrderModal(page)
