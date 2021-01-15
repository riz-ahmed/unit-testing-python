from fixtures import StudentDB
import pytest

@pytest.fixture(scope='module')
def db():                       # db which is in both the test cases is initalised a module wide function
    print("--------------setup----------------")

    db = StudentDB()
    db.connect('/Volumes/Ext_Programs_Mac/Projects/unit-testing-python/src/data.json')
    yield db                                 # db will be returned and function execution will be stopped here

    print("--------------teardown----------------") # this part of the function will be executed will all the test cases have been executed and pytest exits this execution cycle
    db.close()


def test_scott_data(db):                        # db returned by db function is passed here as an input variable

    scott_data = db.get_data("Scott")
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):

    mark_data = db.get_data("Mark")
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
