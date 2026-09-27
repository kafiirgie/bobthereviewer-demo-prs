"""discount.py — sample project module (demo-base version).

apply_discount rounds to 2 decimal places.
"""


def apply_discount(price: float, discount_rate: float) -> float:
    """Return price after applying discount_rate (0.0 - 1.0), rounded to 2 d.p."""
    return round(price * (1 - discount_rate), 2)
