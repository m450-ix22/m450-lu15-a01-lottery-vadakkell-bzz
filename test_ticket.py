import pytest
from ticket import Ticket

def test_ticket_properties():
    ticket = Ticket(5, [1, 2, 3, 4, 5, 6])
    assert ticket.joker == 5
    assert ticket.numbers == [1, 2, 3, 4, 5, 6]

    ticket.joker = 3
    assert ticket.joker == 3

    with pytest.raises(ValueError):
        ticket.joker = 'invalid'
