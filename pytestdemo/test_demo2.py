import pytest


@pytest.mark.smoke
@pytest.mark.skip

def test_firstprogramedemo():
    msg = "Hello"
    assert msg== "Hi", "This test is failed because two string are not match"

def test_secondCreditCard():
    a =4
    b =6
    assert a+2==6,"Addition do not match"

@pytest.fixture()
def setup():
    print("i will be executing first")


def test_fixturedemo(setup):
    print("i will execute steps in fixturedemo method")

