"""
test for CI
"""

import pytest # notwendig wegen des @oytest.mark.xfail

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')


from my_second_file import * # das macht herr rhode auch so in seinen Tests!

# tests for my_second_test.py:
def test_func_1():
    assert(my_function_1(5, 5) == 10)

@pytest.mark.xfail # zeige an, dass pytest erwarten soll, dass dieser Test failed und dass dann als erfolgreicher Test interpretiert wird!
def test_func_1_neg():
    assert(my_function_1(5, 5) == 20)

def test_func_2():
    assert(my_function_2(5, 5, 5) == 15)

# tests for my_first_test.py:
# currently no tests available
