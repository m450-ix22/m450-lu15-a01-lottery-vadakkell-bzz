import pytest
from lottery import create_ticket, select_numbers, print_ticket
from ticket import Ticket
from person import Person

@pytest.fixture
def mock_read_int(monkeypatch):
    def mock_input(prompt, minimum, maximum):
        if "Jokerzahl" in prompt:
            return 6
        return 5
    monkeypatch.setattr('lottery.read_int', mock_input)

def test_create_ticket_success(mock_read_int, capsys):
    person = Person('TestUser', 'password', 10.00)
    create_ticket(person)
    output = capsys.readouterr().out
    assert person.balance == 8.00
    assert 'Dein neues Guthaben: 8.00' in output

def test_create_ticket_fail(capsys):
    person = Person('TestUser', 'password', 1.00)
    create_ticket(person)
    output = capsys.readouterr().out
    assert 'Zuwenig Guthaben' in output
