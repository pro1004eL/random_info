import pytest

from core.functions_lesson12.functions import capitalize_text

@pytest.mark.parametrize('input_value', [
    ([123, 'teda']),
    (0),
    (None),
    ({'test'})
])
def test_capitalize_negative(input_value):
    with pytest.raises(AttributeError):
        capitalize_text(input_value)
