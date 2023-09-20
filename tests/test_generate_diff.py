import os

import pytest

from gendiff import generate_diff


@pytest.fixture
def file1():
    return os.path.abspath("tests/fixtures/file1.json")


@pytest.fixture
def file2():
    return os.path.abspath("tests/fixtures/file2.json")


@pytest.fixture
def expected():
    with open(os.path.abspath("tests/fixtures/json_result")) as file:
        return file.read()


def test_generate_diff(file1, file2, expected):
    assert generate_diff(file1, file2) == expected
