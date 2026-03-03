"""Unit tests for the calculator module."""

import pytest
from src.calculator import Calculator, format_result, validate_number


class TestCalculator:
    """Test cases for the Calculator class."""

    @pytest.fixture
    def calc(self):
        """Create a Calculator instance for testing."""
        return Calculator()

    def test_add(self, calc):
        """Test addition operation."""
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self, calc):
        """Test subtraction operation."""
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(1, 1) == 0
        assert calc.subtract(0, 5) == -5

    def test_multiply(self, calc):
        """Test multiplication operation."""
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 100) == 0

    def test_divide(self, calc):
        """Test division operation."""
        assert calc.divide(10, 2) == 5.0
        assert calc.divide(7, 2) == 3.5
        assert calc.divide(-10, 2) == -5.0

    def test_divide_by_zero(self, calc):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_power(self, calc):
        """Test power operation."""
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(2, -1) == 0.5

    def test_sqrt(self, calc):
        """Test square root operation."""
        assert calc.sqrt(4) == 2.0
        assert calc.sqrt(9) == 3.0
        assert calc.sqrt(2) == pytest.approx(1.414, rel=1e-3)

    def test_history(self, calc):
        """Test that operations are recorded in history."""
        calc.add(1, 2)
        calc.multiply(3, 4)

        history = calc.get_history()
        assert len(history) == 2
        assert history[0]["operation"] == "add"
        assert history[1]["operation"] == "multiply"

    def test_clear_history(self, calc):
        """Test clearing the calculation history."""
        calc.add(1, 2)
        calc.clear_history()

        assert len(calc.get_history()) == 0
        assert calc.last_result is None


class TestUtils:
    """Test cases for utility functions."""

    def test_format_result_integer(self):
        """Test formatting integer results."""
        assert format_result(42) == "42"
        assert format_result(0) == "0"

    def test_format_result_float(self):
        """Test formatting float results."""
        assert format_result(3.14159, 2) == "3.14"
        assert format_result(3.14159, 4) == "3.1416"

    def test_validate_number_valid(self):
        """Test validation with valid numbers."""
        assert validate_number(42) is True
        assert validate_number(3.14) is True
        assert validate_number("123") is True
        assert validate_number("-45.67") is True

    def test_validate_number_invalid(self):
        """Test validation with invalid inputs."""
        assert validate_number("abc") is False
        assert validate_number(None) is False
        assert validate_number([1, 2, 3]) is False
