'''
Pre-requisite:  Install a pytest plugin "pytest-xdist" to run tests parallel
pip install pytest-xdist
'''

# Test case covering the one scenario.
def test_one():
    print("running test one")
    assert True

# Test case covering the two scenario.
def test_two():
    print("Running test two")
    assert True

# Test case covering the three scenario.
def test_three():
    print("Running test three")
    assert True

# Test case covering the four scenario.
def test_four():
    print("Running test four")
    assert True


'''
To runt he tests parallely:

    pytest day17/test_parallel.py -v -s -n=2 
    pytest day17/test_parallel.py -v -s -n 2 

'''
