import pytest

from core.functions_lesson12.functions import word_count

@pytest.mark.parametrize('input_value, expected_result', [
    ('text 3 words', 3),
    ('text 4 words 4', 4),
])
def test_word_count_positive(input_value, expected_result):

    assert word_count(input_value) == expected_result


