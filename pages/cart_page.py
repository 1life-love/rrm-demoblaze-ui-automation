"""Shopping cart page object."""

from __future__ import annotations

from playwright.sync_api import Locator, Page

from components.navigation_bar import NavigationBar


class CartPage:
    """Actions and observable state for the Demoblaze shopping cart."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.navigation = NavigationBar(page)
        self.cart_table = page.get_by_role("table")
        self.cart_rows = page.locator("#tbodyid")
        self.place_order_button = page.get_by_role("button", name="Place Order")
        self.order_modal = page.locator("#orderModal")
        self.success_confirmation = page.locator(".sweet-alert")

    def product_row(self, product_name: str) -> Locator:
        """Return the cart row containing a named product."""
        return self.cart_rows.locator("tr", has_text=product_name)

    def product_price_text(self, product_name: str) -> str:
        """Return the price cell text for a product row."""
        row = self.product_row(product_name)
        # Demoblaze cart columns are image, title, price, delete.
        return row.locator("td").nth(2).inner_text().strip()

    def open_order_modal(self) -> None:
        """Open the checkout order modal."""
        self.place_order_button.click()
