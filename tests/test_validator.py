"""Tests for SearchInputValidator (T-04)."""

import pytest
from customer_search.exceptions import InvalidSearchQueryError, ValidationError
from customer_search.validator import SearchInputValidator


def test_validator_accepts_valid_string() -> None:
    validator = SearchInputValidator()
    validator.validate("Ana")
    assert validator.is_valid("Ana") is True


def test_validator_accepts_single_character() -> None:
    # Q-02 unresolved: no minimum length beyond requiring searchable text
    validator = SearchInputValidator()
    validator.validate("a")
    assert validator.is_valid("a") is True


def test_validator_rejects_empty_string() -> None:
    validator = SearchInputValidator()
    with pytest.raises(InvalidSearchQueryError) as exc_info:
        validator.validate("")
    assert "cannot be empty" in str(exc_info.value)
    assert isinstance(exc_info.value, ValidationError)
    assert isinstance(exc_info.value, ValueError)
    assert validator.is_valid("") is False


def test_validator_rejects_whitespace_only_string() -> None:
    validator = SearchInputValidator()
    with pytest.raises(InvalidSearchQueryError) as exc_info:
        validator.validate("   ")
    assert "whitespace-only" in str(exc_info.value)
    assert validator.is_valid("   ") is False


def test_validator_rejects_tab_and_newline_whitespace() -> None:
    validator = SearchInputValidator()
    with pytest.raises(InvalidSearchQueryError):
        validator.validate("\t  \n ")
    assert validator.is_valid("\t  \n ") is False


def test_validator_rejects_non_string() -> None:
    validator = SearchInputValidator()
    with pytest.raises(InvalidSearchQueryError):
        validator.validate(None)  # type: ignore[arg-type]
    assert validator.is_valid(None) is False  # type: ignore[arg-type]
