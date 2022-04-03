
import pytest

@pytest.mark.Regression
def test_case_a():
    print("Test 1 for regression")

@pytest.mark.Regression
@pytest.mark.Smoke
def test_case_b():
    print("Test 2 for somketest")
