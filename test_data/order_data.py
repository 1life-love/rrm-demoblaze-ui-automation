"""Typed checkout data for order tests."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderInformation:
    """Non-sensitive sample customer information for checkout."""

    name: str
    country: str
    city: str
    credit_card: str
    month: str
    year: str


VALID_ORDER = OrderInformation(
    name="Automation Candidate",
    country="Canada",
    city="Winnipeg",
    credit_card="4111111111111111",
    month="08",
    year="2026",
)
