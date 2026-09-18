# Build: d4d116c7f97adbcb2a75a12c0a1a8836

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
