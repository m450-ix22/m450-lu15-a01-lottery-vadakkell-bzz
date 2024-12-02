import pytest
from person import Person

def test_person_properties():
    person = Person('TestUser', 'password', 50.00)
    assert person.givenname == 'TestUser'
    assert person.password == 'password'
    assert person.balance == 50.00

    person.balance = 100.00
    assert person.balance == 100.00

    with pytest.raises(ValueError):
        person.balance = 'invalid'
