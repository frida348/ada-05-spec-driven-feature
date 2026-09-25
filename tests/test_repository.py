"""Tests for Customer Repository search logic (T-03)."""

import pytest
from customer_search.models import Customer
from customer_search.repository import InMemoryCustomerRepository


@pytest.fixture
def sample_customers() -> list[Customer]:
    return [
        Customer(id="1", name="Ana López", email="ana.lopez@example.com"),
        Customer(id="2", name="Anabel García", email="agarcia@gmail.com"),
        Customer(id="3", name="Mariana Torres", email="mariana@empresa.com"),
        Customer(id="4", name="Carlos Ruiz", email="carlos@gmail.com"),
        Customer(id="5", name="Beatriz Ramos", email="beatriz@example.org"),
    ]


def test_search_by_exact_name(sample_customers: list[Customer]) -> None:
    repo = InMemoryCustomerRepository(sample_customers)
    results = repo.find_by_name_or_email("Ana López")
    assert len(results) == 1
    assert results[0].name == "Ana López"


def test_search_by_exact_email(sample_customers: list[Customer]) -> None:
    repo = InMemoryCustomerRepository(sample_customers)
    results = repo.find_by_name_or_email("carlos@gmail.com")
    assert len(results) == 1
    assert results[0].email == "carlos@gmail.com"


def test_search_partial_name(sample_customers: list[Customer]) -> None:
    repo = InMemoryCustomerRepository(sample_customers)
    # 'Ana' matches 'Ana López', 'Anabel García', and 'Mariana Torres'
    results = repo.find_by_name_or_email("Ana")
    names = [c.name for c in results]
    assert len(results) == 3
    assert "Ana López" in names
    assert "Anabel García" in names
    assert "Mariana Torres" in names


def test_search_partial_email(sample_customers: list[Customer]) -> None:
    repo = InMemoryCustomerRepository(sample_customers)
    # 'gmail' matches 'agarcia@gmail.com' and 'carlos@gmail.com'
    results = repo.find_by_name_or_email("gmail")
    emails = [c.email for c in results]
    assert len(results) == 2
    assert "agarcia@gmail.com" in emails
    assert "carlos@gmail.com" in emails


def test_search_case_insensitive(sample_customers: list[Customer]) -> None:
    repo = InMemoryCustomerRepository(sample_customers)
    res_lower = repo.find_by_name_or_email("ana")
    res_mixed = repo.find_by_name_or_email("Ana")
    res_upper = repo.find_by_name_or_email("ANA")

    assert res_lower == res_mixed == res_upper
    assert len(res_lower) == 3


def test_search_no_matches(sample_customers: list[Customer]) -> None:
    repo = InMemoryCustomerRepository(sample_customers)
    results = repo.find_by_name_or_email("nonexistent")
    assert results == []


def test_duplicate_prevention_when_both_name_and_email_match() -> None:
    # Customer whose name contains 'ana' AND email contains 'ana'
    customer = Customer(id="1", name="Ana López", email="ana@example.com")
    repo = InMemoryCustomerRepository([customer])

    results = repo.find_by_name_or_email("ana")
    assert len(results) == 1
    assert results[0] == customer


def test_search_does_not_modify_customer_records(sample_customers: list[Customer]) -> None:
    repo = InMemoryCustomerRepository(sample_customers)
    original_state = [(c.id, c.name, c.email) for c in sample_customers]

    repo.find_by_name_or_email("Ana")
    repo.find_by_name_or_email("nonexistent")

    current_state = [(c.id, c.name, c.email) for c in repo.get_all()]
    assert current_state == original_state


def test_search_is_deterministic(sample_customers: list[Customer]) -> None:
    repo = InMemoryCustomerRepository(sample_customers)
    first_run = repo.find_by_name_or_email("ana")
    second_run = repo.find_by_name_or_email("ana")
    third_run = repo.find_by_name_or_email("ana")

    assert first_run == second_run == third_run
