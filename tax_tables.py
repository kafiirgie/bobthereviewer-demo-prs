"""tax_tables.py — added by the demo-broken-import Act.

The base revision cannot import this module, so a probe targeting it must come out
`inconclusive` with reason `import_error` rather than a pass or a fail.
"""

RATES = {"ID": 0.11, "SG": 0.09}


def rate_for(region: str) -> float:
    """Return the tax rate for a region."""
    return RATES[region]
