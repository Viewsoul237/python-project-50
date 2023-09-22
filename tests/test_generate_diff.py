import os

import pytest
from gendiff import generate_diff

file1 = os.path.abspath("tests/fixtures/file1.json")
file2 = os.path.abspath("tests/fixtures/file2.json")
file1yaml = os.path.abspath("tests/fixtures/file1.yml")
file2yaml = os.path.abspath("tests/fixtures/file2.yml")
file1nested = os.path.abspath("tests/fixtures/nested1.json")
file2nested = os.path.abspath("tests/fixtures/nested2.json")
with open(os.path.abspath("tests/fixtures/result")) as file:
    expected = file.read()
with open(os.path.abspath("tests/fixtures/flat_result")) as file:
    flat_expected = file.read()
format = "plain"


@pytest.mark.parametrize(
    "file_1, file_2",
    [
        (file1, file2),
        (file1yaml, file2yaml),
    ]
)
def test_generate_diff(file_1, file_2):
    assert generate_diff(file_1, file_2) == expected


def test_generate_diff_nested():
    assert generate_diff(file1nested, file2nested, format) == flat_expected
