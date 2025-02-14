#qui vanno scritti gli assert coi casi "positivi" e quelli "negativi"

import pytest
from collections import Counter

def test_count_happy_path():
    assert Counter(["aldo"]) == {"aldo": 1}
    assert Counter(["aldo", "aldo"]) == {"aldo": 2}
    assert Counter(["aldo", "aldo", "giovanni"]) == {"aldo": 2, "giovanni": 1}

def test_count_unhappy_path():
    with pytest.raises(AssertionError): #potevamo scegliere il tipo di errore
        assert Counter(None)