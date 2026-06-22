"""
Day 17 - Pytest Fixtures for Setup and Teardown
Demonstrates using pytest fixtures for setup and teardown in tests.
Fixtures are used to set up preconditions before tests and clean up after tests.
This module covers:
- @pytest.fixture decorator
- Using yield for setup/teardown
- Passing fixtures to test functions
- Setup runs before test, teardown after
"""

import pytest

# pytest.fixture decorator is used to create fixture functions
# Fixtures provide setup and teardown functionality

@pytest.fixture
def setup():
    """
    Fixture for setup and teardown.
    Code before yield runs BEFORE the test (setup)
    Code after yield runs AFTER the test (teardown)
    """
    print("Setting up")  # Setup - runs before test
    yield  # Test code runs here
    print("Close...")  # Teardown - runs after test


# Test case covering the one scenario.
def test_one(setup):
    """
    Test function that uses the setup fixture.
    The setup fixture is passed as a parameter.
    Output:
        Setting up (before test)
        Test one Passed (during test)
        Close... (after test)
    """
    print("Test one Passed")


# Test case covering the two scenario.
def test_two():
    """
    Test function without fixture.
    No setup or teardown for this test.
    """
    print("Test two Passed")


# Test case covering the three scenario.
def test_three():
    """
    Another test function without fixture.
    """
    print("Test three Passed")
