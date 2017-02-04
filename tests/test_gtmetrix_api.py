import pytest

print("Got into test.py")
def test_gonna_fail():
    assert True == False  # Going to fail here on line 4

if __name__ == '__main__':
    pytest.main()
