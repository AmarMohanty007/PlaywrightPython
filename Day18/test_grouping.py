"""
Day 18 - Pytest Test Grouping with Markers
Demonstrates how to group tests using @pytest.mark decorator for selective test execution.
This module covers:
- Marking tests with @pytest.mark (e.g., sanity, regression)
- Running tests by marker
- Running tests with multiple markers
- Test organization for CI/CD pipelines
"""

import pytest

# Grouping tests: Test categorization
# test_LoginByEmail -> sanity, regression
# test_LoginByFacebook -> sanity
# test_LoginByPhone -> regression
# test_signupByEmail -> sanity, regression
# test_signupByFacebook -> regression
# test_signupbyphone -> sanity
# test_paymentindollor -> sanity, regression
# test_paymentinrupees -> regression


@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    """Test login with email - both sanity and regression test."""
    print("this is login by email test")
    assert 1 == 1

# Test case covering the loginbyfacebook scenario.
@pytest.mark.sanity
def test_loginbyfacebook():
    """Test login with facebook - sanity test only."""
    print("this is login by facebook")
    assert 1 == 1

# Test case covering the loginbyphone scenario.
@pytest.mark.regression
def test_loginbyphone():
    """Test login with phone - regression test only."""
    print("this is login by phone")
    assert 1 == 1


# Test case covering the signupbyemail scenario.
@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyemail():
    """Test signup with email - both sanity and regression test."""
    print("This is signup by email test")
    assert True == True


# Test case covering the signupbyfacebook scenario.
@pytest.mark.regression
def test_signupbyfacebook():
    """Test signup with facebook - regression test only."""
    print("This is signup by facebook test")
    assert True == True

# Test case covering the signupbyphone scenario.
@pytest.mark.sanity
def test_signupbyphone():
    """Test signup with phone - sanity test only."""
    print("This is signup by phone test")
    assert True == True

# Test case covering the paymentindollor scenario.
@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollor():
    """Test payment in dollar - both sanity and regression test."""
    print("this is payment in dollor test")
    assert 1==1

# Test case covering the paymentinrupess scenario.
@pytest.mark.regression
def test_paymentinrupess():
    """Test payment in rupees - regression test only."""
    print("this is payment in rupees test")
    assert 1==1



'''
PYTEST MARKER COMMANDS - How to run tests by marker:

1) Run only sanity tests (5 tests):
     pytest day18/test_grouping.py -v -s -m "sanity"
      
2) Run only regression tests (6 tests):
     pytest day18/test_grouping.py -v -s -m "regression"

3) Run tests that belong to BOTH sanity AND regression:
     pytest day18/test_grouping.py -v -s -m "sanity and regression"
     
4) Run only sanity tests that are NOT regression:
     pytest day18/test_grouping.py -v -s -m "sanity" -m "not regression"

5) Run only regression tests that are NOT sanity:
     pytest day18/test_grouping.py -v -s -m "regression" -m "not sanity"

MARKER EXPLANATION:
- @pytest.mark.sanity : Marks test as a sanity test (basic functionality)
- @pytest.mark.regression : Marks test as a regression test (full functionality)
- Tests can have multiple markers
- Markers enable selective test execution in CI/CD pipelines
'''
