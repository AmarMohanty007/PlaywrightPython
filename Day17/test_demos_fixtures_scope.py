"""
Pytest basics lesson covering test functions, fixtures, fixture returns, scopes, and teardown with yield. This file focuses on demos fixtures scope.
"""

# Fixture : Re-usable function

# scope="function"  fixture will be called before every test function executes
# scope="module"   fixture will be called only once before test functions executes
# scope="class"   fixture will be called only once before the class
# scope="session"  fixture will be called only once for session


# module --> class --> methods
# module --> function


import pytest

# Function demonstrating the setup concept.
@pytest.fixture
def setup(scope="module"):
    print("setup browser..")

# Test case covering the one scenario.
def test_one(setup):
    print("this is my test one")

# Test case covering the two scenario.
def test_two(setup):
    print("this is my test two")

# Test case covering the three scenario.
def test_three(setup):
    print("this is my test three")

