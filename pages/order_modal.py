"""Checkout order modal object."""

from __future__ import annotations

import re

from playwright.sync_api import Dialog, Locator, Page

from test_data.order_data import OrderInformation


class OrderModal:
    """User actions and success details for Demoblaze checkout."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.modal = page.locator("#orderModal")
        self.success_confirmation = page.locator(".sweet-alert")

    @property
    def purchase_button(self) -> Locator:
        """Return the scoped purchase button."""
        return self.modal.get_by_role("button", name="Purchase")

    def fill_order_information(self, order: OrderInformation) -> None:
        """Fill the checkout fields with typed order data."""
        self.modal.locator("#name").fill(order.name)
        self.modal.locator("#country").fill(order.country)
        self.modal.locator("#city").fill(order.city)
        self.modal.locator("#card").fill(order.credit_card)
        self.modal.locator("#month").fill(order.month)
        self.modal.locator("#year").fill(order.year)

    def purchase(self) -> None:
        """Submit the current order information."""
        self.purchase_button.click()

    def purchase_expect_validation_dialog(self) -> str:
        """Submit invalid order data and return the validation dialog text."""
        messages: list[str] = []

        def accept_validation_dialog(dialog: Dialog) -> None:
            messages.append(dialog.message)
            dialog.accept()

        self.page.once("dialog", accept_validation_dialog)
        self.purchase_button.click()
        if not messages:
            raise AssertionError("Expected checkout validation dialog, but none appeared.")
        message = messages[0]
        return message

    def success_details_text(self) -> str:
        """Return the full confirmation details text."""
        return self.success_confirmation.locator("p").inner_text().strip()

    def parsed_success_details(self) -> dict[str, str]:
        """Parse order id, amount, and date from the confirmation details."""
        details = self.success_details_text()
        parsed: dict[str, str] = {}
        for key in ("Id", "Amount", "Card Number", "Name", "Date"):
            match = re.search(rf"{key}:\s*(.+)", details)
            if match:
                parsed[key] = match.group(1).strip()
        return parsed

    def close_success_confirmation(self) -> None:
        """Close the completed purchase confirmation."""
        self.success_confirmation.get_by_role("button", name="OK").click()
