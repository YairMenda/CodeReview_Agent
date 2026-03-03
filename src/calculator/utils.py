"""Utility functions for the calculator module."""

from typing import Union


def format_result(value: Union[int, float], precision: int = 2) -> str:
    """Format a numeric result as a string with specified decimal precision.

    Args:
        value: The numeric value to format
        precision: Number of decimal places (default: 2)

    Returns:
        Formatted string representation of the value
    """
    if isinstance(value, int):
        return str(value)
    return f"{value:.{precision}f}"


def validate_number(value) -> bool:  # Missing type hint for parameter - intentional demo issue
    """Check if a value is a valid number.

    Args:
        value: The value to validate

    Returns:
        True if the value is a valid number, False otherwise
    """
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def parse_expression(expression: str) -> tuple:
    """Parse a simple mathematical expression.

    Note: Very basic parsing - intentional demo issue (no proper validation)

    Args:
        expression: A string like "5 + 3" or "10 / 2"

    Returns:
        Tuple of (operand_a, operator, operand_b)
    """
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Expression must be in format: 'a operator b'")

    a = float(parts[0])  # No validation - intentional demo issue
    operator = parts[1]
    b = float(parts[2])  # No validation - intentional demo issue

    return (a, operator, b)
