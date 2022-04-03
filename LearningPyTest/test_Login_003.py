
import pytest

@pytest.mark.run(order=1)
def test_case_a():
    print("Test 1 ")


@pytest.mark.run(order=3)
def test_case_b():
    print("Test 2 ")

@pytest.mark.run(order=2)
def test_case_c():
    print("Test 3 ")
