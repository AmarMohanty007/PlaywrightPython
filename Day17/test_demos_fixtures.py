"""
Pytest basics lesson covering test functions, fixtures, fixture returns, scopes, and teardown with yield. This file focuses on demos fixtures.
"""

# Fixture : Re-usable function

import pytest

# Function demonstrating the setup concept.
@pytest.fixture
def setup():
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

