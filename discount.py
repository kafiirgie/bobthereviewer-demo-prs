"""discount.py — sample project module (demo-refactor version).

Structurally different from demo-base, behaviourally identical: the discount factor is
computed in a helper instead of inline. Frozen observations must match demo-base.
"""


def _factor(discount_rate: float) -> float:
    """Return the multiplier for a discount rate."""
    return 1 - discount_rate


def apply_discount(price: float, discount_rate: float) -> float:
    """Return price after applying discount_rate (0.0 - 1.0), rounded to 2 d.p."""
    return round(price * _factor(discount_rate), 2)
