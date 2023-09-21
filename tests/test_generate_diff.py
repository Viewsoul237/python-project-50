import os

import pytest
from gendiff import generate_diff

file1 = os.path.abspath("tests/fixtures/file1.json")
file2 = os.path.abspath("tests/fixtures/file2.json")
file1yaml = os.path.abspath("tests/fixtures/file1.yml")
file2yaml = os.path.abspath("tests/fixtures/file2.yml")
with open(os.path.abspath("tests/fixtures/result")) as file:
    expected = file.read()


@pytest.mark.parametrize(
    "file_1, file_2",
    [
        (file1, file2),
        (file1yaml, file2yaml),
    ]
)
def test_generate_diff(file_1, file_2, ):
    assert generate_diff(file_1, file_2) == expected
