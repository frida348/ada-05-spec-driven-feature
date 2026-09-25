"""Tests for Customer domain model (T-02)."""

import pytest
from customer_search.models import Customer


def test_customer_creation_with_name_and_email() -> None:
    customer = Customer(name="Ana López", email="ana@example.com")
    assert customer.name == "Ana López"
    assert customer.email == "ana@example.com"
    assert customer.id is None


def test_customer_creation_with_id() -> None:
    customer = Customer(name="Carlos Ruiz", email="carlos@gmail.com", id="cust-123")
    assert customer.name == "Carlos Ruiz"
    assert customer.email == "carlos@gmail.com"
    assert customer.id == "cust-123"


def test_customer_equality() -> None:
    c1 = Customer(name="Ana López", email="ana@example.com", id="1")
    c2 = Customer(name="Ana López", email="ana@example.com", id="1")
    assert c1 == c2


def test_customer_name_must_be_string() -> None:
    with pytest.raises(TypeError, match="Customer name must be a string"):
        Customer(name=123, email="test@example.com")  # type: ignore[arg-type]


def test_customer_email_must_be_string() -> None:
    with pytest.raises(TypeError, match="Customer email must be a string"):
        Customer(name="Ana López", email=None)  # type: ignore[arg-type]
