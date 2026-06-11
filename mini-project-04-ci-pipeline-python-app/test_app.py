import pytest

from app import (
    check_length,
    has_uppercase,
    has_lowercase,
    has_digit,
    password_strength
)


def test_check_length():
    assert check_length("Password1") is True
    assert check_length("Pass1") is False


def test_uppercase():
    assert has_uppercase("Password") is True
    assert has_uppercase("password") is False


def test_lowercase():
    assert has_lowercase("PASSWORD") is False
    assert has_lowercase("Pass") is True


def test_digit():
    assert has_digit("Pass123") is True
    assert has_digit("Password") is False


def test_strong_password():
    assert password_strength("Password1") == "Strong"


def test_medium_password():
    assert password_strength("password1") == "Medium"


def test_weak_password():
    assert password_strength("pass") == "Weak"


def test_empty_password():
    with pytest.raises(ValueError):
        password_strength("")
