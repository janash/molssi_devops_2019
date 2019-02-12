"""
Testing for the string_util module.
"""
import pytest
import molssi_devops_2019 as md

def test_type_error():
    test_list = []

    with pytest.raises(TypeError):
        md.title_case(test_list)

def test_empty_string():
    test_list = ''

    with pytest.raises(ValueError):
        md.title_case(test_list)

@pytest.mark.parametrize("input_string, output_string", [
('input string', 'Input String'),
('ThIS iS a StRing tO be COnverted.', 'This Is A String To Be Converted.')
])
def test_title_case(input_string, output_string):
    assert md.title_case(input_string) == output_string
