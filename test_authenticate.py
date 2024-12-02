import pytest
from authenticate import login, load_people
from person import Person

@pytest.fixture
def mock_people(monkeypatch):
    def mock_load_people():
        return [
            Person('Inga', 'geheim', 14.00),
            Person('Peter', 'secrät', 7.00),
            Person('Beatrice', 'passWORT', 23.00),
        ]
    monkeypatch.setattr('authenticate.load_people', mock_load_people)

def test_login_success(monkeypatch, mock_people):
    inputs = iter(['geheim'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    person = login()
    assert person.givenname == 'Inga'
    assert person.balance == 14.00

def test_login_fail(monkeypatch, mock_people, capsys):
    inputs = iter(['wrong_password', 'geheim'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    person = login()
    output = capsys.readouterr().out
    assert 'Passwort falsch' in output
    assert person.givenname == 'Inga'
