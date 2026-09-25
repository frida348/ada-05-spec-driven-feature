"""Tests for CustomerSearchService (T-04)."""

from unittest.mock import MagicMock
import pytest
from customer_search.exceptions import InvalidSearchQueryError
from customer_search.models import Customer
from customer_search.repository import InMemoryCustomerRepository
from customer_search.service import CustomerSearchService


def test_service_successful_search() -> None:
    customer = Customer(id="1", name="Ana López", email="ana@example.com")
    repo = InMemoryCustomerRepository([customer])
    service = CustomerSearchService(repository=repo)

    results = service.search("Ana")
    assert results == [customer]


def test_service_empty_results_not_an_error() -> None:
    repo = InMemoryCustomerRepository([])
    service = CustomerSearchService(repository=repo)

    results = service.search("nonexistent")
    assert results == []


def test_service_rejects_empty_query_and_does_not_call_repository() -> None:
    mock_repo = MagicMock()
    service = CustomerSearchService(repository=mock_repo)

    with pytest.raises(InvalidSearchQueryError):
        service.search("")

    mock_repo.find_by_name_or_email.assert_not_called()


def test_service_rejects_whitespace_query_and_does_not_call_repository() -> None:
    mock_repo = MagicMock()
    service = CustomerSearchService(repository=mock_repo)

    with pytest.raises(InvalidSearchQueryError):
        service.search("     ")

    mock_repo.find_by_name_or_email.assert_not_called()


def test_service_uses_custom_validator_if_provided() -> None:
    mock_repo = MagicMock()
    mock_validator = MagicMock()
    service = CustomerSearchService(repository=mock_repo, validator=mock_validator)

    service.search("valid")
    mock_validator.validate.assert_called_once_with("valid")
    mock_repo.find_by_name_or_email.assert_called_once_with("valid")
