"""Tests for CustomerSearchInterface (T-05)."""

import pytest
from customer_search.exceptions import InvalidSearchQueryError
from customer_search.interface import CustomerSearchInterface
from customer_search.models import Customer
from customer_search.repository import InMemoryCustomerRepository
from customer_search.service import CustomerSearchService


def test_interface_search_delegates_to_service() -> None:
    customer = Customer(id="1", name="Ana López", email="ana@example.com")
    repo = InMemoryCustomerRepository([customer])
    service = CustomerSearchService(repository=repo)
    interface = CustomerSearchInterface(service=service)

    assert interface.search("Ana") == [customer]
    assert interface.search_customers("Ana") == [customer]


def test_interface_search_raises_on_invalid_input() -> None:
    repo = InMemoryCustomerRepository([])
    service = CustomerSearchService(repository=repo)
    interface = CustomerSearchInterface(service=service)

    with pytest.raises(InvalidSearchQueryError):
        interface.search("")

    with pytest.raises(InvalidSearchQueryError):
        interface.search_customers("   ")


def test_interface_execute_search_success_response() -> None:
    customer = Customer(id="1", name="Ana López", email="ana@example.com")
    repo = InMemoryCustomerRepository([customer])
    service = CustomerSearchService(repository=repo)
    interface = CustomerSearchInterface(service=service)

    response = interface.execute_search("Ana")
    assert response.success is True
    assert response.data == [customer]
    assert response.error_message is None


def test_interface_execute_search_failure_response() -> None:
    repo = InMemoryCustomerRepository([])
    service = CustomerSearchService(repository=repo)
    interface = CustomerSearchInterface(service=service)

    response = interface.execute_search("   ")
    assert response.success is False
    assert response.data == []
    assert response.error_message is not None
    assert "whitespace-only" in response.error_message
