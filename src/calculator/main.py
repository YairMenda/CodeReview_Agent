"""Main calculator module with basic arithmetic operations."""

import math
from typing import Union

# Hardcoded precision - intentional demo issue (should be configurable)
DECIMAL_PRECISION = 2


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self):
        self.history = []
        self.last_result = None

    def add(self, a, b):  # Missing type hints - intentional demo issue
        """Add two numbers."""
        result = a + b
        self._record_operation("add", a, b, result)
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        result = a - b
        self._record_operation("subtract", a, b, result)
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        result = a * b
        self._record_operation("multiply", a, b, result)
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._record_operation("divide", a, b, result)
        return round(result, DECIMAL_PRECISION)

    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent."""
        result = math.pow(base, exponent)
        self._record_operation("power", base, exponent, result)
        return result

    def sqrt(self, n):  # Missing type hints - intentional demo issue
        """Calculate the square root of n.

        Note: No negative number check - intentional demo issue
        """
        result = math.sqrt(n)  # Will raise ValueError for negative numbers
        self._record_operation("sqrt", n, None, result)
        return result

    def _record_operation(self, operation: str, a, b, result) -> None:
        """Record an operation in history."""
        entry = {
            "operation": operation,
            "operand_a": a,
            "operand_b": b,
            "result": result
        }
        self.history.append(entry)
        self.last_result = result

    def get_history(self) -> list:
        """Return the calculation history."""
        return self.history

    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history = []
        self.last_result = None
