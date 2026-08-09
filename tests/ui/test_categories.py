"""Category navigation tests.

NAV-03 verifies that each product category refreshes the catalogue to a known
representative product without relying on fixed sleeps.
"""

from __future__ import annotations

import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from test_data.category_data import CATEGORY_REPRESENTATIVE_PRODUCTS


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.navigation
@pytest.mark.parametrize(
    ("category_name", "representative_product"),
    CATEGORY_REPRESENTATIVE_PRODUCTS.items(),
    ids=lambda value: str(value).lower().replace(" ", "-"),
)
def test_nav_03_verify_product_category_navigation(
    home_page: HomePage,
    category_name: str,
    representative_product: str,
) -> None:
    """Test case NAV-03.

    Intent: verify category navigation updates the product catalogue.
    Preconditions: Demoblaze is available; browser context is clean.
    Steps: open home, select a category, wait for a representative product.
    Expected results: catalogue remains visible and representative product appears.
    """
    home_page.open()

    home_page.select_category(category_name, representative_product)

    expect(home_page.catalogue).to_be_visible()
    expect(home_page.product_card(representative_product)).to_be_visible()
