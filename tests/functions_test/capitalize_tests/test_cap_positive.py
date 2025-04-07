
import pytest

from core.functions_lesson12.functions import capitalize_text


@pytest.mark.parametrize('input_value, expected_result', [
    ('so what', 'So What')
])

def test_capitalize_text_positive(input_value, expected_result):

    assert capitalize_text(input_value) == expected_result




