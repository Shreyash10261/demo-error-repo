import pytest
from app_logic import calculate_average, fetch_user_data, string_to_int

def test_calculate_average_normal():
    assert calculate_average([10, 20, 30]) == 20.0

def test_calculate_average_empty():
    # This test will crash because calculate_average doesn't handle empty lists
    assert calculate_average([]) == 0.0

def test_fetch_user_data_valid():
    users = {"u1": "Alice", "u2": "Bob"}
    assert fetch_user_data(users, "u1") == "Alice"

def test_fetch_user_data_invalid():
    users = {"u1": "Alice", "u2": "Bob"}
    # This test will crash because fetch_user_data throws a KeyError instead of returning None
    assert fetch_user_data(users, "u3") is None

def test_string_to_int_invalid():
    # This will crash with ValueError
    assert string_to_int("not_a_number") == 0
