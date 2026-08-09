"""Home page object for catalogue and category interactions."""

from __future__ import annotations

from playwright.sync_api import Locator, Page

from components.navigation_bar import NavigationBar


class HomePage:
    """User-facing behaviours and state for the Demoblaze catalogue."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.navigation = NavigationBar(page)
        self.catalogue = page.locator("#tbodyid")
        self.product_cards = self.catalogue.locator(".card")
        self.categories = page.locator(".list-group")

    def open(self) -> None:
        """Open the configured base URL."""
        self.page.goto("/")

    def product_card(self, product_name: str) -> Locator:
        """Return the catalogue card link for a named product."""
        return self.catalogue.get_by_role("link", name=product_name, exact=True).first

    def category_link(self, category_name: str) -> Locator:
        """Return the left navigation link for a product category."""
        return self.categories.get_by_role("link", name=category_name, exact=True)

    def select_category(self, category_name: str, representative_product: str) -> None:
        """Select a category and wait until its representative product is visible."""
        self.category_link(category_name).click()
        self.product_card(representative_product).wait_for(state="visible")

    def open_product(self, product_name: str) -> None:
        """Open a product detail page from the catalogue."""
        self.product_card(product_name).click()
