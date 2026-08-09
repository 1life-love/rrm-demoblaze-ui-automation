"""Navigation bar component shared by Demoblaze pages."""

from __future__ import annotations

from playwright.sync_api import Locator, Page


class NavigationBar:
    """User actions and observable state for the shared top navigation."""

    MODAL_IDS: dict[str, str] = {
        "Contact": "#exampleModal",
        "About us": "#videoModal",
        "Log in": "#logInModal",
        "Sign up": "#signInModal",
    }

    def __init__(self, page: Page) -> None:
        self.page = page
        self.container = page.locator("#navbarExample")

    def go_to_home(self) -> None:
        """Navigate to the product catalogue from the navigation bar."""
        self.container.get_by_role("link", name="Home").click()

    def go_to_cart(self) -> None:
        """Navigate to the shopping cart from the navigation bar."""
        self.container.get_by_role("link", name="Cart", exact=True).click()

    def open_contact_modal(self) -> Locator:
        """Open and return the Contact modal."""
        return self._open_modal("Contact")

    def open_about_modal(self) -> Locator:
        """Open and return the About us modal."""
        return self._open_modal("About us")

    def open_login_modal(self) -> Locator:
        """Open and return the Log in modal."""
        return self._open_modal("Log in")

    def open_signup_modal(self) -> Locator:
        """Open and return the Sign up modal."""
        return self._open_modal("Sign up")

    def open_modal_by_name(self, item_name: str) -> Locator:
        """Open a modal navigation item by its visible link name."""
        return self._open_modal(item_name)

    def modal(self, item_name: str) -> Locator:
        """Return the modal associated with a navigation item."""
        return self.page.locator(self.MODAL_IDS[item_name])

    def modal_title(self, item_name: str) -> Locator:
        """Return the title locator for a navigation item's modal."""
        return self.modal(item_name).locator(".modal-title")

    def close_modal(self, item_name: str) -> None:
        """Close a visible navigation modal by clicking its scoped close control."""
        modal = self.modal(item_name)
        modal.get_by_text("Close", exact=True).click()

    def _open_modal(self, item_name: str) -> Locator:
        self.container.get_by_role("link", name=item_name, exact=True).click()
        return self.modal(item_name)
