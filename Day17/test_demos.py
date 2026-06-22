"""
Day 17 - Basic Pytest Testing Module
Demonstrates basic pytest test functions and how to run them.
This module covers:
- Basic test functions (must start with 'test_')
- Running tests with pytest command
- Using -s flag to see print() output
- Using -v flag for verbose output
- Running specific tests
"""

import pytest

# Test functions must start with 'test_' prefix for pytest to recognize them

def test_one():
    """First test function - prints test one message."""
    print("this is my test one")

# Test case covering the two scenario.
def test_two():
    """Second test function - prints test two message."""
    print("this is my test two")

# Test case covering the three scenario.
def test_three():
    """Third test function - prints test three message."""
    print("this is my test three")


# Alternative: Using class-based test organization
# class TestClass:
#     def test_one(self):
#         print("this is my test one")
#
#     def test_two(self):
#         print("this is my test two")
#
#     def test_three(self):
#         print("this is my test three")


'''
PYTEST COMMANDS - How to run these tests:

To run all tests in the module:
    pytest test_demos.py
    pytest test_demos.py -s          # Show print() outputs
    pytest test_demos.py -s -v       # Show print() + verbose details

To run specific test function:
    pytest test_demos.py::test_one -s -v      # Run only test_one
    pytest test_demos.py::test_two -s -v      # Run only test_two
    pytest test_demos.py::test_three -s -v    # Run only test_three

FLAG EXPLANATIONS:
    -s  : Shows all print() outputs live in console while test runs
    -v  : Runs pytest in verbose mode with detailed test execution information
    -k  : Run tests matching a pattern (e.g., pytest -k "test_one")
'''
