"""
Day 18 - Pytest Test Skipping
Demonstrates how to skip tests using @pytest.mark.skip decorator.
This module covers:
- Skipping specific tests
- Using @pytest.mark.skip decorator
- When to use test skipping (not ready, known issues, etc.)
"""

import pytest

# Test execution flow:
# - test_loginbyemail: RUNS (no decorator)
# - test_loginbyfacebook: SKIPPED (marked with @pytest.mark.skip)
# - test_loginbyphone: SKIPPED (marked with @pytest.mark.skip)
# - test_signupbyemail: RUNS (no decorator)
# - test_signupbyfacebook: SKIPPED (marked with @pytest.mark.skip)
# - test_signupbyphone: SKIPPED (marked with @pytest.mark.skip)

def test_loginbyemail():
    """Test login with email - this test RUNS."""
    print("this is login by email test")
    assert 1 == 1

# Test case covering the loginbyfacebook scenario.
@pytest.mark.skip
def test_loginbyfacebook():
    """Test login with facebook - this test is SKIPPED."""
    print("this is login by facebook")
    assert 1 == 1

# Test case covering the loginbyphone scenario.
@pytest.mark.skip
def test_loginbyphone():
    """Test login with phone - this test is SKIPPED."""
    print("this is login by phone")
    assert 1 == 1


# Test case covering the signupbyemail scenario.
def test_signupbyemail():
    """Test signup with email - this test RUNS."""
    print("This is signup by email test")
    assert True == True


# Test case covering the signupbyfacebook scenario.
@pytest.mark.skip
def test_signupbyfacebook():
    """Test signup with facebook - this test is SKIPPED."""
    print("This is signup by facebook test")
    assert True == True

# Test case covering the signupbyphone scenario.
@pytest.mark.skip
def test_signupbyphone():
    """Test signup with phone - this test is SKIPPED."""
    print("This is signup by phone test")
    assert True == True

# When you run: pytest test_skipping.py -v
# Output will show:
# - test_loginbyemail PASSED
# - test_signupbyemail PASSED
# - test_loginbyfacebook SKIPPED
# - test_loginbyphone SKIPPED
# - test_signupbyfacebook SKIPPED
# - test_signupbyphone SKIPPED
