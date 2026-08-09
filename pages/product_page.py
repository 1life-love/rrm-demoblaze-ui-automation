"""Product detail page object."""

from __future__ import annotations

import re

from playwright.sync_api import Page

from components.navigation_bar import NavigationBar


class ProductPage:
    """Actions and observable product detail data."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.navigation = NavigationBar(page)
        self.name = page.locator(".name")
        self.price = page.locator(".price-container")
        self.add_to_cart_button = page.get_by_role("link", name="Add to cart")

    def displayed_name(self) -> str:
        """Return the visible product name."""
        return self.name.inner_text().strip()

    def displayed_price_text(self) -> str:
        """Return the visible product price text."""
        return self.price.inner_text().strip()

    def add_to_cart(self) -> str:
        """Add the product and return the JavaScript dialog confirmation text."""
        with self.page.expect_event("dialog") as dialog_info:
            self.add_to_cart_button.click()
        dialog = dialog_info.value
        message = dialog.message
        dialog.accept()
        return message


def normalize_price(price_text: str) -> int:
    """Extract a numeric price from UI text such as '$360 *includes tax'."""
    match = re.search(r"\d+", price_text.replace(",", ""))
    if match is None:
        raise ValueError(f"Could not extract a numeric price from {price_text!r}.")
    return int(match.group(0))
