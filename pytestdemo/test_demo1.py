#Any pytest file should start with test_ or end with _test keyword
# pytest method name should start with test
# any code should be wrapped in method only
# -k stands for method name execution, -s for logs in out put and -v stands for more info metadate
# you can run specific file with py.test<file name>
# you can run mark (tag) tests @pytest.mark.smoke    and then run with -m
# you can skip test with @pytest.mark.skip
# @py.test.mark.xfail use for showing no status like passed or failed and not impect others skipping programme
# fixture are used as setup and tear down method test cases.conftest file to generalize to fixture and make to avail. to all test cases.
import pytest
#@pytest.fixture()
#def setup():
    #print("i will be executing first")
    #yield
    #print("i will be execute last")

@pytest.mark.smoke
def test_firstprogramedemo(setup):
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])




