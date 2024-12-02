import pytest
from numeric_input import read_int, read_float

def test_read_int(monkeypatch):
    inputs = iter(['5', '42', 'abc', '50'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert read_int('Enter a number', 1, 50) == 5
    assert read_int('Enter a number', 1, 50) == 42

def test_read_float(monkeypatch):
    inputs = iter(['10.5', '55.5', 'abc', '25.0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert read_float('Enter a number', 1.0, 50.0) == 10.5
    assert read_float('Enter a number', 1.0, 50.0) == 25.0
