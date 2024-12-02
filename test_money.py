import pytest
from money import transfer_money, select_transaction
from person import Person

@pytest.fixture
def mock_read_float(monkeypatch):
    def mock_input(prompt, minimum, maximum):
        if 'Auszahlung' in prompt:
            return 10.00
        return 20.00
    monkeypatch.setattr('money.read_float', mock_input)

def test_transfer_money_deposit(mock_read_float, monkeypatch):
    person = Person('TestUser', 'password', 50.00)
    inputs = iter(['E', 'Z'])  # 'E' for deposit, 'Z' to exit
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 70.00  # 50 + 20

def test_transfer_money_withdraw(mock_read_float, monkeypatch):
    person = Person('TestUser', 'password', 50.00)
    inputs = iter(['A', 'Z'])  # 'A' for withdrawal, 'Z' to exit
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 40.00  # 50 - 10

def test_transfer_money_invalid_balance(mock_read_float, monkeypatch):
    person = Person('TestUser', 'password', 0.00)
    inputs = iter(['A'])  # Attempt to withdraw
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(ValueError):
        transfer_money(person)
