import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    "file_1, file_2, format, result",
    [
        # №1 Testing flat files (json/yml)
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.yml",
            "stylish",
            "tests/fixtures/result",
        ),

        # №2 Testing flat files (yaml/json)
        (
            "tests/fixtures/file1.yaml",
            "tests/fixtures/file2.json",
            "stylish",
            "tests/fixtures/result",
        ),

        # №3 Testing nested files (json/json)
        (
            "tests/fixtures/nested1.json",
            "tests/fixtures/nested2.json",
            "stylish",
            "tests/fixtures/nested_result",
        ),

        # №4 Testing nested files (yml/json)
        (
            "tests/fixtures/nested1.yml",
            "tests/fixtures/nested2.json",
            "stylish",
            "tests/fixtures/nested_result",
        ),

        # №5 Testing nested files (json/yaml) # plain output
        (
            "tests/fixtures/nested1.json",
            "tests/fixtures/nested2.yaml",
            "plain",
            "tests/fixtures/flat_result",
        ),

        # №6 Testing nested files (yml/yaml) # json output
        (
            "tests/fixtures/nested1.yml",
            "tests/fixtures/nested2.yaml",
            "json",
            "tests/fixtures/json_result.json",
        ),
    ]
)
def test_generate_diff(file_1, file_2, format, result):
    with open(result) as file:
        expected = file.read()
        assert generate_diff(file_1, file_2, format) == expected
