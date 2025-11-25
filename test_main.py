# test_main.py

from main import say_hello

def test_say_hello():
    """
    Test case for the say_hello function.
    """
    # Test with a standard name
    result = say_hello("Alice")
    expected = "Hello, Alice!"
    assert result == expected

    # Test with an empty string
    result_empty = say_hello("")
    expected_empty = "Hello, !"
    assert result_empty == expected_empty

    # Test with a number
    result_number = say_hello("123")
    expected_number = "Hello, 123!"
    assert result_number == expected_number
