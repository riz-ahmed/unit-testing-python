from fixtures import StudentDB
import pytest

db = None
def setup_module(module):                       # module to initialise resources
    print("--------------setup----------------")
    global db                                   # db variable is declared as a global variable
    db = StudentDB()
    db.connect('/Volumes/Ext_Programs_Mac/Projects/unit-testing-python/src/data.json')

def teardown_module(module):                    # module to close down test connections, clear db connections etc
    print("--------------teardown----------------")
    db.close()

def test_scott_data():

    scott_data = db.get_data("Scott")
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data():

    mark_data = db.get_data("Mark")
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
