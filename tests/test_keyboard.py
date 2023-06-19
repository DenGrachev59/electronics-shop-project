import pytest
from src.item import Item
from src.keyboard import KeyBoard

def test_keyboard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    kb.change_lang()

    with pytest.raises(AttributeError):
        kb.language = 'something'
    kb.language = 'EN'
    assert str(kb.language) == "EN"
    kb.language = 'RU'
    assert str(kb.language) == "RU"





