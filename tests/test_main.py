"""Provide some test data for the unit tests."""
from aioopenexchangerates.main import add


def test_add():
    """Test the add function."""
    assert add(1, 1) == 2
